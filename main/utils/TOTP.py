import time
import hmac
import base64
import hashlib
import threading


class TOTP(threading.Thread):
    
    def __init__(self, key: str, codeLength: int) -> None:
        self.__key = key
        self.__currTime = None
        self.__preCode = None
        self.__currCode = None
        self.__codeLength = codeLength

        self.__hexDict = {
            "0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "a" : 10,
            "b" : 11,
            "c" : 12,
            "d" : 13,
            "e" : 14,
            "f" : 15
        }

    def hexstr2int(self, string: str) -> int:
        length = len(string)
        cnt = length - 1
        intger = 0

        while cnt >= 0:
            temp = self.__hexDict[string[cnt]]
            intger += temp * 16**(length - cnt -1)
            cnt -= 1
        
        return intger

    def process(self) -> str:
        self.__currTime = str(round(time.time()))
        hashCode = hmac.new(self.__key.encode(), self.__currTime.encode(), hashlib.sha1).hexdigest()
        pos = self.__hexDict[hashCode[-1]]
        encryptionCode = hashCode[pos*2:pos*2+(4*2)]
        encryptionNum = self.hexstr2int(encryptionCode)
        tempCode = str(encryptionNum % 10**self.__codeLength)
        finalCode = "0"*(self.__codeLength - len(tempCode)) + tempCode

        return finalCode
        
        
    def run(self):

        while True:
            self.__preCode = self.__currCode
            self.__currCode = self.process()
            time.sleep(10)
            self.__preCode = None
            time.sleep(20)

    def getPreCode(self) -> str:
        return self.__preCode

    def getCurrCode(self) -> str:
        return self.__currCode

if __name__ == "__main__":
    t = TOTP("123", 6)
    while True:
        print(t.process())
        time.sleep(1)