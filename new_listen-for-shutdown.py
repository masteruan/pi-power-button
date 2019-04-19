#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.wait_for_edge(3, GPIO.FALLING)
input_state = GPIO.input(3)
if input_state == False:
  time.sleep(1)
  count = count + 1
else:
  count = 0
if count == 5:
  subprocess.call(['shutdown', '-h', 'now'], shell=False)
