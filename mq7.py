#!/usr/bin/python
#encoding:utf-8

import RPi.GPIO as GPIO
import time

HC_SR501 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(HC_SR501,GPIO.IN)
GPIO.setup(16,GPIO.OUT)

def mq():

    if(GPIO.input(HC_SR501) == True):
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" 无情况 ")
        a='no smoke'
        b=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        print(b)
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"  警告!")
        b=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        a='Smoke!'
    return a,b
    #time.sleep(1)


