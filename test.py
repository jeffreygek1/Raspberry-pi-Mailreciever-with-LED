import imaplib

M = imaplib.IMAP4_SSL("imap.gmail.com")
M.login("hogeschoolutrechtmail@gmail.com", "raspberry")
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print ('Message %s\n%s\n' % (num, data[0][1]))
M.close()
M.logout()

# lees de header van de afzender (Stefan)

#de 'afzender', de 'tijd' en de 'Message ID' uitlezen
def leesHeader():


    return

leesHeader()

def CSVschrijven(CSVbestand, afzender, tijd, messageID):

    # de message ID is hetzelfde
    if not messageID in CSVbestand:
        with open(CSVbestand, 'a', newline='') as CSVbestand:
            CSVSchrijven = csv.writer(CSVbestand, delimiter=';')
            CSVSchrijven.writerow((afzender, tijd, messageID))

    return # voor de sier

CSVschrijven('CSVEmails.csv', Afzender, Tijd, MessageID)

# # Bepaalt of het een nieuwe email is
# def CSVlezen(CSVbestand):
#
#     with open() as CSVbestand
#
#     return

