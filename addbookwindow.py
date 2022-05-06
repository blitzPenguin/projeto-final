from tkinter import *
import conexao


class Addwindow:

    # Função construtora
    def __init__(self):

        # Criar janela toplevel
        addWindow = Toplevel()
        addWindow.title('Adicionar Livro')
        addWindow.geometry(
            '400x300'
        )
        addWindow.minsize(
            400,
            300
        )
        addWindow.maxsize(
            400,
            300
        )

        # Frame Principal
        framePrincipal = Frame(
            addWindow,
            background='blue',
            padx=5,
            pady=5
        )
        framePrincipal.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Frame Introdução de Título
        frameTitulo = Frame(
            framePrincipal,
            background='yellow'
        )
        frameTitulo.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Introdução de Título
        labelTitulo = Label(
            frameTitulo,
            text='Título: '
        )
        labelTitulo.pack(
            side=LEFT
        )
        entryTitulo = Entry(
            frameTitulo
        )
        entryTitulo.pack(
            side=RIGHT,
            expand=TRUE,
            fill=X
        )

        # Frame Introdução de Autor
        frameAutor = Frame(
            framePrincipal,
            background='orange'
        )
        frameAutor.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Introdução de Autor
        labelAutor = Label(
            frameAutor,
            text='Autor: '
        )
        labelAutor.pack(
            side=LEFT
        )
        entryAutor = Entry(
            frameAutor
        )
        entryAutor.pack(
            side=RIGHT,
            expand=TRUE,
            fill=X
        )

        # Frame Introdução de Editora
        frameEditor = Frame(
            framePrincipal,
            background='red'
        )
        frameEditor.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Introdução de Editora
        labelEditor = Label(
            frameEditor,
            text='Editora: '
        )
        labelEditor.pack(
            side=LEFT
        )
        entryEditor = Entry(
            frameEditor
        )
        entryEditor.pack(
            side=RIGHT,
            expand=TRUE,
            fill=X
        )

        # Frame Introdução de Publicação
        framePublication = Frame(
            framePrincipal,
            background='blue'
        )
        framePublication.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Introdução de Publicação
        labelPublication = Label(
            framePublication,
            text='Data Publicação: '
        )
        labelPublication.pack(
            side=LEFT
        )
        entryPublication = Entry(
            framePublication
        )
        entryPublication.pack(
            side=RIGHT,
            expand=TRUE,
            fill=X
        )

        # Frame Introdução de Genre
        frameGenre = Frame(
            framePrincipal,
            background='green'
        )
        frameGenre.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Introdução de Genre
        labelGenre = Label(
            frameGenre,
            text='Género: '
        )
        labelGenre.pack(
            side=LEFT
        )
        entryGenre = Entry(
            frameGenre
        )
        entryGenre.pack(
            side=RIGHT,
            expand=TRUE,
            fill=X
        )

        # Frame Botões
        frameButtons = Frame(
            framePrincipal,
            background='purple'
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

        # Botões Submeter Cancelar
        buttonAdd = Button(
            frameButtons,
            text='Adicionar Livro'
        )
        buttonCancel = Button(
            frameButtons,
            text='Cancelar',
            command=lambda: addWindow.destroy()
        )
        buttonAdd.grid(
            row=0,
            column=0
        )
        buttonCancel.grid(
            row=0,
            column=1
        )

        addWindow.mainloop()
