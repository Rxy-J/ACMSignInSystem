from datetime import datetime


# ACM基地用户
from typing import Optional


class ACMUser:
    def __init__(self,
                 username: str,
                 passhash: str,
                 name: str,
                 department: str = None,
                 major: str = None,
                 joinTime: datetime = None,
                 allTrainningTime: int = 0,
                 isTrainning: bool = False,
                 currRecordId: str = None,
                 admin: bool = False,
                 email: bool = None) -> None:

        self.__username = username  # 用户名/学号
        self.__passhash = passhash  # 密码，必须为MD5码
        self.__name = name  # 姓名
        self.__department = department  # 学院
        self.__major = major  # 专业
        self.__joinTime = joinTime  # 入队时间
        self.__allTrainningTime = allTrainningTime if type(allTrainningTime) == int else eval(allTrainningTime)  # 总训练时长
        self.__isTrainning = isTrainning if type(isTrainning) == bool else self.parserBool(isTrainning)  # 当前是否在训练
        self.__currRecordId = currRecordId  # 当前正在进行训练的训练记录id
        self.__admin = admin if type(admin) == bool else self.parserBool(admin)  # 是否为管理员
        self.__email = email

    def getUsername(self) -> str:
        return self.__username

    def getPasshash(self) -> str:
        return self.__passhash

    def getName(self) -> str:
        return self.__name

    def getdepartment(self) -> str:
        return self.__department

    def getMajor(self) -> str:
        return self.__major

    def getJoinTime(self) -> datetime:
        return self.__joinTime

    def getAllTrainningTime(self) -> int:
        return self.__allTrainningTime

    def getFormatedAllTrainningTime(self) -> str:
        t = self.__allTrainningTime

        d = int(t / (3600 * 24))
        t -= d * 3600 * 24

        h = int(t / 3600)
        t -= h * 3600

        m = int(t / 60)
        t -= m * 60

        return "{}天{}小时{}分钟{}秒".format(d, h, m, t)

    def getIsTrainning(self) -> bool:
        return self.__isTrainning

    def getCurrRecordId(self) -> str:
        return self.__currRecordId

    def getAdmin(self) -> bool:
        return self.__admin

    def getEmail(self) -> str:
        return self.__email

    def getAll(self) -> tuple:
        return (self.__username, self.__passhash, self.__name, self.__department, self.__major, self.__joinTime,
                self.__allTrainningTime, self.__isTrainning, self.__currRecordId, self.__admin, self.__email)

    def setIsTrainning(self, isTrainning: bool) -> None:
        self.__isTrainning = isTrainning

    def setCurrRecordId(self, currRecordId: str) -> None:
        self.__currRecordId = currRecordId

    def setAllTrainningTime(self, allTrainningTime: int) -> None:
        self.__allTrainningTime = allTrainningTime

    def parserBool(self, source: str) -> bool:
        if source == "Y":
            return True
        else:
            return False

    def getDict(self) -> dict:
        return {
            "username": self.getUsername(),
            "name": self.getName(),
            "department": self.getdepartment(),
            "major": self.getMajor(),
            "joinTime": self.getJoinTime().strftime("%Y.%m.%d") if self.getJoinTime() else None,
            "allTrainningTime": self.getFormatedAllTrainningTime(),
            "admin": self.getAdmin(),
            "email": self.getEmail()

        }

    def __repr__(self):
        return "username=%s, passhash=%s, name=%s, department=%s, major=%s, joinTime=%s, allTrainningTime=%s, isTrainning=%s, currRecordId=%s, admin=%s, email=%s" % (
        self.__username,
        self.__passhash,
        self.__name,
        self.__department,
        self.__major,
        self.__joinTime,
        self.__allTrainningTime,
        self.__isTrainning,
        self.__currRecordId,
        self.__admin,
        self.__email)

    def __str__(self):
        return self.__repr__()


# 训练记录
class TrainningRecord():
    def __init__(self,
                 username: str,
                 startTime: datetime,
                 endTime: datetime = None,
                 valid: bool = False,
                 isRecord: bool = False,
                 timeLength: int = 0,
                 id: int = None) -> None:
        self.__id = id  # 记录id
        self.__username = username  # 用户名
        self.__startTime = startTime  # 训练开始时间
        self.__endTime = endTime  # 训练结束时间
        self.__valid = valid if type(isRecord) == bool else self.parserBool(valid)  # 是否有效
        self.__isRecord = isRecord if type(isRecord) == bool else self.parserBool(isRecord)  # 是否被记录
        self.__timeLength = timeLength  # 本次训练时长

    def getId(self) -> int:
        return self.__id

    def getUsername(self) -> str:
        return self.__username

    def getStartTime(self) -> datetime:
        return self.__startTime

    def getEndTime(self) -> datetime:
        return self.__endTime

    def getValid(self) -> bool:
        return self.__valid

    def getIsRecord(self) -> bool:
        return self.__isRecord

    def getTimeLength(self) -> int:
        return self.__timeLength

    def getFormatedTimeLength(self) -> str:
        t = self.__timeLength
        t_string = ""

        d = int(t / (3600 * 24))
        t -= d * 3600 * 24
        if d:
            t_string += "{}天".format(d)

        h = int(t / 3600)
        t -= h * 3600
        if h:
            t_string += "{}小时".format(h)

        m = int(t / 60)
        t -= m * 60
        if m:
            t_string += "{}分钟".format(m)
        if t:
            t_string += "{}秒".format(t)
        if not t_string:
            t_string = "0秒"

        return t_string

    def getAll(self) -> tuple:
        return self.__username, self.__startTime, self.__endTime, self.__valid, self.__isRecord, self.__timeLength

    def setEndTime(self, endTime: datetime) -> None:
        self.__endTime = endTime

    def setValid(self, valid: bool) -> None:
        self.__valid = valid

    def setIsRecord(self, isRecord: bool) -> None:
        self.__isRecord = isRecord

    def setTimeLength(self, timeLength: str) -> None:
        self.__timeLength = timeLength

    def parserBool(self, source: str) -> bool:
        if source == "Y":
            return True
        else:
            return False

    def getDict(self) -> dict:
        print(self.getStartTime())
        print(self.getEndTime())
        return {
            "id": self.getId(),
            "username": self.getUsername(),
            "startTime": self.getStartTime().strftime("%Y.%m.%d %H:%M:%S"),
            "endTime": self.getEndTime().strftime("%Y.%m.%d %H:%M:%S"),
            "valid": self.getValid(),
            "isRecord": self.getIsRecord(),
            "timeLength": self.getFormatedTimeLength()
        }

    def getAll(self) -> tuple[Optional[int], str, datetime, Optional[datetime], bool, bool, int]:
        return (self.__id, self.__username, self.__startTime, self.__endTime, self.__valid, self.__isRecord, self.__timeLength)

    def __repr__(self):
        return "id=%s, username=%s, startTime=%s, endTime=%s, valid=%s, isRecord=%s, timeLength=%s" % (self.__id,
                                                                                                       self.__username,
                                                                                                       self.__startTime,
                                                                                                       self.__endTime,
                                                                                                       self.__valid,
                                                                                                       self.__isRecord,
                                                                                                       self.__timeLength)

    def __str__(self):
        return self.__repr__()
