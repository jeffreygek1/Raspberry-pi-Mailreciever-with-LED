
import RPi.GPIO as GPIO
from config import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(BUTTON_mute, GPIO.IN)
GPIO.setup(BUTTON_unmute, GPIO.IN)

while True:
	if GPIO.input(BUTTON_mute):
		GPIO.output(YELLOW_LED,True)
	else :
		GPIO.output(YELLOW_LED,False)
    if GPIO.input(BUTTON_unmute):
        GPIO.output(YELLOW_LED, True)
    else:
        GPIO.output(YELLOW_LED, False)