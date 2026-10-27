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
    inse_data="""
insert into family(name,relation)
values(%s,%s)"""
    data=[("tharun","son"),
      ("mani","son")
]
    cursor.execute(inse_data,data)
#except mysql.connection.error as err:
 #   print("error:",err)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected:
        connection.close()
        print("data inserted successfully")