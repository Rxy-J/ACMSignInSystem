#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DK 
@File ：DAOForOP.py
@Author ：OrangeJ
@Date ：2021/11/13 10:55 
'''
from main.utils.ACM.ACM import ACMUser, TrainningRecord
from main.utils.DAO import DBUtils


def updateSignStatus(user: ACMUser, record: TrainningRecord):
    try:
        db = None
        db = DBUtils.getConnection()  # 数据库连接
        cursor = db.cursor()  # 游标

        usql = "update user set allTrainningTime=%s, isTrainning=%s, currRecordId=%s where id=%s;"
        if record.getId() is None:
            rsql = "insert into trainningrecord(username, startTime) values (%s, %s);"
        else:
            rsql = "update trainnginrecord set endTime=%s, status=%s, timeLength=%s where id=%s;"

        cursor.execute(rsql, (record.getUsername(), record.getStartTime()))
        if record.getId() is None:
            user.setCurrRecordId(cursor.lastrowid)
        cursor.execute(usql, (user.getAllTrainningTime(), user.getIsTrainning(), user.getCurrRecordId()))

        db.commit()
        return user.getCurrRecordId()
    except Exception as e:
        db.rollback()
        raise Exception(str(e))
    finally:
        DBUtils.closeConnection(db)
