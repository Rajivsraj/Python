# import mysql.connector
# conn = mysql.connector.connect()
        # OR

"""
from mysql.connector import connect

# connection setup
conn = connect(host="localhost", username="root", password="", database="py_conn")

if conn.is_connected():
    print("Database Connected")

print(conn.close())


if conn.is_connected():
    print("Database Connected")
else:
    print("Connection closed")

"""

from mysql.connector import connect
conn_params = {
    "host": "localhost",
    "username":  "root",
    "password": "",
    "database": "py_conn"
}

conn = connect(**conn_params)
# print(conn.is_connected())
sql = "create table stu(id int primary key auto_increment, name varchar(20))"
cur_obj = conn.cursor()

x = cur_obj.execute(sql)
print(x)