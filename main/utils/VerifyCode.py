import time
import hmac
import hashlib
import threading

from datetime import datetime

from main.Config.GlobalConfig import EMAIL_VERIFY_CODE_TIME

# 邮件验证码
class EmailKeyGen(threading.Thread):
    def __init__(self, codeLength: int=4, daemon: bool=True) -> None:
        super().__init__(daemon=daemon)
        self.__codeLength = codeLength
        self.__codeList = []


    def run(self):
        while True:
            time.sleep(EMAIL_VERIFY_CODE_TIME.total_seconds())
            currTime = datetime.now()
            for code in self.__codeList : 
                if (currTime - code["time"]) > EMAIL_VERIFY_CODE_TIME:
                    self.__codeList.remove(code)

    def getCode(self):
        currTime = datetime.now()
        temp = hashlib.md5(currTime.strftime("%Y%m%d%H%M%S").encode()).hexdigest()
        currCode = temp[(-1-self.__codeLength):-1]

        self.__codeList.append({
            "code" : currCode,
            "time" : currTime
        })
        return currCode

    def checkCode(self, code: str) -> bool:
        for i in self.__codeList:
            if code == i["code"]:
                return True
        return False


# 管理员验证码
class TOTP(threading.Thread):
    
    def __init__(self, key: str, codeLength: int, daemon: bool=True) -> None:
        super().__init__(daemon=daemon)
        self.__key = key
        self.__currTime = None
        self.__preCode = None
        self.__currCode = None
        self.__codeLength = codeLength

    def run(self):
        while True:
            self.__preCode = self.__currCode
            self.__currCode = self.process()
            # print(self.__currCode)
            time.sleep(10)
            self.__preCode = None
            time.sleep(20)

    def process(self) -> str:
        self.__currTime = str(round(time.time()))
        hashCode = hmac.new(self.__key.encode(), self.__currTime.encode(), hashlib.sha1).hexdigest()
        pos = int(hashCode[-1], 16)
        encryptionCode = hashCode[pos*2:pos*2+(4*2)]
        encryptionNum = int(encryptionCode,16)
        tempCode = str(encryptionNum % 10**self.__codeLength)
        finalCode = "0"*(self.__codeLength - len(tempCode)) + tempCode

        return finalCode
        
    def getPreCode(self) -> str:
        return self.__preCode

    def getCurrCode(self) -> str:
        return self.__currCode
