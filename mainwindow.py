from tkinter import *
import addbookwindow
import removewindow
import conexao

#Metodos
def copy():
    pass

def cut():
    pass

def paste(entrySearch):
    entrySearch.clipboard_append()

def procurar(listSearch):
    con = conexao.connect()
    cursor = conexao.createCursor(con)
    query = conexao.query(cursor, 'SELECT * FROM LIVROS')
    listSearch.delete(0, END)
    for i in query:
        listSearch.insert(END,query)


def requisitarLivro():
    pass

def entregarLivro():
    pass

# Função construtora
def createWindow():

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
    fileMenu = Menu(
        menubar,
        tearoff=0,
    )
    editMenu = Menu(
        menubar,
        tearoff=0,
    )
    menubar.add_cascade(
        label='File',
        menu=fileMenu,
    )
    fileMenu.add_command(
        label='Acrescentar Livro',
        command=lambda: addbookwindow.Addwindow()
    )
    fileMenu.add_command(
        label='Remover Livro',
        command=lambda: removewindow.RemoveWindow()
    )
    fileMenu.add_command(
        label='Sair',
        command=quit,
    )
    menubar.add_cascade(
        label='Edit',
        menu=editMenu,
    )
    editMenu.add_command(
        label='Copy',
        command=copy
    )
    editMenu.add_command(
        label='Cut',
        command=cut
    )
    editMenu.add_command(
        label='Paste',
        command=lambda: paste(entrySearch)
    )

    # Frame Principal
    framePrincipal = Frame(
        window,
        background='blue',
        padx=5,
        pady=5
    )
    framePrincipal.pack(
        fill=BOTH,
        expand=TRUE
    )

    # Frame Logotipo
    frameLogotipo = Frame(
        framePrincipal,
        background='light blue'
    )
    frameLogotipo.pack(
        side=TOP,
        expand=TRUE,
        fill=BOTH
    )

    # Label logótipo
    logotipo = PhotoImage(
        file='./imagens/arcor-logo-5.png'
    )
    logotipoLabel = Label(
        frameLogotipo,
        image=logotipo,
        height=120
    )
    logotipoLabel.pack(
        side=TOP,
        expand=TRUE,
        fill=BOTH,
        anchor=CENTER
    )

    # Frame Lista Entregas Pendentes / Atrasadas
    frameDelivery = Frame(
        framePrincipal,
        background='yellow'
    )
    frameDelivery.pack(
        fill=BOTH
    )
    for j in range(2):
        frameDelivery.grid_columnconfigure(
            j,
            weight=1
        )

    # Lista Entregas Pendentes
    labelPending = Label(
        frameDelivery,
        text='Entregas pendentes para hoje:'
    )
    labelPending.grid(
        row=0,
        column=0,
        sticky=N
    )
    listPending = Listbox(
        frameDelivery
    )
    listPending.grid(
        row=1,
        column=0,
        sticky=NSEW
    )

    # Lista Entregas Atrasadas
    labelBehind = Label(
        frameDelivery,
        text='Entregas em atraso:'
    )
    labelBehind.grid(
        row=0,
        column=1,
        sticky=N
    )
    listBehind = Listbox(
        frameDelivery
    )
    listBehind.grid(
        row=1,
        column=1,
        sticky=NSEW
    )

    # Frame de  Entrada de Procuras
    frameSearch = Frame(
        framePrincipal,
        background='red'
    )
    frameSearch.pack(
        fill=BOTH
    )

    # Entrada de Procuras
    entrySearch = Entry(
        frameSearch,
    )
    buttonSearch = Button(
        frameSearch,
        text='Pesquisar Livro',
        command=lambda: procurar(listSearch),
    )
    entrySearch.pack(
        side=LEFT,
        anchor=NW,
        fill=X,
        expand=TRUE
    )
    buttonSearch.pack(
        side=LEFT,
        anchor=NE,
        expand=FALSE
    )

    # Frame Lista de Procuras
    frameSearchList = Frame(
        framePrincipal,
        background='orange'
    )
    frameSearchList.pack(
        fill=BOTH
    )

    # Lista de Procuras
    listSearch = Listbox(
        frameSearchList
    )
    listSearch.pack(
        fill=X
    )

    # Frame Botões
    frameButtons = Frame(
        framePrincipal,
        background='green'
    )
    frameButtons.pack(
        anchor=CENTER,
        side=BOTTOM,
        fill=X
    )
    for j in range(2):
        frameButtons.grid_columnconfigure(
            j,
            weight=1
        )

    # Botões
    buttonAdd = Button(
        frameButtons,
        text='Adicionar Requisição',
        command=requisitarLivro
    )
    buttonDeliver = Button(
        frameButtons,
        text='Entregar Livro',
        command=entregarLivro
    )
    buttonAdd.grid(
        row=0,
        column=0
    )
    buttonDeliver.grid(
        row=0,
        column=1
    )
    window.mainloop()
