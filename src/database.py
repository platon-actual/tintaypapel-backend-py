import mysql.connector

#database = mysql.connector.connect(
#    host='localhost',
#    user='root',
#    password='1234',
#    database='typ_bd'
#)
def db_connect():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='typ_bd'
    )