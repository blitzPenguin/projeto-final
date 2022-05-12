from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import conexao


# Função Submissão Requisição
def adicionar_requisicao(
        dialog_window,
        id_livro,
        entry_id_aluno,
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
        dialog_window.destroy()
    else:
        if messagebox.askyesno(title='Confirmação', message='Deseja criar a requisição?'):
            con.commit()
            query_statement = '''SELECT MAX(id) FROM REQUISICOES_HEADER'''
            conexao.query(cursor, query_statement)
            id_requisicao = cursor.fetchone()
            try:
                for i in id_livro:
                    query_statement = '''INSERT INTO REQUISICOES_DESC (id_requisicao, id_livro)
                        VALUES (\''''+str(id_requisicao[0])+'\', \''+str(i)+'\')'
                    conexao.query(cursor, query_statement)
                    query_statement = '''UPDATE LIVROS
                        SET requisitado = 1
                        WHERE id = \''''+str(i)+'\''
                    conexao.query(cursor, query_statement)
            except Exception:
                messagebox.showerror(title='Erro', message='Não foi possível criar a requisição')
                con.close()
            else:
                messagebox.showinfo(title='Sucesso', message='Criou a requisição com sucesso')
                con.commit()
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
    frame_principal = ttk.Frame(
        dialog_window,
        padding=5
    )
    frame_principal.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Frame Titulo
    frame_titulo = ttk.Frame(
        frame_principal
    )
    frame_titulo.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Display Título
    label_titulo = ttk.Label(
        frame_titulo,
        text='Título: '
    )
    label_titulo.pack(
        side=LEFT
    )
    display_titulo = ttk.Label(
        frame_titulo,
        text=titulo_livro
    )
    display_titulo.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Indtrodução ID aluno
    frame_id_aluno = ttk.Frame(
        frame_principal
    )
    frame_id_aluno.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Introdução ID aluno
    lable_id_aluno = ttk.Label(
        frame_id_aluno,
        text='ID Aluno: '
    )
    lable_id_aluno.pack(
        side=LEFT
    )
    entry_id_aluno = ttk.Entry(
        frame_id_aluno
    )
    entry_id_aluno.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Data Requisição
    frame_data_requisicao = ttk.Frame(
        frame_principal
    )
    frame_data_requisicao.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Display Data Requisição
    label_data_requisicao = ttk.Label(
        frame_data_requisicao,
        text='Data Requisição: '
    )
    label_data_requisicao.pack(
        side=LEFT
    )
    current_time = time.strftime("%d %b %Y", time.localtime())
    display_data_requisicao = ttk.Label(
        frame_data_requisicao,
        text=current_time
    )
    display_data_requisicao.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Data Limite
    frame_data_limite = ttk.Frame(
        frame_principal
    )
    frame_data_limite.pack(
        expand=TRUE,
        fill=BOTH
    )

    # Display Data Limite
    label_data_limite = ttk.Label(
        frame_data_limite,
        text='Data de Entrega: '
    )
    label_data_limite.pack(
        side=LEFT
    )
    limit_time = time.strftime("%d %b %Y", time.strptime(time.ctime(time.time() + 604800)))
    display_data_limite = ttk.Label(
        frame_data_limite,
        text=limit_time
    )
    display_data_limite.pack(
        side=RIGHT,
        expand=TRUE,
        fill=X
    )

    # Frame Botões
    frame_botoes = ttk.Frame(
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
    botao_add = ttk.Button(
        frame_botoes,
        text='Adicionar Livro',
        command=lambda: adicionar_requisicao(
            dialog_window,
            id_livro,
            entry_id_aluno,
        )
    )
    botao_cancel = ttk.Button(
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
