import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Th@run122",
    database="tharun"
)
cursor=connection.cursor()
select_query="""
select * from family"""
cursor.execute(select_query)
result=cursor.fetchall()
for row in result:
    print(row)
cursor.close()
connection.close()