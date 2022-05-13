from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import themed_tk
import addbookwindow
import removewindow
import conexao
import requisicaodialog


# Funções


def copy(window, entry_search):
    window.clipboard_clear()
    window.clipboard_append(entry_search.selection_get())


def cut(window, entry_search):
    window.clipboard_clear()
    window.clipboard_append(entry_search.selection_get())
    if entry_search.index(ANCHOR) < entry_search.index(INSERT):
        entry_search.delete(ANCHOR, INSERT)
    elif entry_search.index(INSERT) < entry_search.index(ANCHOR):
        entry_search.delete(INSERT, ANCHOR)


def paste(window, entry_search):
    entry_search.insert(entry_search.index(INSERT), window.clipboard_get())
    window.clipboard_clear()


def procurar_livro(entry_search, list_search):
    print(entry_search.get())
    con = conexao.connect()
    cursor = conexao.create_cursor(con)
    conexao.query(
        cursor,
        '''SELECT DISTINCT titulo, isbn, autor, editora, data_publicacao, Nome, REQUISITADO.designacao, LIVROS.id
            FROM LIVROS, GENEROS, LIVROS_GENEROS, REQUISITADO
            WHERE LIVROS_GENEROS.id_livro = LIVROS.id
            AND
            LIVROS.id_requisitado = REQUISITADO.id
            AND
            (Nome LIKE \'%'''+entry_search.get()+'''%\'
            OR titulo LIKE \'%'''+entry_search.get()+'''%\'
            OR autor LIKE \'%'''+entry_search.get()+'''%\'
            OR editora LIKE \'%'''+entry_search.get()+'''%\'
            OR data_publicacao LIKE \'%'''+entry_search.get()+'%\')'
    )
    fetch = conexao.fetch(cursor)
    for i in list_search.get_children():
        list_search.delete(i)
    for i in fetch:
        list_search.insert('', END, values=i)
    con.close()


def requisitar_livro(list_search):
    livro_selection = list_search.selection()
    id_livro = []
    titulo_livro = []
    for i in range(len(livro_selection)):
        id_livro.append(list_search.item(livro_selection[i])['values'][7])
        titulo_livro.append(list_search.item(livro_selection[i])['values'][0])
    requisicaodialog.criar_dialog(id_livro, titulo_livro)


def entregar_livro(list_search):
    livro_selection = list_search.selection()
    id_livro = []
    titulo_livro = []
    for i in range(len(livro_selection)):
        id_livro.append(list_search.item(livro_selection[i])['values'][7])
        titulo_livro.append(list_search.item(livro_selection[i])['values'][0])
    if messagebox.askyesno(title='Confirmar Entrega', message='Deseja entregar o(s) livro(s) '+str(titulo_livro)+' ?'):
        try:
            con = conexao.connect()
            cursor = conexao.create_cursor(con)
            for i in id_livro:
                query_statement = '''UPDATE REQUISICOES_HEADER, DESCRICOES_DESC
                    SET devolvido = 1 WHERE REQUISICOES_HEADER.id = DESCRICOES_DESC.id_requisicao
                    AND DESCRICOES_DESC.id_livro = \''''+str(i)+'''\';
                    UPDATE LIVROS
                    SET id_requisitado = 2 WHERE id = \''''+str(i)+'\''
                conexao.query(cursor, query_statement)
        except Exception:
            messagebox.showerror(title='Erro', message='Não foi possível Entregar o(s) livro(s)')
            con.close()
        else:
            con.commit()
            messagebox.showinfo(title='Sucesso', message='Entrega concluida')
            con.close()


# Função construtora


