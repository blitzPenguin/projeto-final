from tkinter import *
from tkinter import messagebox
import time
import conexao


# Função Submissão Requisição
def adicionar_requisicao(
        dialog_window,
        id_livro,
        entry_id_aluno,
        display_data_requisicao,
        display_data_limite
):
    con = conexao.connect()
    cursor = conexao.create_cursor(con)
    try:
        id_aluno = entry_id_aluno.get()
        query_statement = '''INSERT INTO REQUISICOES_HEADER (id_aluno, data_limite)
            VALUES (\''''+id_aluno+'\', DATE_ADD(CURRENT_TIMESTAMP,INTERVAL 7 DAY))'''
        conexao.query(cursor, query_statement)
    except Exception:
        messagebox.showerror(title='Erro', message='Não foi possível criar a requisição')
        con.close()
    else:
        if messagebox.askyesno(title='Confirmação', message='Deseja criar a requisição?'):
            con.commit()
            messagebox.showinfo(title='Sucesso', message='Criou a requisição com sucesso')
            con.close()
            dialog_window.destroy()



# Função criadora de janela


def criar_dialog(id_livro, titulo_livro):
    dialog_window = Toplevel()
    dialog_window.title(
        'Janela Requisição'
    )
    dialog_window.geometry(
        '400x300'
    )
    dialog_window.minsize(
        400,
        300
    )
    dialog_window.maxsize(
        400,
        300
    )

    # Frame Principal
    frame_principal = Frame(
        dialog_window,
        padx=5,
        pady=5
    )
    frame_principal.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Frame Titulo
    frame_titulo = Frame(
        frame_principal
    )
    frame_titulo.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Display Título
    label_titulo = Label(
        frame_titulo,
        text='Título: '
    )
    label_titulo.pack(
        side=LEFT
    )
    display_titulo = Label(
        frame_titulo,
        text=titulo_livro
    )
    display_titulo.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Indtrodução ID aluno
    frame_id_aluno = Frame(
        frame_principal
    )
    frame_id_aluno.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Introdução ID aluno
    lable_id_aluno = Label(
        frame_id_aluno,
        text='ID Aluno: '
    )
    lable_id_aluno.pack(
        side=LEFT
    )
    entry_id_aluno = Entry(
        frame_id_aluno
    )
    entry_id_aluno.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Data Requisição
    frame_data_requisicao = Frame(
        frame_principal
    )
    frame_data_requisicao.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Display Data Requisição
    label_data_requisicao = Label(
        frame_data_requisicao,
        text='Data Requisição: '
    )
    label_data_requisicao.pack(
        side=LEFT
    )
    current_time = time.ctime(time.time())
    display_data_requisicao = Label(
        frame_data_requisicao,
        text=current_time
    )
    display_data_requisicao.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Data Limite
    frame_data_limite = Frame(
        frame_principal
    )
    frame_data_limite.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Display Data Limite
    label_data_limite = Label(
        frame_data_limite,
        text='Data de Entrega: '
    )
    label_data_limite.pack(
        side=LEFT
    )
    limit_time = time.ctime(time.time() + 604800)
    display_data_limite = Label(
        frame_data_limite,
        text=limit_time
    )
    display_data_limite.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Botões
    frame_botoes = Frame(
        frame_principal,
    )
    frame_botoes.pack(
        anchor=CENTER,
        side=BOTTOM,
        fill=X
    )
    for j in range(2):
        frame_botoes.grid_columnconfigure(
            j,
            weight=1
        )

    # Botões Submeter Cancelar
    botao_add = Button(
        frame_botoes,
        text='Adicionar Livro',
        command=lambda: adicionar_requisicao(
            dialog_window,
            id_livro,
            entry_id_aluno,
            display_data_requisicao,
            display_data_limite,
        )
    )
    botao_cancel = Button(
        frame_botoes,
        text='Cancelar',
        command=lambda: dialog_window.destroy()
    )
    botao_add.grid(
        row=0,
        column=0
    )
    botao_cancel.grid(
        row=0,
        column=1
    )

    dialog_window.mainloop()
