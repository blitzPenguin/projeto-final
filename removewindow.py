from tkinter import *
import windowconstructor


class RemoveWindow:

    # Função Construtora
    def __init__(self):

        # Criar janela toplevel
        removeWindow = Toplevel()
        removeWindow.geometry(
            '400x300'
        )
        removeWindow.minsize(
            400,
            300
        )
        removeWindow.maxsize(
            400,
            300
        )

        # Frame de  Entrada de Procuras
        frameSearch = windowconstructor.createFrames(
            removeWindow,
            color='red'
        )
        frameSearch.pack(
            fill=BOTH
        )

        # Entrada de Procuras
        entrySearch = windowconstructor.createEntry(
            frameSearch
        )
        buttonSearch = windowconstructor.createButton(
            frameSearch,
            text='Pesquisar Livro'
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
        frameSearchList = windowconstructor.createFrames(
            removeWindow,
            color='orange'
        )
        frameSearchList.pack(
            fill=BOTH
        )

        # Lista de Procuras
        listSearch = windowconstructor.createList(
            frameSearchList
        )
        listSearch.pack(
            fill=X
        )

        # Frame Botões
        frameButtons = windowconstructor.createFrames(
            removeWindow,
            color='green'
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
        buttonRemove = windowconstructor.createButton(
            frameButtons,
            text='Remover Livro'
        )
        buttonRemove.grid(
            row=0,
            column=0
        )
        buttonCancel = windowconstructor.createButton(
            frameButtons,
            text='Cancelar',
            command=lambda: removeWindow.destroy()
        )
        buttonCancel.grid(
            row=0,
            column=1
        )
        removeWindow.mainloop()
