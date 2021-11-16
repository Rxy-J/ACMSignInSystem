import pymysql
from pymysql.connections import Connection

from main.Config import MysqlConfig
from main.Exception.Error import DbConnectError


def getConnection() -> Connection:
    try:
        return pymysql.connect(
            host=MysqlConfig.MYSQL_HOST,
            user=MysqlConfig.MYSQL_USER,
            password=MysqlConfig.MYSQL_PASSWORD,
            database=MysqlConfig.MYSQL_DATABASE
        )
    except Exception as e:
        # print(str(e))

        raise DbConnectError


def closeConnection(conn: Connection):
    try:
        if conn is not None:
            conn.close()
    except Exception as e:
        print(str(e))
