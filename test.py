import csv
import imaplib
import time
from email.parser import HeaderParser
from config import *

# lees de header van de afzender
# - de 'afzender' en de 'tijd' uitlezen
def leesHeader():

    mailserver = imaplib.IMAP4_SSL(HOSTNAME)
    mailserver.login(USERNAME, PASSWORD)
    mailserver.select(MAILBOX, readonly=True)

    typ, data = mailserver.search(None, 'UNSEEN')

    if typ == "OK":

        for num in data[0].split():
            mail = mailserver.fetch(num, '(BODY[HEADER])')

            parser = HeaderParser()
            msg = parser.parsestr(mail[1][0][1].decode("utf-8"))

            CSVschrijven(msg["From"], msg["Date"])
    else:
        print("Er is iets fout gegaan met het ophalen van de emails: "+typ)

    mailserver.close()
    mailserver.logout()

    return

# functie voor het schrijven naar het CSV bestand. Wordt later aangeroepen
def schrijven(afzender, tijd):
    with open(CSV_PATH, 'a', newline='') as CSVbestand:
        CSVSchrijven = csv.writer(CSVbestand, delimiter=',')
        CSVSchrijven.writerow((afzender, tijd))

    return

def CSVschrijven(afzender, tijd):

    # leest het csv bestand en schrijft in het CSV bestand
    with open(CSV_PATH, 'r', newline='') as CSVbestand:
        CSVlezen = csv.DictReader(CSVbestand)
        # stopt alle regels uit csv in een lijst met dictionaries
        csv_dictEmails = list(CSVlezen)

        # schrijft in de csv, als de afzender niet bestaat
        if not any(email['afzender'] == afzender for email in csv_dictEmails):
            #print('afzender false')
            schrijven('data/emails.csv', afzender, tijd)
            nieuweEmail()

        # schrijft in de csv, als de afzender al bestaat, maar de tijd anders is
        else:
            #print('afzender true')
            if not any(email['tijd'] == tijd for email in csv_dictEmails):
                schrijven('data/emails.csv', afzender, tijd)
                nieuweEmail()
                #print('tijd false')
            #else:
                #print('afzender true, tijd true')

    return

def nieuweEmail():
    print("Nieuwe email ontvangen!")

def mainLoop():

    while 1:

        leesHeader()

        time.sleep(REFRESHTIME)

    return



mainLoop()