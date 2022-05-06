from tkinter import *
import conexao


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

        # Frame Principal
        framePrincipal = Frame(
            removeWindow,
            background='blue',
            padx=5,
            pady=5
        )
        framePrincipal.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Frame de  Entrada de Procuras
        frameSearch = Frame(
            framePrincipal,
            background='red'
        )
        frameSearch.pack(
            expand=TRUE,
            fill=BOTH
        )

        # Entrada de Procuras
        entrySearch = Entry(
            frameSearch
        )
        buttonSearch = Button(
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
        frameSearchList = Frame(
            framePrincipal,
            background='orange'
        )
        frameSearchList.pack(
            expand=TRUE,
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
            fill=X,
            expand=TRUE
        )
        for j in range(2):
            frameButtons.grid_columnconfigure(
                j,
                weight=1
            )

        # Botões
        buttonRemove = Button(
            frameButtons,
            text='Remover Livro'
        )
        buttonRemove.grid(
            row=0,
            column=0
        )
        buttonCancel = Button(
            frameButtons,
            text='Cancelar',
            command=lambda: removeWindow.destroy()
        )
        buttonCancel.grid(
            row=0,
            column=1
        )
        removeWindow.mainloop()
