
# ----------------------
# 数据API
#
# ----------------------


import base64
import re

from datetime import datetime

from django.http import HttpRequest
from django.http.response import (HttpResponse, 
                                  HttpResponseRedirect,
                                  HttpResponseNotFound,
                                  JsonResponse)
from django.middleware import csrf

from DK import static  # 加载生成器
# from main.proc.getPage import getLoginPage
from main.Config.GlobalConfig import (DEFAULT_RESPONSE_TEMPLATE,
                                      EMAIL_VERIFY_CODE_TIME,
                                      MAX_TRAINNING_TIME, 
                                      MAX_VERIFY_TIME_GAP,
                                      VERIFY_CODE_CONTEXT,
                                      DEFAULT_TITLE,
                                      DEFAULT_ADMIN_EXPRIE_TIME_BROWSER,
                                      DEFAULT_USER_EXPRIE_TIME_BROWSER,
                                      DEFAULT_ADMIN_EXPRIE_TIME_MP,
                                      DEFAULT_USER_EXPRIE_TIME_MP)
from main.utils.ACM.ACM import ACMUser, TrainningRecord
from main.utils.DAO.DAO import DAOForTrainRecord, DAOForUser
from main.utils.Mail import SendMail
from main.utils.MD5 import getMD5
from main.utils.QRCode import getQRCode

# session检查
def checkSession(request: HttpRequest) -> bool:
    if request.session.exists(request.session.session_key) and request.session["isLogin"]: # 已登录
        return True
    else:
        return False

# 管理员检查
def checkAdmin(request: HttpRequest) -> bool:
    if request.session.get("admin"):
        return True
    else:
        return False

# 检查来源是否为小程序
def checkFromMP(request: HttpRequest) -> bool:
    MPRegex = "miniProgram"
    ua = request.headers["User-Agent"]
    if ua.find(MPRegex) == -1:
        return False
    else:
        return True

# 清除过期session
def clearSession(request: HttpRequest):
    request.session.clear_expired()

# ------------------------------

# 用户名检验，用户名唯一
# POST
def checkUsername(request: HttpRequest) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE

    try :
        username = request.POST.get("username")
        usable = True

        if not username:
            raise Exception("用户名不可用")

        user = DAOForUser.getUserByUsername(username)
        if user:
            usable = False

        response["status"] = "success"
        response["msg"] = "ok"
        response["data"] = {
            "usable" : usable
        }
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)
        response["data"] = {}
    
    return JsonResponse(response)

# 邮箱验证码
# POST
def getEmailCode(request: HttpRequest) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE
    emailRegex = r"[-_\w\.]{0,64}@[-\w]{1,63}\.*[-\w]{1,63}"

    try:
        username = request.POST.get("username")
        email = request.POST.get("email")

        if username == None:
            pass
            # raise Exception("请输入用户名")

        if not len(re.findall(emailRegex, email)):
            raise Exception("请输入格式正确的邮箱")

        code = static.EMAIL_CODE.getCode()
        print(code)
        validTime = EMAIL_VERIFY_CODE_TIME.total_seconds() % 60
        context = VERIFY_CODE_CONTEXT.format(username, code, validTime)

        temp = SendMail(receiver=email, receiverName=username, title=DEFAULT_TITLE, mailContext=context)
        # temp.start()
        temp.run()

        response["status"] = "success"
        response["msg"] = "ok"

    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)

    response["data"] = {}
    return JsonResponse(response)

# 注册
# POST
def register(request: HttpRequest) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE

    clearSession(request)

    try:
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get("name")
        department = request.POST.get("department")
        major = request.POST.get("major")
        joinTime = request.POST.get("joinTime")
        adminVerify = request.POST.get("adminVerify")
        admin = request.POST.get("admin")
        email = request.POST.get("email")
        emailVerify = request.POST.get("emailVerify")

        # 邮箱验证
        if not static.EMAIL_CODE.checkCode(emailVerify):
            raise Exception("邮箱验证码出错")

        # 管理员验证码验证
        if admin:
            admin = True
            if not (adminVerify == static.ADMIN_CODE.getCurrCode() or adminVerify == static.ADMIN_CODE.getPreCode()):
                raise Exception("管理员验证码错误")
        else:
            admin = False

        user = ACMUser(username=username, passhash=getMD5(password), name=name, department=department, major=major, joinTime=joinTime, admin=admin, email=email)
        userId = DAOForUser.addUser(user)

        response["status"] = "success"
        response["msg"] = "ok"
        response["data"] = {
            "userId" : userId
        }
        
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)
        response["data"] = {}
    
    return JsonResponse(response)

