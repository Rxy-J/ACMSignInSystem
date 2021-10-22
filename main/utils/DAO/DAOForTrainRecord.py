#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ACMSignInSystem
@File ：DAOForTrainRecord.py
@Author ：OrangeJ
@Date ：2021/10/10 13:32 
'''

from main.utils.DAO import DBUtils
from main.utils.ACM.ACM import TrainningRecord
from main.Exception.Error import DbError


# 添加签到记录
def addTrainRecord(record: TrainningRecord) -> int:
    try:
        db = None
        db = DBUtils.getConnection()  # 数据库连接
        cursor = db.cursor()  # 游标

        sql = "insert into trainningrecord(username, startTime, endTime, status, timeLength) values (%s, %s, %s, %s, %s);"

        cursor.execute(sql, (record.getUsername(),
                             record.getStartTime(),
                             record.getEndTime(),
                             record.getStatus(),
                             record.getTimeLength()))
        db.commit()
        return cursor.lastrowid
    except Exception as e:
        db.rollback()
        raise DbError(str(e))
    finally:
        if db is not None:
            DBUtils.closeConnection(db)


# 根据记录id删除记录
def deleteTrainRecordById(tid: int) -> bool:
    try:
        db = None
        db = DBUtils.getConnection()  # 数据库连接
        cursor = db.cursor()  # 游标

        sql = "delete from trainningrecord where id=%s"

        cursor.execute(sql, (tid,))
        db.commit()
    except Exception as e:
        db.rollback()
        raise DbError(str(e))
    finally:
        if db is not None:
            DBUtils.closeConnection(db)


# 根据记录id更新记录信息
def updateRecordById(trainningRecord: TrainningRecord):
    try:
        db = None
        db = DBUtils.getConnection()
        cursor = db.cursor()

        sql = "update trainningrecord set endTime=%s, status=%s, timeLength=%s where id=%s;"

        cursor.execute(sql, (trainningRecord.getEndTime(),
                             trainningRecord.getStatus(),
                             trainningRecord.getTimeLength(),
                             trainningRecord.getId()))

    except Exception as e:
        db.rollback()
        raise DbError(str(e))
    finally:
        if db is not None:
            DBUtils.closeConnection(db)


# 根据id获取训练记录
def getTrainRecordById(tid: int) -> TrainningRecord:
    try:
        db = None
        db = DBUtils.getConnection()
        cursor = db.cursor()

        sql = "select username, startTime, endTime, status, timeLength, id from trainningrecord where id=%s order by id;"

        cursor.execute(sql, (tid,))

        unformatedRecord = cursor.fetchone()
        if unformatedRecord != None:
            return TrainningRecord(*unformatedRecord)
        else:
            return None
    except Exception as e:
        raise DbError(str(e))
    finally:
        if db is not None:
            DBUtils.closeConnection(db)


# 根据用户名查询训练记录
def getTrainRecordByUsername(username: str, suffix: str = "") -> list:
    try:
        db = None
        db = DBUtils.getConnection()
        cursor = db.cursor()

        sql = "select username, startTime, endTime, status, timeLength, id from trainningrecord where username=%s {} order by id;".format(
            suffix)

        cursor.execute(sql, (username,))

        unformatedRecords = cursor.fetchall()
        records = []
        if unformatedRecords != None:
            for unformatedRecord in unformatedRecords:
                records.append(TrainningRecord(*unformatedRecord))
        return records
    except Exception as e:
        raise DbError(str(e))
    finally:
        if db is not None:
            DBUtils.closeConnection(db)


# 获取全部训练记录
def getAllTrainRecords() -> list:
    try:
        db = None
        db = DBUtils.getConnection()
        cursor = db.cursor()

        sql = "select username, startTime, endTime, status, timeLength, id from trainningrecord order by id;"

        cursor.execute(sql)

        unformatedRecords = cursor.fetchall()
        records = []
        if unformatedRecords is not None:
            for unformatedRecord in unformatedRecords:
                records.append(TrainningRecord(*unformatedRecord))
        return records
    except Exception as e:
        raise DbError(str(e))
    finally:
        if db is not None:
            DBUtils.closeConnection(db)
