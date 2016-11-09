# import imaplib
import csv

# M = imaplib.IMAP4_SSL("imap.gmail.com")
# M.login("hogeschoolutrechtmail@gmail.com", "raspberry")
# M.select()
# typ, data = M.search(None, 'ALL')
## for num in data[0].split():
#     typ, data = M.fetch(num, '(RFC822)')
#     print ('Message %s\n%s\n' % (num, data[0][1]))
# M.close()
# M.logout()

# lees de header van de afzender (Stefan)
# - de 'afzender', de 'tijd' en de 'Message ID' uitlezen
def leesHeader():


    return

leesHeader()

# functie voor het schrijven naar het CSV bestand. Wordt later aangeroepen
def schrijven(CSVbestand, afzender, tijd):
    with open(CSVbestand, 'a', newline='') as CSVbestand:
        CSVSchrijven = csv.writer(CSVbestand, delimiter=',')
        CSVSchrijven.writerow((afzender, tijd))

    return

def CSVschrijven(CSVbestand, afzender, tijd):

    # leest het csv bestand en schrijft in het CSV bestand
    with open(CSVbestand, 'r', newline='') as CSVbestand:
        CSVlezen = csv.DictReader(CSVbestand)
        # stopt alle regels uit csv in een lijst met dictionaries
        csv_dictEmails = list(CSVlezen)

        print(csv_dictEmails)


        while True:
            # schrijft in de csv, als de afzender niet bestaat
            if not any(email['afzender'] == afzender for email in csv_dictEmails):
                print('afzender false')
                schrijven('data/emails.csv', afzender, tijd)
                break

            # schrijft in de csv, als de afzender al bestaat, maar de tijd anders is
            elif any(email['afzender'] == afzender for email in csv_dictEmails):
                print('afzender true')
                if not any(email['tijd'] == tijd for email in csv_dictEmails):
                    schrijven('data/emails.csv', afzender, tijd)
                    print('tijd false')
                else:
                    print('afzender true, tijd true')
                break

    return

Afzender = 'blub'
Tijd = '17:05:00'

CSVschrijven('data/emails.csv', Afzender, Tijd)