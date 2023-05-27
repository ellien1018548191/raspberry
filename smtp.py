# -*- coding: utf-8 -*-
import smtplib#导入smtp模块
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)                  # 使用BCM编号方式  
GPIO.setup(26, GPIO.OUT)
#自己的qq邮箱，如果你是136的话可以改成xxxxxx@136.com
QQMAIL_USER = '1018548191@qq.com'
#smtp服务的授权码，根据上面的操作就可以获得
QQMAIL_PASS = 'bclftzcbtpipbccb'
#smtp的服务类型，我的是QQ，其他比如136邮箱可改成smtp.136.com,或者谷歌邮箱smtp.gmail.com
SMTP_SERVER = 'smtp.qq.com'
#这个端口一般没什么问题所有邮箱都是25，谷歌的587也可以
SMTP_PORT = 25
#接受者，我这里是我自己
recipient1='1018548191@qq.com'
#邮件主题
sub1 = '11'
#邮件内容
text1='22'
#发送函数，参数recipient是接受者了，subject是邮件主题，text是邮件内容
def send_email(recipient,subject,text):
    smtpserver = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(QQMAIL_USER,QQMAIL_PASS)
    header = 'To:'+recipient+'\n'+'From:'+QQMAIL_USER
    header = header + '\n' +'Subject:' + subject +'\n'
    msg = header +'\n'+text+'\n\n'
    smtpserver.sendmail(QQMAIL_USER,recipient,msg)
    smtpserver.close()
    
import mq7
c,d=mq7.mq()   
GPIO.output(26, False)
if c=='Smoke!':
    send_email(recipient1,sub1,text1)#调用函数
    GPIO.output(26, True) 

    
GPIO.cleanup()