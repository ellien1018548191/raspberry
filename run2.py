# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from sys import argv,exit
from PyQt5.QtWidgets import QApplication,QMainWindow
import icon_rc
import time
import cv2

import numpy as np
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)                  # 使用BCM编号方式  
GPIO.setup(26, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
  
  
  
  
# import smtplib#导入smtp模块
# import RPi.GPIO as GPIO
# #自己的qq邮箱
# QQMAIL_USER = '1018548191@qq.com'
# #smtp服务的授权码
# QQMAIL_PASS = 'bclftzcbtpipbccb'
# #smtp的服务类型，QQ，其他比如136邮箱可改成smtp.136.com,或者谷歌邮箱smtp.gmail.com
# SMTP_SERVER = 'smtp.qq.com'
# #这个端口一般没什么问题所有邮箱都是25，谷歌的587也可以
# SMTP_PORT = 25
# #接受者，
# recipient1='1018548191@qq.com'
# #邮件主题
# sub1 = 'fire'
# #邮件内容
# text1='Dormitory on fire'
# #发送函数，参数recipient是接受者了，subject是邮件主题，text是邮件内容
# def send_email(recipient,subject,text):
#     smtpserver = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
#     smtpserver.ehlo()
#     smtpserver.starttls()
#     smtpserver.ehlo
#     smtpserver.login(QQMAIL_USER,QQMAIL_PASS)
#     header = 'To:'+recipient+'\n'+'From:'+QQMAIL_USER
#     header = header + '\n' +'Subject:' + subject +'\n'
#     msg = header +'\n'+text+'\n\n'
#     smtpserver.sendmail(QQMAIL_USER,recipient,msg)
#     smtpserver.close()


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Qiao', 'Paula', 'Ilza', 'Z', 'W']
# Initialize and start realtime video capture

minW = 64.0
minH = 68.0
class Ui_MainWindow(object):
    def __init__(self, MainWindow):

        self.timer_camera = QtCore.QTimer() # 定时器
        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)
        self.cap = cv2.VideoCapture() # 准备获取图像
        self.CAM_NUM = 0
       
        self.slot_init() # 设置槽函数




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(765, 645)
        MainWindow.setMinimumSize(QtCore.QSize(765, 645))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/pic/pai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 50, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_open.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(12)
        self.pushButton_open.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/pic/g1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_open.setIcon(icon1)
        self.pushButton_open.setObjectName("pushButton_open")
        self.horizontalLayout.addWidget(self.pushButton_open)
        self.pushButton_take = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_take.sizePolicy().hasHeightForWidth())
        self.pushButton_take.setSizePolicy(sizePolicy)
        self.pushButton_take.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_take.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(12)
        self.pushButton_take.setFont(font)
        self.pushButton_take.setIcon(icon)
        self.pushButton_take.setObjectName("pushButton_take")
        self.horizontalLayout.addWidget(self.pushButton_take)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_close.setMaximumSize(QtCore.QSize(130, 40))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(12)
        self.pushButton_close.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/pic/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_face = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_face.sizePolicy().hasHeightForWidth())
        self.label_face.setSizePolicy(sizePolicy)
        self.label_face.setMinimumSize(QtCore.QSize(0, 0))
        self.label_face.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_face.setFont(font)
        self.label_face.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_face.setStyleSheet("background-color: rgb(192, 218, 255);")
        self.label_face.setAlignment(QtCore.Qt.AlignCenter)
        self.label_face.setObjectName("label_face")
        self.verticalLayout.addWidget(self.label_face)
        self.verticalLayout.setStretch(2, 5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qt-Camera （思绪无限）"))
        self.label.setText(_translate("MainWindow", "Qt Camera - WuXian"))
        self.pushButton_open.setToolTip(_translate("MainWindow", "点击打开摄像头"))
        self.pushButton_open.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButton_take.setToolTip(_translate("MainWindow", "点击拍照"))
        self.pushButton_take.setText(_translate("MainWindow", "拍照"))
        self.pushButton_close.setToolTip(_translate("MainWindow", "点击关闭摄像头"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭摄像头"))
        self.label_face.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/pic/Hint.png\"/><span style=\" font-size:28pt;\">点击打开摄像头</span><br/></p></body></html>"))


    def slot_init(self):
        # 设置槽函数
        self.pushButton_open.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.pushButton_close.clicked.connect(self.closeEvent)
        self.pushButton_take.clicked.connect(self.takePhoto)



    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(
                    self, u"Warning", u"请检测相机与电脑是否连接正确",
                    buttons=QtWidgets.QMessageBox.Ok,
                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)


    def show_camera(self):
        
        flag, self.image = self.cap.read()

        self.image=cv2.flip(self.image, 1) # 左右翻转
        
        
        gray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        GPIO.output(26, False)
        GPIO.output(16, False)
        GPIO.output(12, False)
        import bh1750   #光照强度小于10，led亮
        k=bh1750.getIlluminance()
        if k<10:
            GPIO.output(12, True)
        else:
            GPIO.output(12, False)
        
                
        for(x,y,w,h) in faces:

            cv2.rectangle(self.image, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            GPIO.output(16, False)

        # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                # print(id)
                GPIO.output(16, True)
                GPIO.output(26, True)
      
        
            
            
            
            elif(confidence > 100):
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
                # print(id)
                
        import mq7
        c,d=mq7.mq()   
        GPIO.output(26, False)
        if c=='Smoke!':
            # send_email(recipient1,sub1,text1)#调用函数
            GPIO.output(26, True)   
        import dht11    #温度大于1，风扇旋转
        a,b=dht11.DHT11()
        GPIO.output(24, False)
        if a>26:
            GPIO.output(24, True)    
        else:
            GPIO.output(24, False)    
        
            cv2.putText(self.image, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(self.image, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
            
            
             
            cv2.putText(self.image, 'Tem:'+str(a)+' Hum:'+str(b)+' '+str(c), (5,25), font, 1, (255,255,255), 2)  
            # w=id+' '+d
            # with open("1.txt","a") as f:
            #     f.writelines(w+'\n')
            
            import csv

# # 1. 创建文件对象
#             f1 = open('门禁.csv','a',encoding='utf-8')
#             f2 = open('温湿度.csv','a',encoding='utf-8')
            

# # 2. 基于文件对象构建 csv写入对象
#             csv_writer = csv.writer(f1)
#             csv_writer = csv.writer(f2)

# # 3. 构建列表头
#             csv_writer.writerow([id,d])
#             csv_writer.writerow([a,b,d])
            
# # 4. 写入csv文件内容
            

# # 5. 关闭文件
#             f1.close()
#             f2.close()
            
            
   #     cv2.imshow('camera',self.img)
        show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_face.setPixmap(QtGui.QPixmap.fromImage(showImage))
        self.label_face.setScaledContents(True)


    def takePhoto(self):
        if self.timer_camera.isActive() != False:
            now_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
            print(now_time)
            cv2.imwrite('pic_'+str(now_time)+'.png',self.image)

            cv2.putText(self.image, 'The picture have saved !',
                        (int(self.image.shape[1]/2-130), int(self.image.shape[0]/2)),
                        cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                        1.0, (255, 0, 0), 1)

            self.timer_camera.stop()

            show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # 左右翻转

            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.label_face.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.label_face.setScaledContents(True)



    def closeEvent(self):
        if self.timer_camera.isActive() != False:
            ok = QtWidgets.QPushButton()
            cacel = QtWidgets.QPushButton()

            msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")

            msg.addButton(ok,QtWidgets.QMessageBox.ActionRole)
            msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
            ok.setText(u'确定')
            cacel.setText(u'取消')

            if msg.exec_() != QtWidgets.QMessageBox.RejectRole:

                if self.cap.isOpened():
                    self.cap.release()
                if self.timer_camera.isActive():
                    self.timer_camera.stop()
                self.label_face.setText("<html><head/><body><p align=\"center\"><img src=\":/newPrefix/pic/Hint.png\"/><span style=\" font-size:28pt;\">点击打开摄像头</span><br/></p></body></html>")



if __name__ == '__main__':
    app = QApplication(argv)

    window = QMainWindow()
    ui = Ui_MainWindow(window)

    window.show()
    exit(app.exec_())
    GPIO.cleanup()
    
