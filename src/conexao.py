'''
conexao.py
funções referentes à ligação à base de dados e queries efetuadas'''

import mysql.connector


def connect():
    '''conexão à base de dados'''
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Biblioteca_bd"
    )


def cursor(
        con
):
    return con.cursor()


# Execucao querys #


def query_req_pendentes(
        cursor
):
    cursor.execute(
        '''
        SELECT ALUNOS.nome, TURMAS.designacao, LIVROS.titulo, REQUISICOES_HEADER.data_limite, LIVROS.id
        FROM ALUNOS
        INNER JOIN TURMAS
        ON TURMAS.id = ALUNOS.id_turma
        INNER JOIN REQUISICOES_HEADER
        ON REQUISICOES_HEADER.id_aluno = ALUNOS.id
        INNER JOIN REQUISICOES_DESC
        ON REQUISICOES_DESC.id_requisicao = REQUISICOES_HEADER.id
        INNER JOIN LIVROS
        ON LIVROS.id = REQUISICOES_DESC.id_livro
        WHERE REQUISICOES_HEADER.data_limite >= DATE(NOW())
        AND
        REQUISICOES_DESC.devolvido = 0
        '''
    )


def query_req_atrasadas(
        cursor
):
    cursor.execute(
        '''
        SELECT ALUNOS.nome, TURMAS.designacao, LIVROS.titulo, REQUISICOES_HEADER.data_limite, LIVROS.id
        FROM ALUNOS
        INNER JOIN TURMAS
        ON TURMAS.id = ALUNOS.id_turma
        INNER JOIN REQUISICOES_HEADER
        ON REQUISICOES_HEADER.id_aluno = ALUNOS.id
        INNER JOIN REQUISICOES_DESC
        ON REQUISICOES_DESC.id_requisicao = REQUISICOES_HEADER.id
        INNER JOIN LIVROS
        ON LIVROS.id = REQUISICOES_DESC.id_livro
        WHERE REQUISICOES_HEADER.data_limite < DATE(NOW())
        AND
        REQUISICOES_DESC.devolvido = 0
        '''
    )


def query_pesquisa(
        cursor,
        lista_pesquisa
):
    cursor.execute(
        '''
        SELECT LIVROS.titulo, LIVROS.autor, LIVROS.editora, LIVROS.data_publicacao, GENEROS.designacao, LIVROS.isbn, REQUISITADO.designacao, LIVROS.id
        FROM LIVROS
        INNER JOIN LIVROS_GENEROS
        ON LIVROS_GENEROS.id_livro = LIVROS.id
        INNER JOIN GENEROS
        ON GENEROS.id = LIVROS_GENEROS.id_genero
        INNER JOIN REQUISITADO
        ON REQUISITADO.id = LIVROS.id_requisitado
        WHERE
        LIVROS.ativo = 1
        AND
        (LIVROS.titulo LIKE \'%'''+lista_pesquisa+'''%\'
        OR LIVROS.autor LIKE \'%'''+lista_pesquisa+'''%\'
        OR LIVROS.editora LIKE \'%'''+lista_pesquisa+'''%\'
        OR LIVROS.data_publicacao LIKE \'%'''+lista_pesquisa+'''%\'
        OR GENEROS.designacao LIKE \'%'''+lista_pesquisa+'''%\'
        OR LIVROS.isbn LIKE \''''+lista_pesquisa+'''%\')
        ORDER BY LIVROS.titulo ASC
        '''
    )


def query_comparar_livro(
    cursor,
    titulo,
    autor,
    editora,
    publicacao
):
    cursor.execute(
        '''
        SELECT LIVROS.id FROM LIVROS
        WHERE
        titulo LIKE \''''+titulo.get()+'''\'
        AND
        autor LIKE \''''+autor.get()+'''\'
        AND
        editora LIKE \''''+editora.get()+'''\'
        AND
        data_publicacao LIKE \''''+publicacao.get()+'''\'
        '''
    )