# 登录
# POST
def login(request: HttpRequest) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE

    clearSession(request) # 先清除过期Session

    try:

        username = request.POST.get("username")
        password = request.POST.get("password")
        source = request.POST.get("from")
        
        if username == None or password == None:
            raise Exception("请检查账号或密码")

        if request.session.session_key == None:
            request.session.create()
        request.session["username"] = username
        request.session["isLogin"] = False
        request.session["admin"] = False

        user = DAOForUser.getUserByUsername(username)

        if user == None:
            raise Exception("用户不存在")
            
        if getMD5(password) != user.getPasshash():
            raise Exception("密码错误")

        if user.getAdmin():
            request.session["admin"] = True

        if source == "MP":
            if request.session["admin"]:
                request.session.set_expiry(DEFAULT_ADMIN_EXPRIE_TIME_MP)
            else:
                request.session.set_expiry(DEFAULT_USER_EXPRIE_TIME_MP)
        else:
            if request.session["admin"]:
                request.session.set_expiry(DEFAULT_ADMIN_EXPRIE_TIME_BROWSER)
            else:
                request.session.set_expiry(DEFAULT_USER_EXPRIE_TIME_BROWSER)

        request.session["isLogin"] = True

        response["status"] = "success"
        response["msg"] = "登录成功"
        response["data"] = {
            "username" : user.getUsername(),
            "admin" : user.getAdmin(),
            "sessionId": request.session.session_key,
        }

        # return HttpResponseRedirect("../")
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)
        response["data"] = {}

    return JsonResponse(response)
    # temp = JsonResponse(response)
    # temp.__setitem__("Access-Control-Allow-Origin", "*")
    # return temp

# 注销
# GET
def logout(request: HttpRequest) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE
    try:
        request.session.delete(request.session.session_key)
        clearSession(request)

        response["status"] = "success"
        response["msg"] = "ok"
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)
        
    response["data"] = {}

    return JsonResponse(response)
    # return HttpResponseRedirect("../")

# 获取签到二维码
# GET
def getCode(request: HttpRequest) -> HttpResponse:
    try:
        if not checkSession(request):
            # if checkFromMP(request):
            raise Exception("尚未登录")

        if not checkAdmin(request):
            raise Exception("您不是管理员，请使用管理员账号访问")
        
        csrf_token = csrf.get_token(request)
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
# POST
def signIn(request: HttpRequest) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE
    try:
        if not checkSession(request):
            # if checkFromMP(request):
            raise Exception("尚未登录")

        vToken = request.POST.get("token")
        vTime = request.POST.get("time")
        # info = request.POST.get("info")
        
        if not vTime or not vToken:
            raise Exception("参数不足")

        cToken = getMD5(base64.b64encode(vTime.encode()).decode())
        cTime = datetime.now()
        gap = cTime - datetime.strptime(vTime, "%Y%m%d%H%M%S")

        user = DAOForUser.getUserByUsername(request.session.get("username"))

        if user == None:
            raise Exception("用户不存在")
        if vToken != cToken or gap > MAX_VERIFY_TIME_GAP:
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
        response["data"] = {}

    return JsonResponse(response)

# 获取用户信息
# GET
def getUserInfo(request: HttpRequest) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE

    try:
        clearSession(request)
        if not checkSession(request):
            # if checkFromMP(request):
            raise Exception("尚未登录")
                
                

        username = request.session.get("username")
        user = DAOForUser.getUserByUsername(username)
        if user != None:
            response["status"] = "success"
            response["msg"] = "ok"
            response["data"] = user.getDict()
            response["data"]["isLogin"] = True
        else:
            raise Exception("用户不存在")
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)
        response["data"] = {}
    
    return JsonResponse(response)

# 获取用户训练记录
# GET
def getRecord(request: HttpRequest) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE
    response["data"] = {
        "records" : []
    }

    try:
        clearSession(request)
        if not checkSession(request):
            # if checkFromMP(request):
            raise Exception("尚未登录")
                
        username = request.session.get("username")
        records = DAOForTrainRecord.getTrainRecordByUsername(username)
        response["status"] = "success"
        response["msg"] = "ok"
        response["data"] = {
            "records" : [i.getDict() for i in records]
        }
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)
        response["data"] = {}

    return JsonResponse(response)

# 获取全体用户信息
# GET
def getAll(request: HttpRequest) -> JsonResponse:
    response = DEFAULT_RESPONSE_TEMPLATE
    response["data"] = {
        "records" : []
    }

    try:
        clearSession(request)
        if not checkSession(request):
            # if checkFromMP(request):
            raise Exception("尚未登录")
                
        if not checkAdmin(request):
            raise Exception("请使用管理员身份登录")

        users = DAOForUser.getAll()
        response["status"] = "success"
        response["msg"] = "ok"
        response["data"] = {
            "users" : [ i.getDict() for i in users]
        }
    except Exception as e:
        response["status"] = "error"
        response["msg"] = str(e)
        response["data"] = {}

    return JsonResponse(response)

