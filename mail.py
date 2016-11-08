
import pygame
from imapclient import IMAPClient
from config import *
import time
import RPi.GPIO as GPIO

# !/usr/bin/env python

DEBUG = True

# Stuurt de GPIO voor de lampjes aan.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# Deze loop haalt om de zoveel tijd bij of er mailtjes binnen komen.
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

    if countemails > NEWMAIL_OFFSET:
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED,True)
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/victory-sound.mp3")
        pygame.mixer.music.play()

        MAIL_CHECK_FREQ = 0
        while pygame.mixer.music.get_busy() == True:
            continue
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