def criar_janela():

    # Janela
    window = themed_tk.ThemedTk(
        theme='breeze'
    )
    window.title('Biblioteca Escolar')
    window.minsize(
        1024,
        768
    )
    if window.winfo_screenheight() >= 900:
        window.geometry(
            '1200x900'
        )
    else:
        window.geometry(
            '1024x768'
        )
    window.resizable(
        width=TRUE,
        height=TRUE
    )

    # Barra Topo
    menubar = Menu(window)
    window.config(menu=menubar)
    file_menu = Menu(
        menubar,
        tearoff=0,
    )
    edit_menu = Menu(
        menubar,
        tearoff=0,
    )
    menubar.add_cascade(
        label='File',
        menu=file_menu,
    )
    file_menu.add_command(
        label='Acrescentar Livro',
        command=lambda: addbookwindow.criar_janela()
    )
    file_menu.add_command(
        label='Remover Livro',
        command=lambda: removewindow.criar_janela()
    )
    file_menu.add_command(
        label='Sair',
        command=quit,
    )
    menubar.add_cascade(
        label='Edit',
        menu=edit_menu,
    )
    edit_menu.add_command(
        label='Copy',
        command=lambda: copy(window, entry_search)
    )
    edit_menu.add_command(
        label='Cut',
        command=lambda: cut(window, entry_search)
    )
    edit_menu.add_command(
        label='Paste',
        command=lambda: paste(window, entry_search)
    )

    # Frame Principal
    frame_principal = ttk.Frame(
        window,
        padding=5
    )
    frame_principal.pack(
        fill=BOTH,
        expand=TRUE
    )

    # Frame Logotipo
    frame_logotipo = ttk.Frame(
        frame_principal,
    )
    frame_logotipo.pack(
        side=TOP,
        expand=TRUE,
        fill=BOTH
    )

    # Label logótipo
    logotipo = PhotoImage(
        file='./imagens/logo4.png'
    )
    logotipo_label = ttk.Label(
        frame_logotipo,
        image=logotipo,
        anchor=CENTER
    )
    logotipo_label.pack(
        side=TOP,
        expand=TRUE,
        fill=X,
    )

    # Frame Lista Entregas Pendentes / Atrasadas
    frame_delivery = ttk.Frame(
        frame_principal,
    )
    frame_delivery.pack(
        fill=BOTH
    )
    for j in range(2):
        frame_delivery.grid_columnconfigure(
            j,
            weight=1
        )

    # Lista Entregas Pendentes
    label_pending = ttk.Label(
        frame_delivery,
        text='Entregas pendentes para hoje:'
    )
    label_pending.grid(
        row=0,
        column=0,
        sticky=N
    )
    list_pending = Listbox(
        frame_delivery
    )
    list_pending.grid(
        row=1,
        column=0,
        sticky=NSEW
    )

    # Lista Entregas Atrasadas
    label_behind = ttk.Label(
        frame_delivery,
        text='Entregas em atraso:'
    )
    label_behind.grid(
        row=0,
        column=1,
        sticky=N
    )
    list_behind = Listbox(
        frame_delivery
    )
    list_behind.grid(
        row=1,
        column=1,
        sticky=NSEW
    )

    # Frame de  Entrada de Procuras
    frame_search = ttk.Frame(
        frame_principal,
    )
    frame_search.pack(
        fill=BOTH
    )

    # Entrada de Procuras
    entry_search = ttk.Entry(
        frame_search,
    )
    button_search = ttk.Button(
        frame_search,
        text='Pesquisar Livro',
        command=lambda: procurar_livro(entry_search, list_search),
        padding=5
    )
    entry_search.pack(
        side=LEFT,
        anchor=NW,
        fill=X,
        expand=TRUE,
    )
    button_search.pack(
        side=LEFT,
        anchor=NE,
        expand=FALSE,
    )

    # Frame Lista de Procuras
    frame_search_list = ttk.Frame(
        frame_principal,
    )
    frame_search_list.pack(
        fill=BOTH
    )

    # Lista de Procuras
    columns = ('Titulo', 'ISBN', 'Autor', 'Editora', 'Publicação', 'Género', 'Requisitado')
    list_search = ttk.Treeview(
        frame_search_list,
        columns=columns,
        show='headings',
        selectmode='extended',
    )
    for i in columns:
        list_search.heading(i, text=i)
        list_search.column(i, width=10, anchor='center')
    list_search.pack(
        fill=X
    )

    # Frame Botões
    frame_buttons = ttk.Frame(
        frame_principal,
    )
    frame_buttons.pack(
        anchor=CENTER,
        side=BOTTOM,
        fill=X
    )
    for j in range(2):
        frame_buttons.grid_columnconfigure(
            j,
            weight=1
        )

    # Botões
    button_add = ttk.Button(
        frame_buttons,
        text='Adicionar Requisição',
        command=lambda: requisitar_livro(list_search)
    )
    button_deliver = ttk.Button(
        frame_buttons,
        text='Entregar Livro',
        command=lambda: entregar_livro(list_search)
    )
    button_add.grid(
        row=0,
        column=0
    )
    button_deliver.grid(
        row=0,
        column=1
    )
    window.mainloop()
