import configparser
import os

from ACMSignInSystem.settings import BASE_DIR

MYSQL = "mysql"
MYSQL_INI = os.path.join(BASE_DIR, "main/Config/MySQL.ini")

conf = configparser.ConfigParser()
conf.read(MYSQL_INI)

MYSQL_HOST = conf.get(MYSQL, "host")
MYSQL_PORT = conf.get(MYSQL, "port")
MYSQL_USER = conf.get(MYSQL, "user")
MYSQL_PASSWORD = conf.get(MYSQL, "password")
MYSQL_DATABASE = conf.get(MYSQL, "database")