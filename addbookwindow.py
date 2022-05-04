from tkinter import *
import windowconstructor


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

        # Frame Introdução de Título
        frameTitulo = windowconstructor.createFrames(
            addWindow,
            color='yellow'
        )
        frameTitulo.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Introdução de Título
        labelTitulo = windowconstructor.createLabel(
            frameTitulo,
            text='Título: '
        )
        labelTitulo.pack(
            side=LEFT
        )
        entryTitulo = windowconstructor.createEntry(
            frameTitulo
        )
        entryTitulo.pack(
            side=RIGHT,
            expand=TRUE,
            fill=X
        )

        # Frame Introdução de Autor
        frameAutor = windowconstructor.createFrames(
            addWindow,
            color='orange'
        )
        frameAutor.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Introdução de Autor
        labelAutor = windowconstructor.createLabel(
            frameAutor,
            text='Autor: '
        )
        labelAutor.pack(
            side=LEFT
        )
        entryAutor = windowconstructor.createEntry(
            frameAutor
        )
        entryAutor.pack(
            side=RIGHT,
            expand=TRUE,
            fill=X
        )

        # Frame Introdução de Editora
        frameEditor = windowconstructor.createFrames(
            addWindow,
            color='red'
        )
        frameEditor.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Introdução de Editora
        labelEditor = windowconstructor.createLabel(
            frameEditor,
            text='Editora: '
        )
        labelEditor.pack(
            side=LEFT
        )
        entryEditor = windowconstructor.createEntry(
            frameEditor
        )
        entryEditor.pack(
            side=RIGHT,
            expand=TRUE,
            fill=X
        )

        # Frame Introdução de Publicação
        framePublication = windowconstructor.createFrames(
            addWindow,
            color='blue'
        )
        framePublication.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Introdução de Publicação
        labelPublication = windowconstructor.createLabel(
            framePublication,
            text='Data Publicação: '
        )
        labelPublication.pack(
            side=LEFT
        )
        entryPublication = windowconstructor.createEntry(
            framePublication
        )
        entryPublication.pack(
            side=RIGHT,
            expand=TRUE,
            fill=X
        )

        # Frame Introdução de Genre
        frameGenre = windowconstructor.createFrames(
            addWindow,
            color='green'
        )
        frameGenre.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Introdução de Genre
        labelGenre = windowconstructor.createLabel(
            frameGenre,
            text='Género: '
        )
        labelGenre.pack(
            side=LEFT
        )
        entryGenre = windowconstructor.createEntry(
            frameGenre
        )
        entryGenre.pack(
            side=RIGHT,
            expand=TRUE,
            fill=X
        )

        # Frame Botões
        frameButtons = windowconstructor.createFrames(
            addWindow,
            color='purple'
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
        buttonAdd = windowconstructor.createButton(
            frameButtons,
            text='Adicionar Livro'
        )
        buttonCancel = windowconstructor.createButton(
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
