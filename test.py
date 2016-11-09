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

#de 'afzender', de 'tijd' en de 'Message ID' uitlezen
def leesHeader():


    return

leesHeader()

# functie voor het schrijven naar het CSV bestand. Wordt later aangeroepen
def schrijven(CSVbestand, afzender, tijd, messageID):
    with open(CSVbestand, 'a', newline='') as CSVbestand:
        CSVSchrijven = csv.writer(CSVbestand, delimiter=',')
        CSVSchrijven.writerow((afzender, tijd, messageID))

    return

def CSVschrijven(CSVbestand, afzender, tijd, messageID):

    # leest het csv bestand en schrijft in het CSV bestand
    # tempDict = {}
    with open(CSVbestand, 'r', newline='') as CSVbestand:
        CSVlezen = csv.DictReader(CSVbestand)
        for regel in CSVlezen:
            values = regel.values()

        if not messageID == regel.values():
            print(messageID)
            schrijven('data/emails.csv', afzender, tijd, messageID)

        # for i in regel.values():
        #     if messageID == i:
        #         print(i)
        #         print(messageID)
        #         schrijven('data/emails.csv', afzender, tijd, messageID)
        #         break


    return # voor de sier

Afzender = 'blub'
Tijd = '124113'
MessageID = 'uhw4n0t87gon75hmgevnob56uytwhgyu5hmoevn5tirujfcmgvy56kufo84vyc 4v6iyfcmnrvdtgf'

CSVschrijven('data/emails.csv', Afzender, Tijd, MessageID)