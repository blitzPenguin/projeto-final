from tkinter import *
import windowconstructor
import addbookwindow
import removewindow


class Mainwindow:

    # Funções
    def acrescentarLivro():
        addbookwindow.Addwindow()

    def removerLivro():
        removewindow.RemoveWindow()

    def copy():
        pass

    def cut():
        pass

    def paste():
        pass

    # Função construtora

    def __init__(self):

        # Window
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
        windowconstructor.createBar(
            window
        )

        # Frame Principal
        framePrincipal = windowconstructor.createFrames(
            window,
            color='blue'
        )
        framePrincipal.pack(
            fill=BOTH,
            expand=TRUE
        )

        # Frame Logotipo
        frameLogotipo = windowconstructor.createFrames(
            framePrincipal,
            color='light blue'
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
        frameDelivery = windowconstructor.createFrames(
            framePrincipal,
            color='yellow'
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
        labelPending = windowconstructor.createLabel(
            frameDelivery,
            text='Entregas pendentes para hoje:'
        )
        labelPending.grid(
            row=0,
            column=0,
            sticky=N
        )
        listPending = windowconstructor.createList(
            frameDelivery
        )
        listPending.grid(
            row=1,
            column=0,
            sticky=NSEW
        )

        # Lista Entregas Atrasadas
        labelBehind = windowconstructor.createLabel(
            frameDelivery,
            text='Entregas em atraso:'
        )
        labelBehind.grid(
            row=0,
            column=1,
            sticky=N
        )
        listBehind = windowconstructor.createList(
            frameDelivery
        )
        listBehind.grid(
            row=1,
            column=1,
            sticky=NSEW
        )

        # Frame de  Entrada de Procuras
        frameSearch = windowconstructor.createFrames(
            framePrincipal,
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
            framePrincipal,
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
            framePrincipal,
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
        buttonAdd = windowconstructor.createButton(
            frameButtons,
            text='Adicionar Requisição'
        )
        buttonDeliver = windowconstructor.createButton(
            frameButtons,
            text='Entregar Livro'
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
