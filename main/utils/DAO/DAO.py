from datetime import datetime

from main.utils.DAO import DBUtils
from main.utils.ACM.ACM import ACMUser, TrainningRecord
from main.Exception.Error import DbError

# --------------------------------------
# user表操作

class DAOForUser():

    # 添加用户，以ACMUser为单位进行添加
    def addUser(user: ACMUser) -> int:
        try:
            db = DBUtils.getConnection() # 数据库连接
            cursor = db.cursor() # 游标

            sql = "insert into user(username, passhash, name, department, major, joinTime, allTrainningTime, isTrainning, currRecordId, admin, email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, email);"

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
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

    # 根据用户名/学号删除用户
    def deleteUserByUsername(username: str) -> bool:
        try:
            db = DBUtils.getConnection() # 数据库连接
            cursor = db.cursor() # 游标

            sql = "delete from user where username=%s"

            cursor(sql, (username,))
            db.commit()
        except Exception as e:
            db.rollback()
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

    # 根据用户名/学号更新个人信息/状态
    def updateUserInfoByUsername(user: ACMUser):
        try:
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
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)
                        
    # 根据用户名/学号更改密码
    def updatePwdByUsername(username: str, passhash: str):
        try:
            db = DBUtils.getConnection()
            cursor = db.cursor()

            sql = "update user set passhash=%s where username=%s;"

            cursor.execute(sql, (passhash, username))
            db.commit()
        except Exception as e:
            db.rollback()
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

    # 根据用户名/学号更改用户权限组
    def updatePrivByUsername(username: str, admin: bool):
        try:
            db = DBUtils.getConnection() # 数据库连接
            cursor = db.cursor() # 游标
            
            sql = "update user set admin=%s where username=%s;"

            if admin:
                status = "Y"
            else:
                status = "N"

            cursor.execute(sql, (status, username))
            db.commit()
        except Exception as e:
            db.rollback()
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

    # --------------------------
    # 查询操作均返回ACMUser对象或对象列表
    #         

    # 根据用户名/学号查找用户
    def getUserByUsername(username: str):
        try:
            db = DBUtils.getConnection() # 数据库连接
            cursor = db.cursor() # 游标

            sql = "select username, passhash, name, department, major, joinTime, allTrainningTime, isTrainning, currRecordId, admin, email from user where username=%s;"

            cursor.execute(sql, (username))
            unformatedUser = cursor.fetchone()
            
            if unformatedUser != None:
                return ACMUser(*unformatedUser)
            else:
                return None
        except Exception as e:
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

    # 根据当前是否在训练状态查询
    def getUsersByStatus(isTrainning: bool) -> list:
        try:
            db = DBUtils.getConnection() # 数据库连接
            cursor = db.cursor() # 游标

            users = []

            sql = "select username, passhash, name, department, major, joinTime, allTrainningTime, isTrainning, currRecordId, admin, email from user where isTrainning=%s order by id;"

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
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

    # 根据用户权限组查询
    def getUsersByPriv(admin: bool) -> list:
        try:
            db = DBUtils.getConnection() # 数据库连接
            cursor = db.cursor() # 游标

            users = []

            sql = "select username, passhash, name, department, major, joinTime, allTrainningTime, isTrainning, currRecordId, admin, email from user where admin=%s;"

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
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

    # 获取user表全部信息
    def getAll(self):
        try:
            db = DBUtils.getConnection() # 数据库连接
            cursor = db.cursor() # 游标

            users = []
            sql = "select username, passhash, name, department, major, joinTime, allTrainningTime, isTrainning, currRecordId, admin, email from user;"

            cursor.execute(sql)
            
            unformatedUsers = cursor.fetchall()
            if unformatedUsers != None:
                for unformatedUser in unformatedUsers:
                    users.append(ACMUser(*unformatedUser))
            
            return users
        except Exception as e:
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

# ----------------------------------------------------
# trainningRecord表操作

class DAOForTrainRecord():

    # 添加签到记录
    def addTrainRecord(record: TrainningRecord) -> int:
        try:
            db = DBUtils.getConnection() # 数据库连接
            cursor = db.cursor() # 游标

            sql = "insert into trainningrecord(username, startTime, endTime, valid, isRecord, timeLength) values (%s, %s, %s, %s, %s, %s)"

            if record.getValid():
                valid = "Y"
            else:
                valid = "N"
            
            if record.getIsRecord():
                isRecord = "Y"
            else:
                isRecord = "N"
            
            cursor.execute(sql, (record.getUsername(),
                                       record.getStartTime(),
                                       record.getEndTime(),
                                       valid,
                                       isRecord,
                                       record.getTimeLength()))
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)
    
    # 根据记录id删除记录
    def deleteTrainRecordById(id: int) -> bool:
        try:
            db = DBUtils.getConnection() # 数据库连接
            cursor = db.cursor() # 游标

            sql = "delete from trainningrecord where id=%s"

            cursor.execute(sql, (id,))
            db.commit()
        except Exception as e:
            db.rollback()
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

    # 根据记录id更新记录信息
    def updateRecordById(trainningRecord: TrainningRecord):
        try:
            db = DBUtils.getConnection()
            cursor = db.cursor()

            sql = "update trainningrecord set endTime=%s, valid=%s, isRecord=%s, timeLength=%s where id=%s;"

            if trainningRecord.getValid():
                status = "Y"
            else:
                status = "N"
            
            if trainningRecord.getIsRecord():
                isRecord = "Y"
            else:
                isRecord = "N"
            
            cursor.execute(sql, (trainningRecord.getEndTime(),
                                 status,
                                 isRecord,
                                 trainningRecord.getTimeLength(),
                                 trainningRecord.geti))

        except Exception as e:
            db.rollback()
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)
    
    # 根据id获取训练记录
    def getTrainRecordById(id: int) -> TrainningRecord:
        try:
            db = DBUtils.getConnection()
            cursor = db.cursor()

            sql = "select username, startTime, endTime, valid, isRecord, timeLength, id from trainningrecord where id=%s;"

            cursor.execute(sql, (id,))

            unformatedRecord = cursor.fetchone()
            if unformatedRecord != None:
                return TrainningRecord(*unformatedRecord)
            else:
                return None
        except Exception as e:
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

    # 根据用户名查询训练记录
    def getTrainRecordByUsername(username: str) -> list:
        try:
            db = DBUtils.getConnection()
            cursor = db.cursor()

            sql = "select username, startTime, endTime, valid, isRecord, timeLength, id from trainningrecord where username=%s;"

            cursor.execute(sql, (username,))

            unformatedRecords = cursor.fetchall()
            records = []
            if unformatedRecords != None:
                for unformatedRecord in unformatedRecords:
                    records.append(ACMUser(*unformatedRecord))
            return records
        except Exception as e:
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)

    # 获取全部训练记录
    def getAllTrainRecords() -> list:
        try:
            db = DBUtils.getConnection()
            cursor = db.cursor()

            sql = "select username, startTime, endTime, valid, isRecord, timeLength, id from trainningrecord;"

            cursor.execute(sql)

            unformatedRecords = cursor.fetchall()
            records = []
            if unformatedRecords != None:
                for unformatedRecord in unformatedRecords:
                    records.append(ACMUser(*unformatedRecord))
            return records
        except Exception as e:
            raise DbError(str(e))
        finally:
            DBUtils.closeConnection(db)



    