def query_adicionar_livro(
        cursor,
        titulo,
        autor,
        editora,
        publicacao,
        isbn,
):
    cursor.execute(
        '''
        INSERT INTO LIVROS (titulo, autor, editora, data_publicacao, isbn)
        VALUES (\''''+titulo.get()+'\', \''+autor.get()+'\', \''+editora.get()+'''\', \'
        '''+publicacao.get()+'\', \''+isbn.get()+'''\')
        '''
    )


def query_ativar_livro(
    cursor,
    livro,
    isbn
):
    print(livro[0])
    cursor.execute(
        '''
        UPDATE LIVROS
        SET LIVROS.ativo = 1
        WHERE LIVROS.id = \''''+str(livro[0])+'''\'
        '''
    )



def query_listar_generos(
        cursor,
):
    cursor.execute(
        '''
        SELECT GENEROS.designacao from GENEROS
        '''
    )


def query_listar_alunos(
    cursor
):
    '''query para resgatar os dados relativos à lista de alunos'''
    cursor.execute(
        '''
        SELECT ALUNOS.id, ALUNOS.nome, TURMAS.designacao FROM ALUNOS
        INNER JOIN TURMAS
        ON TURMAS.id = ALUNOS.id_turma
        '''
    )


def query_adicionar_genero(
        cursor,
        genero
):
    cursor.execute(
        '''
        SELECT GENEROS.id FROM GENEROS
        WHERE GENEROS.designacao like \'''' + genero + '''\'
        '''
    )
    id_genero = cursor.fetchone()
    print("id genero: ", id_genero)
    if id_genero == None:
        cursor.execute(
            '''
            INSERT INTO GENEROS (designacao)
            VALUES (\'''' + genero + '''\')
            '''
        )
        cursor.execute(
            '''
            SELECT MAX(id) FROM GENEROS
            '''
        )
        id_genero = cursor.fetchone()
        cursor.execute(
            '''
            SELECT MAX(id) FROM LIVROS
            '''
        )
        livro = cursor.fetchone()
        print("livro: ", livro)
        cursor.execute(
            '''
            INSERT INTO LIVROS_GENEROS (id_livro, id_genero)
            VALUES (\''''+str(livro[0])+'\', \''+str(id_genero[0])+'''\')
            '''
        )
    else:
        cursor.execute(
            '''
            SELECT MAX(id) FROM LIVROS
            '''
        )
        livro = cursor.fetchone()
        cursor.execute(
            '''
            INSERT INTO LIVROS_GENEROS (id_livro, id_genero)
            VALUES (\''''+str(livro[0])+'\', \''+str(id_genero[0])+'''\')
            '''
        )


def query_remover_livro(
        cursor,
        livro
):
    cursor.execute(
        '''
        UPDATE LIVROS
        SET LIVROS.ativo = 0
        WHERE LIVROS.id = \''''+str(livro)+'''\'
        '''
    )


def query_requisicao_cabecalho(
        cursor,
        aluno
):
    cursor.execute(
        '''
        INSERT INTO REQUISICOES_HEADER (id_aluno, data_limite)
        VALUES (\''''+str(aluno)+'''\', DATE_ADD(CURRENT_TIMESTAMP,INTERVAL 7 DAY))
        '''
    )


def query_requisicao_descricao(
        cursor,
        livro
):
    cursor.execute(
        '''
        SELECT MAX(id) FROM REQUISICOES_HEADER
        '''
    )
    requisicao = cursor.fetchone()
    cursor.execute(
        '''
        INSERT INTO REQUISICOES_DESC (id_requisicao, id_livro)
        VALUES (\''''+str(requisicao[0])+'\', \''+str(livro)+'''\')
        '''
    )
    cursor.execute(
        '''
        UPDATE LIVROS
        SET id_requisitado = 2
        WHERE id = \''''+str(livro)+'''\'
        '''
    )


def query_entregar_livro(
        cursor,
        livro
):
    cursor.execute(
        '''
        UPDATE REQUISICOES_DESC, LIVROS
        SET REQUISICOES_DESC.devolvido = 1,
        LIVROS.id_requisitado = 1
        WHERE REQUISICOES_DESC.id_livro = \''''+str(livro)+'''\'
        AND
        LIVROS.id = \''''+str(livro)+'''\'
        '''
    )
