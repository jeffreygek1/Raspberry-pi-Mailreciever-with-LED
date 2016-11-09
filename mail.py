
import pygame
from imapclient import IMAPClient
from config import *
import time
import RPi.GPIO as GPIO
import os

# !/usr/bin/env python

DEBUG = True

# Stuurt de GPIO voor de lampjes aan.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BUTTON_mute, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_unmute, GPIO.IN, pull_up_down=GPIO.PUD_UP)
played = 0
def isplayed(r):
    if r == 0:
        global played
        played = 1
        return played
    if r == 1:
        global played
        played = 0
        return played

# Deze loop haalt om de zoveel tijd bij of er mailtjes binnen komen.
def loop():
    if GPIO.input(BUTTON_mute) == True:
        os.system("amixer set PCM -- 0%")
    if GPIO.input(BUTTON_unmute) == True:
        os.system("amixer set PCM -- 100%")

    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)
    print('Logging in as ' + USERNAME)
    select_info = server.select_folder(MAILBOX)
    print('%d messages in INBOX' % select_info['EXISTS'])

    folder_status = server.folder_status(MAILBOX, 'UNSEEN')

    countemails = int(folder_status['UNSEEN'])

    print("You have", countemails, "new emails!")
    print(countemails)
    print(NEWMAIL_OFFSET)

    if countemails > NEWMAIL_OFFSET:
        GPIO.output(RED_LED, False)
        for i in range(0, 101):
            GPIO.output(YELLOW_LED, True)
            time.sleep(0.15)
            GPIO.output(YELLOW_LED, False)
            time.sleep(0.15)
            if played == 0:
                GPIO.output(YELLOW_LED, True)
                pygame.mixer.init()
                pygame.mixer.music.load("sounds/victory-sound.mp3")
                pygame.mixer.music.play()
                isplayed(0)

            while pygame.mixer.music.get_busy() == True:
                continue
        MAIL_CHECK_FREQ = 0


    else:
        GPIO.output(YELLOW_LED, False)
        GPIO.output(RED_LED, True)

        MAIL_CHECK_FREQ = 15
        isplayed(1)

    time.sleep(MAIL_CHECK_FREQ)

try:
    print('Press Ctrl-C to quit.')
    while True:
        loop()

finally:
    GPIO.cleanup()
