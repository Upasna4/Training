import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="")
sql = connection.cursor()


def create_db(db_name):
    query="CREATE DATABASE IF NOT EXISTS "+db_name      #EXISTS K BAAD SPACE DENA WRNA ERROR DEGA
    sql.execute(query)
    print("database created")
    return db_name

db_name=create_db("database1")
sql.execute("USE database1")
print("Database Selected")

def create_tb(tb_name):
    query="CREATE TABLE %s(id int primary key,name varchar(30),city varchar(30),mobile BIGINT) "% tb_name
    sql.execute(query)
    print("Table Created")

# def insert_data(tb_name,u_id,name,city,mobile):
#      #query="INSERT INTO %s(id,name,city,mobile)VALUES(1,'user','chd',10)"%tb_name
#      query = "INSERT INTO %s(id,name,city,mobile)VALUES""(%d,'%s','%s',%d)" %(tb_name,u_id,name,city,mobile)
#      sql.execute(query)
#      connection.commit()
#      print("Data inserted")
#
# for i in range(5):
#      u_id=int(input("enter id"))
#      name=input("enter name")
#      city=input("enter city")
#      mobile=int(input("enter mobile"))
#      insert_data("record",u_id,name,city,mobile)
#

# def fetch_data(tb_name):
#     sql.execute("SELECT name,mobile  FROM %s" % tb_name)
#
#     data=sql.fetchall()
#     for i in data:
#         print(i)


#fetch_data("record")


# def fetch_with_where(tb_name,d_id):
#     sql.execute("SELECT * FROM %s WHERE id=%d"%(tb_name,d_id))
#     data=sql.fetchall()
#     print(data)
#
#
# fetch_with_where("record",1)



# def fetch_with_where(tb_name,d_id):
#     sql.execute("SELECT name FROM %s WHERE id=%d"%(tb_name,d_id))
#     data=sql.fetchall()
#     print(data)
#
#
# fetch_with_where("record",1)


# def fetch_with_where(tb_name):
#     sql.execute("SELECT * FROM %s" %tb_name)
#     data=sql.fetchone()                         #gives only first row
#     print(data)
#
#
# fetch_with_where("record")


def fetch_with_where(tb_name):
    sql.execute("SELECT * FROM %s" % tb_name)
    for i in range(3):                  #gives first three rows
        data=sql.fetchone()
        print(data)


# fetch_with_where("record")


# def update_data(tb_name):
#     sql.execute("UPDATE %s SET name='anshu',city='jmu' WHERE id=3"%tb_name)
#     connection.commit()                     #here values are updated
#     print("updated successfully")
#
#
# update_data("record")


# def generic_update(tb_name=None,t_id=None,name=None,city=None,mobile=None):
#     if tb_name is None and t_id is None and name is None and city is None and mobile is None:
#         print("nothing to chng")
#     elif tb_name is not None and t_id is not None and name is not None and city is not None and mobile !=0:
#         sql.execute("UPDATE %s SET name='%s',city='%s',mobile=%d WHERE id=%d" % (tb_name,name,city,mobile,t_id))
#         connection.commit()
#         print("data updated")
#     elif tb_name!="" and t_id!=0 and name is not and city is not None and mobile != 0:
#         sql.execute("UPDATE %s SET name='%s',city='%s',mobile=%d WHERE id=%d" % (tb_name, name, city, mobile, t_id))
#         connection.commit()
    # elif name is None and city is None and mobile is not None:
    #     sql.execute("UPDATE %s SET mobile=%d WHERE u_id=%d" % (tb_name,mobile,u_id))
    #     connection.commit()
    # elif tb_name is not None and t_id is not None and name is not None and city is not None and mobile is None:
    #     sql.execute("UPDATE %s SET name='%s',city='%s' WHERE u_id=%d" % (tb_name,name,city,u_id))
    #     connection.commit()
    # elif name is None and city is not None and mobile is None:
    #     sql.execute("UPDATE %s SET city='%s' WHERE u_id=%d" % (tb_name,city,u_id))
    #     connection.commit()


