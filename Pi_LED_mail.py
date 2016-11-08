import pygame
from imapclient import IMAPClient
from config import *
import time
import RPi.GPIO as GPIO

# !/usr/bin/env python

DEBUG = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def loop():
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)

    print('Logging in as ' + USERNAME)
    select_info = server.select_folder(MAILBOX)
    print('%d messages in INBOX' % select_info['EXISTS'])

    folder_status = server.folder_status(MAILBOX, 'UNSEEN')
    countemails = int(folder_status['UNSEEN'])

    print
    "You have", countemails, "new emails!"
    def Mailrecieved():
        countemails = int(folder_status['UNSEEN'])
        if countemails == 0:
            return 0
        else:
            return 1

    if countemails > NEWMAIL_OFFSET:
        while True:
            GPIO.output(GREEN_LED, True)
            time.sleep(0.15)
            GPIO.output(GREEN_LED, False)
            time.sleep(0.15)
            if Mailrecieved() == 0:
                break
    else:
        GPIO.output(GREEN_LED, False)
        GPIO.output(RED_LED, True)

    time.sleep(MAIL_CHECK_FREQ)


try:
    print
    'Press Ctrl-C to quit.'
    while True:
        loop()

finally:
    GPIO.cleanup()

