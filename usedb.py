import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="")
sql=connection.cursor()          #connection.cursor ka obj h connection
print("connected successfully")


def create_db(dbname):
    query="CREATE DATABASE IF NOT EXISTS "+dbname
    sql.execute(query)
    print("database created")
    return dbname
dbname = create_db("student")
sql.execute("USE student")                 #to select database
print("database selected")


# def create_tb(table_name):
#     query="CREATE TABLE %s(id int primary key,name varchar(23),adress varchar(30),mobile BIGINT)"%table_name
#     sql.execute(query)
#     print("table created")
# table_name = create_tb("student_record")


# def insert_data(table_name):
#     query="INSERT INTO %s(id,name,adress,mobile)VALUES(1,'upasna','chd',1222)"%table_name
#     sql.execute(query)
#     connection.commit()
#     print("data inserted")
#
# insert_data("student_record")


# def insert_data(table_name,id,name,adress,mobile):
#     query="INSERT INTO %s(id,name,adress,mobile)VALUES""(%d,'%s','%s',%d)"%(table_name,id,name,adress,mobile)
#     sql.execute(query)
#     connection.commit()
#     print("data inserted")

# for i in range(5):
#     id=int(input("id"))
#     name=input("name")
#     adress=input("adress")
#     mobile=int(input("no"))
#     insert_data("student_record",id,name,adress,mobile)


def fetch_data(table_name):
    sql.execute("SELECT * FROM %s" % table_name)

    data=sql.fetchall()
    print(data)


fetch_data("student_record")






