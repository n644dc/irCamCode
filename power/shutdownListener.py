#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

try:
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.wait_for_edge(3, GPIO.FALLING)
finally:  
    GPIO.cleanup()

subprocess.call(['shutdown', '-h', 'now'], shell=False)


