from datetime import timedelta



# email code generator
EMAIL_VERIFY_CODE_TIME = timedelta(days=0, hours=0, minutes=30, seconds=0)
EMAIL_CODE_LENGTH = 4

# admin code generator
ENCRYP_KEY = "ACM of NPU"
ADMIN_CODE_LENGTH = 6

# trainning
MAX_VERIFY_TIME_GAP = timedelta(minutes=1) # 最大时间间隔
MAX_TRAINNING_TIME = timedelta(hours=7) # 最大单次训练时长

# http response
DEFAULT_RESPONSE_TEMPLATE = {
    "status": "", # ENUM("success", "error")
    "msg": "", # 响应详细信息，success对应ok，error对应响应的错误信息
    "data": {} # 如果响应需要返回数据则在data中添加
}

# email
SENDER = "admin@mail.orangej.xyz" # 发件人
DEFAULT_HOST = "localhost" # 发件HOST
DEFAULT_TEXT_TYPE = "plain" # 文本格式
DEFAULT_CODEC = "utf-8" # 文本编码方式

VERIFY_CODE_CONTEXT = "{}，您的验证码为{}，{}内有效。如果这并不是您本人的操作请忽略该邮件或马上联系管理员"