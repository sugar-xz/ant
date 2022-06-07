import os
import psycopg2
import pymysql
from testframe.common.logger import Log
from testframe.common.config_util import ConfigUtil

db_name = os.environ.get("AUTO_DB", "postgres")


class DBExecute(object):
    def __init__(self):
        self.logger = Log.get_log()
        self.db = None
        self.cursor = None

        self.host = ConfigUtil.get_ini(db_name, "host")
        self.username = ConfigUtil.get_ini(db_name, "user")
        self.port = ConfigUtil.get_ini(db_name, "port")
        self.password = ConfigUtil.get_ini(db_name, "password")
        self.database = ConfigUtil.get_ini(db_name, "database")


    def connectDB(self):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            if db_name == "postgres":
                self.db = psycopg2.connect(database=self.database, user=self.username, password=self.password,
                                           host=self.host, port=self.port)
            elif db_name == "mysql":
                self.db = pymysql.Connect(host=self.host, port=int(self.port), user=self.username, passwd=self.password,
                                          db=self.database)
            # create cursor
            self.cursor = self.db.cursor()
            self.logger.debug("Connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self, sql, much=True):
        """
        :param much:
        :param sql: sql语句，动态语法时包含占位符%s
                    "SELECT name,saving FROM trade WHERE account = '%s' % ('13512345678',)"
                    "SELECT name,saving FROM trade WHERE account = '13512345678'"
        :type sql: string
        :return:
        """
        self.connectDB()
        # executing sql
        try:
            if not much:
                self.cursor.execute(sql)
            else:
                for i in sql:
                    self.cursor.execute(i)
            # executing by committing to DB
            self.db.commit()
        except Exception as e:
            self.logger.error(e.args)
            self.db.rollback()
        return self.cursor

    def executeSQL2(self, sql, values):
        """
        sql = "SELECT name,saving FROM trade WHERE account = '%s' "
        values = ('13512345678',)
        """
        self.connectDB()
        # executing sql
        try:
            self.cursor.execute(sql % values)
            # executing by committing to DB
            self.db.commit()
        except Exception as e:
            self.logger.error(e.args)
            self.db.rollback()
        return self.cursor

    def get_all(self):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        if self.cursor is not None:
            return self.cursor.fetchall()

    def get_one(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        return value

    def closeDB(self):
        """
        close database
        :return:
        """
        if self.db is not None or self.cursor is not None:
            self.cursor.close()
            self.db.close()
        self.logger.debug("Database closed!")


if __name__ == '__main__':
    con = DBExecute()
    con.executeSQL(["SELECT * FROM auth_user;","SELECT * FROM auth_user where id=2;"])
    # data = con.get_all()
    # for row in data:
    #     print("ID = ", row[0])
    #     print("ID = ", row[1])
    #     print("ID = ", row[2])
    con.closeDB()
