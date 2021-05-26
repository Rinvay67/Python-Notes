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
