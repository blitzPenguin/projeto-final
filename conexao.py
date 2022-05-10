import mysql.connector


def connect():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Biblioteca_bd"
    )
    return con


def create_cursor(con):
    cursor = con.cursor()
    return cursor


def query(cursor, input_text):
    cursor.execute(input_text)


def fetch(cursor):
    return cursor.fetchall()


# Codigo para teste

# con = connect()
  
# create cursor object
# cursor = createCursor(con)
  
# assign data query
# query1 = "select * from GENEROS"
  
# executing cursor
# cursor.execute(query1)
  
# display all records
# table = cursor.fetchall()
  
# describe table
# print('\n Table Description:')
# for attr in table:
#   print(attr)
