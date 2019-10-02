#import regform
import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="")
sql = connection.cursor()
print("connected successfully")

#   def create_db(db_name):
#     query="CREATE DATABASE IF NOT EXISTS "+db_name
#     sql.execute(query)
#     print("database created")
#     return db_name
#
# db_name=create_db("regdetails")
sql.execute("USE regdetails")
print("database selected")


def create_tb(tb_name):
    query="CREATE TABLE %s(email varchar(30) primary key,username varchar(30),name varchar(30),gender varchar(10),password varchar(30))" % tb_name
    sql.execute(query)
    print("table created")

create_tb("table1")




