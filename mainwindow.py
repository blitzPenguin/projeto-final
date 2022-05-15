# mainwindow.py #
# Função referente à criação da janela principal #


from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk
import addbookwindow
import funcoes
import removewindow


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
        label='Copiar',
        command=lambda: funcoes.copiar(window, entry_search)
    )
    edit_menu.add_command(
        label='Cortar',
        command=lambda: funcoes.cortar(window, entry_search)
    )
    edit_menu.add_command(
        label='Colar',
        command=lambda: funcoes.colar(window, entry_search)
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
        text='Entregas pendentes:'
    )
    label_pending.grid(
        row=0,
        column=0,
        sticky=N
    )
    columns = ('Aluno', 'Titulo', 'Data Requisicao', 'Data Limite')
    list_pending = ttk.Treeview(
        frame_delivery,
        columns=columns,
        show='headings',
        selectmode=EXTENDED
    )
    for i in columns:
        list_pending.heading(i, text=i)
        list_pending.column(i, width=10, anchor=CENTER)
    list_pending.grid(
        row=1,
        column=0,
        sticky=NSEW
    )
    funcoes.requisicoes_pendentes(list_pending)

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
    list_behind = ttk.Treeview(
        frame_delivery,
        columns=columns,
        show='headings',
        selectmode=EXTENDED
    )
    for i in columns:
        list_behind.heading(i, text=i)
        list_behind.column(i, width=10, anchor=CENTER)
    list_behind.grid(
        row=1,
        column=1,
        sticky=NSEW
    )
    funcoes.requisicoes_atrasadas(list_behind)

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
        command=lambda: funcoes.procurar_livro(entry_search, list_search),
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
    columns = ('Titulo', 'Autor', 'Editora', 'Publicação', 'Género', 'ISBN', 'Requisitado')
    list_search = ttk.Treeview(
        frame_search_list,
        columns=columns,
        show='headings',
        selectmode=EXTENDED,
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
        command=lambda: funcoes.requisitar_livro_dialog(list_search, list_pending)
    )
    button_deliver = ttk.Button(
        frame_buttons,
        text='Entregar Livro',
        command=lambda: funcoes.entregar_livro(list_pending, list_behind)
    )
    button_add.grid(
        row=0,
        column=0,
        pady=7
    )
    button_deliver.grid(
        row=0,
        column=1,
        pady=7
    )
    window.mainloop()
