import pymysql


conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    db='test',
    charset='utf8'
)
cursor = conn.cursor()
print(conn)
print(cursor)
cursor.close()
conn.close()


cursor = conn.cursor()
sql = 'select userid, username from user;'
cursor.execute(sql)
print(cursor.rowcount)
rs = cursor.fetchone()
print(rs)
rs = cursor.fetchmany(3)
print(rs)
rs = cursor.fetchall()
print(rs)
cursor.close()
conn.close()


cursor = conn.cursor()
sql = 'select userid, username from user;'
cursor.execute(sql)
rs = cursor.fetchall()
for row in rs:
    print('userid=%s,\tusername=%s' % row)
cursor.close()
conn.close()
