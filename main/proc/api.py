import base64

from datetime import timedelta
from datetime import datetime
from django.http.response import JsonResponse, HttpResponse, HttpResponseNotFound

from main.utils.QRCode import getQRCode
from main.utils.MD5 import getMD5
from main.utils.ACM.ACM import ACMUser, TrainningRecord
from main.utils.DAO.DAO import DAOForUser, DAOForTrainRecord

MAX_TIME_GAP = timedelta(minutes=1) # 最大时间间隔
MAX_TRAINNING_TIME = timedelta(hours=7) # 最大单次训练时长

DEFAULT_RESPONSE_TEMPLATE = {
    "status": "", # ENUM("success", "error")
    "msg": "", # 响应详细信息，success对应ok，error对应响应的错误信息
    "data": {} # 如果响应需要返回数据则在data中添加
}

# session检查
def checkSession(request) -> bool:
    flag = True

    if not request.session.exists(request.session.session_key): # session存在
        flag = False
    elif request.POST["username"] != request.session["username"]: # 操作本人
        flag = False
    elif not request.session["isLogin"]: # 已登录
        flag = False

    return flag

# 登录
def login(request) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE

    username = request.POST["username"]
    password = request.POST["password"]
    
    request.session["username"] = username
    request.session["isLogin"] = False
    request.session["admin"] = False
    
    try:
        user = DAOForUser.getUserByUsername(username)

        if user == None:
            raise Exception("用户不存在")
        if user.getPassword() != password:
            raise Exception("密码错误")

        if user.getAdmin():
            request.session["admin"] = True

        request.session["isLogin"] = True

        response["status"] = "success"
        response["msg"] = "登录成功"
        response["data"] = {
            "username" : user.getUsername(),
            "admin" : user.getAdmin(),
            "sessionId": request.session.session_key,
        }

    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)

    return JsonResponse(response)

def logout(request) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE
    response["status"] = "success"
    response["msg"] = "ok"    
    return JsonResponse(response)

# 获取签到二维码
def getCode(request) -> HttpResponse:
    try:
        if not checkSession(request):
            raise Exception("请先登录")

        if not request.session.get("admin"):
            raise Exception("您不是管理员，请使用管理员账号登录")

        csrf_token = request.META["CSRF_COOKIE"]
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        verifyToken = getMD5(base64.b64encode(time.encode()).decode())

        data = {
            "csrf_token": csrf_token,
            "token" : verifyToken,
            "time": time
        }
        
        imgBytes = getQRCode(str(data))
        return HttpResponse(imgBytes)
    except Exception as e:
        response = {
            "status": "error",
            "msg": str(e)
        }
        return  HttpResponseNotFound(str(response).encode())

# 签到/签退
def signIn(request) -> JsonResponse:

    response = DEFAULT_RESPONSE_TEMPLATE

    vToken = request.POST["token"]
    vTime = request.POST["time"]
    info = request.POST["info"]
    
    cToken = getMD5(base64.b64encode(vTime.encode()).decode())
    cTime = datetime.now()
    gap = cTime - datetime.strptime(vTime, "%Y%m%d%H%M%S")

    try:
        if not checkSession(request):
            raise Exception("请先登录")

        user = DAOForUser.getUserByUsername(info["username"])

        if user == None:
            raise Exception("用户不存在")
        if user.getPassword() != info["password"]:
            raise Exception("用户身份验证失败")
        if vToken != cToken or gap > MAX_TIME_GAP:
            raise Exception("打卡信息校验失败")
           
        # 如果在训练
        if user.getIsTrainning():
            user.setIsTrainning(False)

            record = DAOForTrainRecord.getTrainRecordById(user.getCurrRecordId())
            record.setEndTime(datetime.now())
            timeLength = record.getEndTime()-record.getStartTime()
            record.setTimeLength = str(round(timeLength.total_seconds()))

            # 如果训练超时
            if timeLength > MAX_TRAINNING_TIME:         
                record.setValid(False)
                record.setIsRecord(False)
                status = "error"
                msg = "单次训练时间超过7个小时，不计入总训练时间"
                data = {}

            # 如果训练未超时
            else:
                user.setAllTrainningTime(str(eval(user.getAllTrainningTime())+eval(record.getTimeLength())))
                record.setValid(True)
                record.setIsRecord(True)

                status = "success"
                msg = "签退成功"
                data = {
                    "trainningTime" : timeLength.total_seconds(),
                }
            
            DAOForTrainRecord.updateRecordById(record)
                
        # 如果未在训练
        else:
            user.setIsTrainning(True)

            newRecord = TrainningRecord(username=user.getUsername(), startTime=datetime.now())
            id = DAOForTrainRecord.addTrainRecord(newRecord)
            user.setCurrRecordId(str(id))
            
            

            status = "success"
            msg = "签到成功"
            data = {
                "startTime" : newRecord.getStartTime().strptime("%Y%m%d%H%M%S")
            }
        
        DAOForUser.updateUserInfoByUsername(user)
        
        response["status"] = status
        response["msg"] = msg
        response["data"] = data

    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)
    return JsonResponse(response)

def register(request) -> JsonResponse:

    response = DEFAULT_RESPONSE_TEMPLATE

    username = request.POST["username"]
    password = request.POST["password"]
    name = request.POST["name"]
    department = request.POST["department"]
    major = request.POST["major"]
    joinTime = request.POST["joinTime"]
    verify = request.POST["verify"]
    admin = request.POST["admin"]
    email = request.POST["email"]

    try:
        # 管理员验证码生成方式待考虑
        # if not verify == ???:
        #     raise Exception("管理员验证码错误")
        

        pass
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)

def getUserInfo(request) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE

    try:
        if not checkSession(request):
            raise Exception("请先登录")


        username = request.session.get("username")
        user = DAOForUser.getUserByUsername(username)
        if user != None:
            response["status"] = "success"
            response["msg"] = "ok"
            response["data"] = user.getDict()
        else:
            raise Exception("用户不存在")
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)
    
    return JsonResponse(response)

def getRecord(request) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE
    response["data"] = {
        "records" : []
    }

    try:
        if not checkSession(request):
            raise Exception("请先登录")
        
        username = request.session.get["username"]
        records = DAOForTrainRecord.getTrainRecordByUsername(username)
        response["status"] = "success"
        response["msg"] = "ok"
        response["data"] = {
            "records" : records
        }
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)

    return JsonResponse(response)


def getAll(request) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE
    response["data"] = {
        "records" : []
    }

    try:
        if not checkSession(request):
            raise Exception("请先登录")
        if not request.session.get("admin"):
            raise Exception("您不是管理员，请使用管理员账号登录")
        

        users = DAOForUser.getAll()
        response["status"] = "success"
        response["msg"] = "ok"
        response["data"] = {
            "users" : users
        }
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)

    return JsonResponse(response)





