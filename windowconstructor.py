from tkinter import *
import functions

# Criação de barra de topo
def createBar(master):
    menubar = Menu(master)
    master.config(menu=menubar)
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
        command=lambda: functions.acrescentarLivro(),
    )
    fileMenu.add_command(
        label='Remover Livro',
        command=functions.removerLivro,
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
        command=functions.copy,
    )
    editMenu.add_command(
        label='Cut',
        command=functions.cut,
    )
    editMenu.add_command(
        label='Paste',
        command=functions.paste,
    )

# Criação de frames
def createFrames(master, **kwargs):
    frame = Frame(
        master,
        padx=5,
        pady=5,
    )
    if 'color' in kwargs:
        frame.config(background=kwargs['color'])
    if 'width' in kwargs:
        frame.config(width=kwargs['width'])
    return frame

# Criar Butões
def createButton(master, **kwargs):
    button = Button(
        master,
    )
    if 'text' in kwargs:
        button.config(text=kwargs['text'])
    if 'image' in kwargs:
        button.config(
            text=kwargs['image'],
            compound=TOP,
        )
    return button

# Criação de labels
def createLabel(master, **kwargs):
    label = Label(
        master,
    )
    if 'text' in kwargs:
        label.config(text=kwargs['text'])
    if 'image' in kwargs:
        label.config(image=kwargs['image'])
    return label

# Criar Caixa de Texto
def createEntry(master, **kwargs):
    entry = Entry(
        master,
        width=10,
    )
    return entry

# Criar Lista
def createList(master):
    list = Listbox(
        master,
    )
    return list