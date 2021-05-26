import pymysql
from pymysql import MySQLError


conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    db='test',
    charset='utf8'
)
cursor = conn.cursor()

sql_insert = 'insert into user(userid, username) values (10, "name");'
sql_update = 'update user set username="name" where userid=1;'
sql_delete = 'delete from user where userid<3;'
try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)
    conn.commit()
except MySQLError as ex:
    print(ex)
    conn.rollback()
cursor.close()
conn.close()
