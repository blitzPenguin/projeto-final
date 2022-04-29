from tkinter import *
import windowConstructor
import functions


class Mainwindow:

    # Função construtora
    def __init__(self):
        # Window
        window = Tk()
        window.minsize(800, 600)
        if window.winfo_screenmmheight() >= 768:
            window.geometry('1024x768')
        else:
            window.geometry('800x600')
        window.resizable(width=TRUE, height=TRUE)

        # Barra Topo
        windowConstructor.createBar(window)
        # Frame Principal
        framePrincipal = windowConstructor.createFrames(
            window,
            color='blue',
        )

        # Label logótipo
        logotipo = PhotoImage(file='./imagens/arcor-logo-5.png')
        logotipoLabel = Label(
            framePrincipal,
            image=logotipo,
            height=120,
        )
        logotipoLabel.pack(
            side=TOP,
            expand=TRUE,
            fill=BOTH,
            anchor=CENTER,
        )

        # Frames secundárias
        frameButtons = windowConstructor.createFrames(
            framePrincipal,
            color='green',
        )
        frameList = windowConstructor.createFrames(
            framePrincipal,
            color='yellow',
        )
        frameSearch = windowConstructor.createFrames(
            framePrincipal,
            color='red',
        )
        frameSearchList = windowConstructor.createFrames(
            framePrincipal,
            color='orange'
        )
        framePrincipal.pack(
            fill=BOTH,
            expand=TRUE,
        )
        frameList.pack(
            fill=BOTH,
        )
        frameSearch.pack(
            fill=BOTH,
        )
        frameSearchList.pack(
            fill=BOTH
        )
        frameButtons.pack(
            anchor=CENTER,
            side=BOTTOM,
            fill=X,
        )
        for j in range(2):
            frameButtons.grid_columnconfigure(j, weight=1)

        # Lista Requisiões
        labelDelivery = windowConstructor.createLabel(
            frameList,
            text='Entregas pendentes para hoje:'
        )
        labelDelivery.pack(
            anchor=N,
        )
        listDelivery = windowConstructor.createList(frameList)
        listDelivery.pack(
            anchor=CENTER,
            expand=True,
            fill=BOTH,
        )

        # Entrada de procuras
        entrySearch = windowConstructor.createEntry(
            frameSearch,
        )
        buttonSearch = windowConstructor.createButton(
            frameSearch,
            text='Pesquisar Livro',
        )
        entrySearch.pack(
            side=LEFT,
            anchor=NW,
            fill=X,
            expand=TRUE,
        )
        buttonSearch.pack(
            side=LEFT,
            anchor=NE,
            expand=FALSE,
        )

        # Entrada de lista de procuras
        listSearch = windowConstructor.createList(
            frameSearchList,
        )
        listSearch.pack(
            fill=X,
        )

        # Butões
        buttonAdd = windowConstructor.createButton(
            frameButtons,
            text='Adicionar Requisição',
        )
        buttonDeliver = windowConstructor.createButton(
            frameButtons,
            text='Entregar Livro',
        )
        buttonAdd.grid(
            row=0,
            column=0,
        )
        buttonDeliver.grid(
            row=0,
            column=1,
        )

        window.mainloop()
