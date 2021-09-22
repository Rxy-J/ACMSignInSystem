import smtplib
import threading

from email.mime.text import MIMEText
from email.header import Header

from main.Config.GlobalConfig import SENDER, DEFAULT_HOST, DEFAULT_TEXT_TYPE, DEFAULT_CODEC

class SendMail(threading.Thread):
    def __init__(self, receiver: str, receiverName: str, title: str, mailContext: str, sender: str=SENDER, host: str=DEFAULT_HOST, textType: str=DEFAULT_TEXT_TYPE, codec: str=DEFAULT_CODEC) -> None:
        self.__host = host # host
        
        self.__sender = sender # 发件人
        self.__receiver = receiver # 收件人
        self.__receiverName = receiverName # 收件人姓名
        
        self.__title = title # 邮件题目
        self.__mailContext = mailContext # 邮件正文

        self.__textType = textType # 文本格式
        self.__codec = codec # 文本编码

    
    def run(self):
        message = MIMEText(self.__mailContext, self.__textType, self.__codec) # 正文
        message['From'] = u'<{0}>'.format(self.__sender)   # 发送者
        message['To'] =  u'{0}  <{1}>'.format(self.__receiverName, self.__receiver)  # 接收者    
        message['Subject'] = Header(self.__title, self.__codec).encode() # 标头
        
        
        try:
            smtpObj = smtplib.SMTP(self.__host)
            smtpObj.sendmail(self.__sender, self.__receiver, message.as_string())
            print ("邮件发送成功")
        except smtplib.SMTPException as e:
            print ("Error: 无法发送邮件")


