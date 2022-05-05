from tkinter import *
import mainwindow


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
    if 'command' in kwargs:
        button.config(
            command=kwargs['command']
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
