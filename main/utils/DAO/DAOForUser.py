#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ACMSignInSystem
@File ：DAOForTrainRecord.py
@Author ：OrangeJ
@Date ：2021/10/10 13:32
'''

from main.utils.DAO import DBUtils
from main.utils.ACM.ACM import ACMUser

# 添加用户，以ACMUser为单位进行添加
def addUser(user: ACMUser) -> int:
    try:
        db = None
        db = DBUtils.getConnection()  # 数据库连接
        cursor = db.cursor()  # 游标
        sql = "insert into user(username, passhash, name, department, major, joinTime, allTrainningTime, isTrainning, currRecordId, admin, email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

        if user.getIsTrainning():
            status = "Y"
        else:
            status = "N"

        if user.getAdmin():
            admin = "Y"
        else:
            admin = "N"

        cursor.execute(sql, (user.getUsername(),
                             user.getPasshash(),
                             user.getName(),
                             user.getdepartment(),
                             user.getMajor(),
                             user.getJoinTime(),
                             user.getAllTrainningTime(),
                             status,
                             user.getCurrRecordId(),
                             admin,
                             user.getEmail()))
        db.commit()
        return cursor.lastrowid
    except Exception as e:
        db.rollback()
        raise Exception(str(e) + str(e.__traceback__.tb_lineno))
    finally:
        DBUtils.closeConnection(db)


# 根据用户名/学号删除用户
def deleteUserByUsername(username: str) -> bool:
    try:
        db = None
        db = DBUtils.getConnection()  # 数据库连接
        cursor = db.cursor()  # 游标

        sql = "delete from user where username=%s"

        cursor(sql, (username,))
        db.commit()
    except Exception as e:
        db.rollback()
        raise Exception(str(e))
    finally:
        DBUtils.closeConnection(db)


# 根据用户名/学号更新个人信息/状态
def updateUserInfoByUsername(user: ACMUser):
    try:
        db = None
        db = DBUtils.getConnection()
        cursor = db.cursor()

        sql = "update user set name=%s, department=%s, major=%s, allTrainningTime=%s, isTrainning=%s, currRecordId=%s where username=%s;"

        if user.getIsTrainning():
            status = "Y"
        else:
            status = "N"

        cursor.execute(sql, (user.getName(),
                             user.getdepartment(),
                             user.getMajor(),
                             user.getAllTrainningTime(),
                             status,
                             user.getCurrRecordId(),
                             user.getUsername()))
        db.commit()
    except Exception as e:
        db.rollback()
        raise Exception(str(e))
    finally:
        DBUtils.closeConnection(db)


# 根据用户名/学号更改密码
def updatePwdByUsername(username: str, passhash: str):
    try:
        db = None
        db = DBUtils.getConnection()
        cursor = db.cursor()

        sql = "update user set passhash=%s where username=%s;"

        cursor.execute(sql, (passhash, username))
        db.commit()
    except Exception as e:
        db.rollback()
        raise Exception(str(e))
    finally:
        DBUtils.closeConnection(db)


# 根据用户名/学号更改用户权限组
def updatePrivByUsername(username: str, admin: bool):
    try:
        db = None
        db = DBUtils.getConnection()  # 数据库连接
        cursor = db.cursor()  # 游标

        sql = "update user set admin=%s where username=%s;"

        if admin:
            status = "Y"
        else:
            status = "N"

        cursor.execute(sql, (status, username))
        db.commit()
    except Exception as e:
        db.rollback()
        raise Exception(str(e))
    finally:
        DBUtils.closeConnection(db)


# --------------------------
# 查询操作均返回ACMUser对象或对象列表
#

# 根据用户名/学号查找用户
def getUserByUsername(username: str):
    try:
        db = None
        db = DBUtils.getConnection()  # 数据库连接
        cursor = db.cursor()  # 游标

        sql = "select username, passhash, name, department, major, joinTime, allTrainningTime, isTrainning, currRecordId, admin, email from user where username=%s;"

        cursor.execute(sql, (username,))
        unformatedUser = cursor.fetchone()

        if unformatedUser != None:
            return ACMUser(*unformatedUser)
        else:
            return None
    except Exception as e:
        raise Exception(str(e))
    finally:
        DBUtils.closeConnection(db)


# 根据当前是否在训练状态查询
def getUsersByStatus(isTrainning: bool) -> list:
    try:
        db = None
        db = DBUtils.getConnection()  # 数据库连接
        cursor = db.cursor()  # 游标

        users = []

        sql = "select username, passhash, name, department, major, joinTime, allTrainningTime, isTrainning, currRecordId, admin, email from user where isTrainning=%s order by uid;"

        if isTrainning:
            status = "Y"
        else:
            status = "N"

        cursor.execute(sql, (status))
        unformatedUsers = cursor.fetchall()

        if unformatedUsers != None:
            for unformatedUser in unformatedUsers:
                users.append(ACMUser(*unformatedUser))
        return users
    except Exception as e:
        raise Exception(str(e))
    finally:
        DBUtils.closeConnection(db)


# 根据用户权限组查询
def getUsersByPriv(admin: bool) -> list:
    try:
        db = None
        db = DBUtils.getConnection()  # 数据库连接
        cursor = db.cursor()  # 游标

        users = []

        sql = "select username, passhash, name, department, major, joinTime, allTrainningTime, isTrainning, currRecordId, admin, email from user where admin=%s order by uid;"

        if admin:
            status = "Y"
        else:
            status = "N"

        cursor.execute(sql, (status))
        unformatedUsers = cursor.fetchall()

        if unformatedUsers != None:
            for unformatedUser in unformatedUsers:
                users.append(ACMUser(*unformatedUser))
        return users
    except Exception as e:
        raise Exception(str(e))
    finally:
        DBUtils.closeConnection(db)


# 获取user表全部信息
def getAll():
    try:
        db = None
        db = DBUtils.getConnection()  # 数据库连接
        cursor = db.cursor()  # 游标

        users = []
        sql = "select username, passhash, name, department, major, joinTime, allTrainningTime, isTrainning, currRecordId, admin, email from user order by uid;"

        cursor.execute(sql)

        unformatedUsers = cursor.fetchall()
        if unformatedUsers != None:
            for unformatedUser in unformatedUsers:
                users.append(ACMUser(*unformatedUser))

        return users
    except Exception as e:
        raise Exception(str(e))
    finally:
        DBUtils.closeConnection(db)
