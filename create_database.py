import mysql.connector
from mysql.connector import errorcode
try:
    connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Th@run122"

)
    cursor=connection.cursor()
    cre_database="""
create database tharun"""
    cursor.execute(cre_database)
except mysql.connector.error as err:
    print("error:",err)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected():
        connection.close()
        print("database created successfully")