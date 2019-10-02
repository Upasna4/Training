import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="")
sql=connection.cursor()

def insert_data(tb_name):
    query="INSERT INTO %s"(id,name,city,mobile)VALUES"(1,'user','chd',10)"%tb_name
    sql.execute(query)
    connection.commit()
    print("Data inserted")
