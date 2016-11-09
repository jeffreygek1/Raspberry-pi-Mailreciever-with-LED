
import RPi.GPIO as GPIO
from config import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(BUTTON_mute, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	if GPIO.input(BUTTON_mute):
		GPIO.output(YELLOW_LED,True)
	else :
		GPIO.output(YELLOW_LED,False)