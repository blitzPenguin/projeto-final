# Projeto final

Por João Oliveira

## Introdução

Projeto final para curso EFA PRO de Programador Informático.

Trata-se de um software de gestão de uma biblioteca escolar com gestão dos livros da mesma e as requisições efetuadas pelos alunos.

## Tecnologias

Este projeto foi criado em `Python` com recurso ao `tkinter` para a construção de interface gráfica.
Utilizei o `PHPMyAdmin` para a construção da base de dados referente ao programa.

## Utilização

A aplicação seria utilizada pela funcionária de uma dada escola para colmatar as possíveis terefas diárias da biblioteca.

- Requisições de livros
- Devolução de livros
- Visualização da disponibilidade de qualquer livro
- Adição de livros à base de dados
- Desativação de entradas de livros na base de dados, caso o livro se torne indisponível

## Screenshots

### Programa

![ScreenShot](src/imagens/screenshot1.png)

### Base de dados

![ScreenShot](src/imagens/screenshot2.png)

## Requisitos

Para o funcionamento do programa é necessário previamente criar a base de dados derivada do ficheiro .sql na pasta `/src/SQL` através do `PHPMyAdmin` em localhost.

## Execução

Este projeto contém dois executáveis, para `Windows` e `Linux`.

Estes executáveis foram criados com uso do módulo `PyInstaller`.