#!/usr/bin/env python
from subprocess import Popen, PIPE
import RPi.GPIO as GPIO
from threading import Thread
import os
import time
import CameraRunnerThread

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

cameraOn = False
camera = CameraRunnerThread.CameraRunner()

def turnCameraOn():
  camera.start()
  
def turnCameraOff():
  camera.join()
  fileName = camera.fileName
  camPath = os.path.join(camera.fileDir, camera.fileName)
  print "converting to MP4 " + camPath
  cmd = "MP4Box -add " + camPath + ".h264 " + camPath + ".mp4"
  out, err = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).communicate()
  print out + " __--__ Error: " + err
  os.remove(camPath + ".h264")
  print "Conversion Completed, Video Saved."

def getCameraState():
  time.sleep(2)
  on = False
  if GPIO.input(26):
    on = True
  return on
  
def changeCameraState(camState):
  if camState:
    print "Starting Cam..."
    turnCameraOn()
    GPIO.output(20,GPIO.HIGH)
  else:
    print "Stopping Cam..."
    turnCameraOff()
    GPIO.output(20,GPIO.LOW)

    
try:
  while True:
    # print "Check Switch"
    cameraRunning = getCameraState()
    if cameraRunning == cameraOn:
      continue
    else:
      cameraOn = cameraRunning
      changeCameraState(cameraOn)
finally:
  GPIO.cleanup()