import mysql.connector
from mysql.connector import errorcode
try:
    connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Th@run122",
    database="tharun"

)
    cursor=connection.cursor()
    cre_table="""
create table family(
name varchar(50),
relation varchar(50))"""
    cursor.execute(cre_table)
except mysql.connection.error as err:
    print("error:",err)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected:
        connection.close()
        print("table created successfully")