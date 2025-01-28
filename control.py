'''
Author: cairq cairq@tongbaninfo.com
Date: 2025-01-17 23:50:36
LastEditors: cairq cairq@tongbaninfo.com
LastEditTime: 2025-01-18 13:52:26
FilePath: \pi_car\control.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import RPi.GPIO as GPIO
import time

def move_forward():
  print('move_forward')
  GPIO.cleanup()
  time.sleep(0.1)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(21,GPIO.OUT)
  GPIO.setup(16,GPIO.OUT)
  GPIO.output(21,GPIO.LOW)
  GPIO.output(16,GPIO.LOW)

def move_backward():
  print('move_backward')
  GPIO.cleanup()
  time.sleep(0.1)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(20,GPIO.OUT)
  GPIO.setup(12,GPIO.OUT)
  GPIO.output(20,GPIO.LOW)
  GPIO.output(12,GPIO.LOW)

def turn_left():
  print('turn_left')
  GPIO.cleanup()
  time.sleep(0.1)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(16,GPIO.OUT)
  GPIO.output(16,GPIO.LOW)

def turn_right():
  print('turn_right')
  GPIO.cleanup()
  time.sleep(0.1)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(21,GPIO.OUT)
  GPIO.output(21,GPIO.LOW)

def turn_stop():
  print('turn_stop')
  time.sleep(0.1)
  GPIO.cleanup()