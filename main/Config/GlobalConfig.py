from datetime import timedelta, datetime

urlCreator = "{}{}/"

# email验证码生成器参数
EMAIL_VERIFY_CODE_TIME = timedelta(days=0, hours=0, minutes=30, seconds=0)
EMAIL_CODE_LENGTH = 4

# admin验证码生成器参数
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

# email参数
SENDER = "admin@mail.orangej.xyz" # 发件人
DEFAULT_HOST = "localhost" # 发件HOST
DEFAULT_TEXT_TYPE = "plain" # 文本格式
DEFAULT_CODEC = "utf-8" # 文本编码方式
DEFAULT_TITLE = "ACM验证码" # 邮件主题
VERIFY_CODE_CONTEXT = "{}，您的验证码为{}，{}内有效。如果这并不是您本人的操作请忽略该邮件或马上联系管理员"

# 
DEFAULT_TIME = datetime.fromtimestamp(0)

# Session过期时间
# 当值为整数后，从设置开始计时，单位为秒，超时即过期
# 当值为datetime时，超过该日期即过期
# 当值为0时，关闭浏览器/断开连接即过期
# 当值为None时，依赖project/setting.py中SESSION_COOKIE_AGE参数的值
DEFAULT_ADMIN_EXPRIE_TIME_BROWSER = 0
DEFAULT_ADMIN_EXPRIE_TIME_MP = 7*24*3600
DEFAULT_USER_EXPRIE_TIME_BROWSER = 0
DEFAULT_USER_EXPRIE_TIME_MP = 7*24*3600

# 页面路由相关
ROOT_URL = None # 如 https://www.baidu.com/，最后一定要加/
UP_LAYER = ".." # 用于返回上一层
if ROOT_URL:
    BASE_API_URL = urlCreator.format(ROOT_URL, "api")
else:
    BASE_API_URL = urlCreator.format("../", "api")


