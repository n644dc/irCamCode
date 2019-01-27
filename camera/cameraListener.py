#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

cameraOn = False

def turnCameraOn():
  print "Starting Cam..."

def getCameraState():
  sleep(2)
  on = False
  if GPIO.input(26):
    on = True
  return on
  
def changeCameraState(camState):
  if camState:
    turnCameraOn
  else:
    turnCameraOff

    
try:
  while True:
    print "Checking Cam"
    cameraRunning = getCameraState()
    if cameraRunning == cameraOn:
      print "Camera state has not changed. Doing Nothing."
    else:
      cameraOn = cameraRunning
      changeCameraState(cameraOn)
      
    
finally:
  GPIO.cleanup()


#subprocess.call(['shutdown', '-h', 'now'], shell=False)