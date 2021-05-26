# 数据库

## connection

```python
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
```

## cursor

```python
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
```

## transfer

```python
import pymysql
import sys
from pymysql import MySQLError


def log(f):
    def fn(*args, **kwargs):
        print(f.__name__ + ': ' + str(args[1:]))
        return f(*args, **kwargs)

    return fn


class TransferMoney(object):
    def __init__(self, conn):
        self.__conn = conn

    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.__conn.commit()
        except MySQLError as ex:
            self.__conn.rollback()
            raise ex
        except Exception as ex:
            self.__conn.rollback()
            raise ex

    @log
    def check_acct_available(self, acctid):
        cursor = self.__conn.cursor()
        try:
            sql = 'select acctid from account where acctid=%s;' % acctid
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) is not 1:
                raise Exception('帐号%s不存在！' % acctid)
        finally:
            cursor.close()

    @log
    def has_enough_money(self, acctid, money):
        cursor = self.__conn.cursor()
        try:
            sql = 'select acctid from account where acctid=%s AND money>%s;' % (
                acctid, money)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) is not 1:
                raise Exception('帐号%s余额不足！' % acctid)
        finally:
            cursor.close()

    @log
    def reduce_money(self, acctid, money):
        cursor = self.__conn.cursor()
        try:
            sql = 'update account set money=money-%s where acctid=%s;' % (
                money, acctid)
            cursor.execute(sql)
            if cursor.rowcount is not 1:
                raise Exception('帐号%s减款失败！' % acctid)
        finally:
            cursor.close()

    @log
    def add_money(self, acctid, money):
        cursor = self.__conn.cursor()
        try:
            sql = 'update account set money=money+%s where acctid=%s;' % (
                money, acctid)
            cursor.execute(sql)
            if cursor.rowcount is not 1:
                raise Exception('帐号%s加款失败！' % acctid)
        finally:
            cursor.close()


source_acctid = sys.argv[1]
target_acctid = sys.argv[2]
money = sys.argv[3]
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    db='test',
    charset='utf8'
)
transfer_money = TransferMoney(conn)
try:
    transfer_money.transfer(source_acctid, target_acctid, money)
except Exception as ex:
    print('出现问题：' + str(ex))
    conn.rollback()
finally:
    conn.close()
```
