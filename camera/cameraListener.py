#!/usr/bin/env python

import RPi.GPIO as GPIO
from threading import Thread
from time import sleep
import CameraRunnerThread

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

cameraOn = False
camera = CameraRunnerThread.CameraRunner()


def turnCameraOn():
  camera.start()
  
def turnCameraOff():
  camera.join()

def getCameraState():
  sleep(2)
  on = False
  if GPIO.input(26):
    on = True
  return on
  
def changeCameraState(camState):
  if camState:
    print "Starting Cam..."
    turnCameraOn()
  else:
    print "Stopping Cam..."
    turnCameraOff()

    
try:
  while True:
    print "Check Switch"
    cameraRunning = getCameraState()
    if cameraRunning == cameraOn:
      print "Camera state has not changed. Doing Nothing."
    else:
      cameraOn = cameraRunning
      changeCameraState(cameraOn)
finally:
  GPIO.cleanup()