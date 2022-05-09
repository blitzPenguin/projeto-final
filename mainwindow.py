from tkinter import *
import addbookwindow
import removewindow
import conexao

# Metodos


def copy():
    pass


def cut():
    pass


def paste(window, entry_search):
    entry_search.insert(END, window.clipboard_get())


def procurar_livro(list_search):
    con = conexao.connect()
    cursor = conexao.create_cursor(con)
    query = conexao.query(cursor, 'SELECT * FROM LIVROS')
    list_search.delete(0, END)
    for i in query:
        list_search.insert(END, query)


def requisitar_livro():
    pass


def entregar_livro():
    pass


# Função construtora


def criar_janela():

    # Janela
    window = Tk()
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
        command=copy
    )
    edit_menu.add_command(
        label='Cut',
        command=cut
    )
    edit_menu.add_command(
        label='Paste',
        command=lambda: paste(window, entry_search)
    )

    # Frame Principal
    frame_principal = Frame(
        window,
        background='blue',
        padx=5,
        pady=5
    )
    frame_principal.pack(
        fill=BOTH,
        expand=TRUE
    )

    # Frame Logotipo
    frame_logotipo = Frame(
        frame_principal,
        background='light blue'
    )
    frame_logotipo.pack(
        side=TOP,
        expand=TRUE,
        fill=BOTH
    )

    # Label logótipo
    logotipo = PhotoImage(
        file='./imagens/arcor-logo-5.png'
    )
    logotipo_label = Label(
        frame_logotipo,
        image=logotipo,
        height=120
    )
    logotipo_label.pack(
        side=TOP,
        expand=TRUE,
        fill=BOTH,
        anchor=CENTER
    )

    # Frame Lista Entregas Pendentes / Atrasadas
    frame_delivery = Frame(
        frame_principal,
        background='yellow'
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
    label_pending = Label(
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
    label_behind = Label(
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
    frame_search = Frame(
        frame_principal,
        background='red'
    )
    frame_search.pack(
        fill=BOTH
    )

    # Entrada de Procuras
    entry_search = Entry(
        frame_search,
    )
    button_search = Button(
        frame_search,
        text='Pesquisar Livro',
        command=lambda: procurar_livro(list_search),
    )
    entry_search.pack(
        side=LEFT,
        anchor=NW,
        fill=X,
        expand=TRUE
    )
    button_search.pack(
        side=LEFT,
        anchor=NE,
        expand=FALSE
    )

    # Frame Lista de Procuras
    frame_search_list = Frame(
        frame_principal,
        background='orange'
    )
    frame_search_list.pack(
        fill=BOTH
    )

    # Lista de Procuras
    list_search = Listbox(
        frame_search_list
    )
    list_search.pack(
        fill=X
    )

    # Frame Botões
    frame_buttons = Frame(
        frame_principal,
        background='green'
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
    button_add = Button(
        frame_buttons,
        text='Adicionar Requisição',
        command=requisitar_livro
    )
    button_deliver = Button(
        frame_buttons,
        text='Entregar Livro',
        command=entregar_livro
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
