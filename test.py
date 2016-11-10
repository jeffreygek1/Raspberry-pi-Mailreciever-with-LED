import csv
import imaplib
import time
from email.parser import HeaderParser
from config import *
import pygame
import RPi.GPIO as GPIO
import os

# lees de header van de afzender
# - de 'afzender' en de 'tijd' uitlezen
def leesHeader():

    # Maak de verbinding met de mail server
    mailserver = imaplib.IMAP4_SSL(HOSTNAME)
    mailserver.login(USERNAME, PASSWORD)
    mailserver.select(MAILBOX, readonly=True)

    # Haal alle emails op die nog niet gelezen zijn
    typ, data = mailserver.search(None, 'UNSEEN')

    # Check of de verbinding is gelukt
    if typ == "OK":

        for num in data[0].split():
            mail = mailserver.fetch(num, '(BODY[HEADER])')

            parser = HeaderParser()
            msg = parser.parsestr(mail[1][0][1].decode("utf-8"))

            # Roep csvCheck aan met de afzender en datum/tijd
            csvCheck(msg["From"], msg["Date"])
    else:
        print("Er is iets fout gegaan met het ophalen van de emails: "+typ)

    # Sluit de mail verbinding
    mailserver.close()
    mailserver.logout()

    return

# functie voor het schrijven naar het CSV bestand. Wordt later aangeroepen
def schrijven(afzender, tijd):

    # Open het CSV bestand en schrijf hier de juiste data in weg
    with open(CSV_PATH, 'a', newline='') as CSVbestand:
        CSVSchrijven = csv.writer(CSVbestand, delimiter=',')
        CSVSchrijven.writerow((afzender, tijd))

    return

# Check of de email al bestaat in het CSV bestand
def csvCheck(afzender, tijd):

    # leest het csv bestand en schrijft in het CSV bestand
    with open(CSV_PATH, 'r', newline='') as CSVbestand:
        CSVlezen = csv.DictReader(CSVbestand)
        # stopt alle regels uit csv in een lijst met dictionaries
        csv_dictEmails = list(CSVlezen)

        # schrijft in de csv, als de afzender niet bestaat
        if not any(email['afzender'] == afzender for email in csv_dictEmails):
            #print('afzender false')
            schrijven(afzender, tijd)
            nieuweEmail()

        # schrijft in de csv, als de afzender al bestaat, maar de tijd anders is
        else:
            #print('afzender true')
            if not any(email['tijd'] == tijd for email in csv_dictEmails):
                schrijven(afzender, tijd)
                nieuweEmail()

    return

# Wordt aangeroepen op het moment dat er een nieuwe email binnen komt
def nieuweEmail():

    print("Nieuwe email ontvangen!")
    GPIO.output(YELLOW_LED, True)
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/victory-sound.mp3")
    pygame.mixer.music.play()
    for i in range(0, 20):
        GPIO.output(YELLOW_LED, True)
        time.sleep(0.15)
        GPIO.output(YELLOW_LED, False)
        time.sleep(0.15)
        if GPIO.input(BUTTON_mute) == True:
            print("mute")
            os.system("amixer set PCM -- 0%")
        if GPIO.input(BUTTON_unmute) == True:
            print("unmute")
            os.system("amixer set PCM -- 100%")

    return

# Mainloop van het programma
def mainLoop():

    print("Druk op CTRL+C om te stoppen!")

    while 1:

        leesHeader()

        time.sleep(REFRESHTIME)

    return


# Start de mainloop
mainLoop()