#update_data("record",3,"sam","guj",45)
#update_data("record",1,"upasna","sgr",67)
#update_data("record",88,"","",435)
#update_data("record",568,"shikha","jmu",0)
#update_data("record",879,"","del",0)

#generic_update()
#generic_update("record",879,"user","del",7899)
#generic_update("record",879,"anshu","del",6777)
#generic_update("record",8634,"piya","jmu",0)


def generic_update(**keyword):
    if keyword.get("tb_name") is None and keyword.get("id") is None and keyword.get("name") is None and keyword.get("city") is None\
    and keyword.get("mobile") is None:                  #sub none hai   1
        print("nothing to change")

    elif keyword.get("tb_name") is not None and keyword.get("id") is not None and keyword.get("name") is not None\
        and keyword.get("city") is not None and keyword.get("mobile") is not None:
        sql.execute("update %s set name='%s',city='%s',mobile=%d where id=%d" %(keyword['tb_name'],keyword['name'],keyword['city'],\
            keyword['mobile'],keyword['id']))
        connection.commit()                             #sub update hore hai    2
        print("data updated")

    elif keyword.get("tb_name") is None and keyword.get("id") is not None and keyword.get("name") is not None\
        and keyword.get("city") is not None and keyword.get("mobile") is not None:
        print("table not mentioned")      #rest everythng mentioned    3

    elif keyword.get("tb_name") is None and keyword.get("id") is None and keyword.get("name") is not None\
        and keyword.get("city") is not None and keyword.get("mobile") is not None:
        print("table not mentioned")     #id also not mentioned   4

    elif keyword.get("tb_name") is None and keyword.get("id") is not None and keyword.get("name") is None\
        and keyword.get("city") is None and keyword.get("mobile") is None:
        print("table not mentioned")            #name also no mentioned   5

    elif keyword.get("tb_name") is None and keyword.get("id") is None and keyword.get("name") is not None\
        and keyword.get("city") is None and keyword.get("mobile") is not None:
        print("table not mentioned")      #city also not mentioned   6

    elif keyword.get("tb_name") is None and keyword.get("id") is not None and keyword.get("name") is not None\
        and keyword.get("city") is not None and keyword.get("mobile") is None:
        print("table not mentioned")       #mobile also not mentioned   7

    elif keyword.get("tb_name") is None and keyword.get("id") is None and keyword.get("name") is None\
        and keyword.get("city") is not None and keyword.get("mobile") is not None:
        print("table not mentioned")       #id n name not mentioned   8

    elif keyword.get("tb_name") is None and keyword.get("id") is None and keyword.get("name") is None\
        and keyword.get("city") is None and keyword.get("mobile") is not None:
        print("table not mentioned")           #id name city not mentioned    9

    elif keyword.get("tb_name") is None and keyword.get("id") is None and keyword.get("name") is None\
        and keyword.get("city") is not None and keyword.get("mobile") is not None:
        print("table not mentioned")           #id city not mentioned    10

    elif keyword.get("tb_name") is None and keyword.get("id") is None and keyword.get("name") is not None\
        and keyword.get("city") is not None and keyword.get("mobile") is None:
        print("table not mentioned")          #id mobile not mentioned    11

    elif keyword.get("tb_name") is None and keyword.get("id") is not None and keyword.get("name") is None\
        and keyword.get("city") is None and keyword.get("mobile") is not None:
        print("table not mentioned")          #name city not mentioned    12

    elif keyword.get("tb_name") is not None and keyword.get("id") is None and keyword.get("name") is None\
        and keyword.get("city") is None and keyword.get("mobile") is None:
        print("only tablename mentioned")      #13

    elif keyword.get("tb_name") is not None and keyword.get("id") is None and keyword.get("name") is not None\
        and keyword.get("city") is not None and keyword.get("mobile") is not None:
        print("id not mentioned")              #14

    elif keyword.get("tb_name") is not None and keyword.get("id") is None and keyword.get("name") is None\
        and keyword.get("city") is not None and keyword.get("mobile") is not None:
        print("id not mentioned")      #name also not mentioned    15

    elif keyword.get("tb_name") is not None and keyword.get("id") is None and keyword.get("name") is not None\
        and keyword.get("city") is None and keyword.get("mobile") is not None:
        print("id not mentioned")          #city also not mentioned     16

    elif keyword.get("tb_name") is not None and keyword.get("id") is None and keyword.get("name") is not None\
        and keyword.get("city") is not None and keyword.get("mobile") is None:
        print("id not mentioned")         #mobile also not mentioned    17

    elif keyword.get("tb_name") is not None and keyword.get("id") is None and keyword.get("name") is None\
        and keyword.get("city") is None and keyword.get("mobile") is not None:
        print("id not mentioned")       #name n city also not mentioned     18

    elif keyword.get("tb_name") is not None and keyword.get("id") is None and keyword.get("name") is not None\
        and keyword.get("city") is None and keyword.get("mobile") is None:
        print("id not mentioned")         #city n mobile not mentioned      19

    elif keyword.get("tb_name") is not None and keyword.get("id") is None and keyword.get("name") is None\
        and keyword.get("city") is not None and keyword.get("mobile") is None:
        print("id not mentioned")          #name n mobile not mentioned   20

    elif keyword.get("tb_name") is not None and keyword.get("id") is not None and keyword.get("name") is not None\
        and keyword.get("city") is None and keyword.get("mobile") is None:
        sql.execute("update %s set name='%s' where id=%d" % (keyword['tb_name'], keyword['name'],keyword['id']))
        connection.commit()        #21
        print("only name updated")

    elif keyword.get("tb_name") is not None and keyword.get("id") is not None and keyword.get("name") is None\
        and keyword.get("city") is not None and keyword.get("mobile") is None:
        sql.execute("update %s set city='%s' where id=%d" % (keyword['tb_name'], keyword['city'],keyword['id']))
        connection.commit()       #22
        print("only city updated")

    elif keyword.get("tb_name") is not None and keyword.get("id") is not None and keyword.get("name") is None\
        and keyword.get("city") is None and keyword.get("mobile") is not None:
        sql.execute("update %s set mobile='%s' where id=%d" % (keyword['tb_name'],keyword['mobile'],keyword['id']))
        connection.commit()                  #23
        print("only mobile updated")

    elif keyword.get("tb_name") is not None and keyword.get("id") is not None and keyword.get("name") is not None\
        and keyword.get("city") is not None and keyword.get("mobile") is None:
        sql.execute("update %s set name='%s' where id=%d" % (keyword['tb_name'], keyword['name'],keyword['id']))
        connection.commit()        #24
        print("only name and city updated")

    elif keyword.get("tb_name") is not None and keyword.get("id") is not None and keyword.get("name") is not None\
        and keyword.get("city") is None and keyword.get("mobile") is not None:
        sql.execute("update %s set name='%s' where id=%d" % (keyword['tb_name'], keyword['name'],keyword['id']))
        connection.commit()       #25
        print("only name and mobile updated")



#generic_update(city="chd",name="ram",tb_name="record",mobile=12345,id=8634)
#generic_update(city="chd",name="ram",mobile=12345,id=8634)
#generic_update(tb_name="record")
#generic_update(city="chd",name="ram",tb_name="record",mobile=12345)
#generic_update(name="geeta",tb_name="record",id=3)
#generic_update(city="hry",tb_name="record",id=3)
#generic_update(tb_name="record",mobile=6854,id=568)
#generic_update(tb_name="record",name="dikhu",city="kmr",id=88)
generic_update(name="raman",tb_name="record",mobile=8532,id=3)



# def generic_insert(**keyword):
#     if keyword.get("tb_name") is not None and keyword.get("id") is not None and keyword.get("name") is not None \
#     and keyword.get("city") is not None and keyword.get("mobile") is not None:
#         sql.execute("INSERT INTO %s(id,name,city,mobile)VALUES(%d,'%s','%s',%d)" % (keyword['tb_name'],keyword=['id'],\
#             keyword['name'],keyword['city'],keyword['mobile']))
#         connection.commit()
#         print("Data inserted")
#
#
# generic_insert("record",4,"piya","kmr",76890)
#
#



