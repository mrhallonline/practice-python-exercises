import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

conn.login('emailaddress', 'password')

#select a folder and only for reading
conn.select_folder('INBOX', readonly=True)

#find emails
UIDs = conn.search(['SINCE 20-Aug-2015'])
#list of UIDs
UIDs
#fetch by UID
rawMessage = conn.fetch([47474], ['BODY[]', 'FLAGS'])
#parse email
import pyzmail36
message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
#get subject
message.get_subject()
#get sender
message.get_addresses('from')
#get body of email
message.text_part.get_payload().decode('UTF-8')

#logout when finished
conn.logout()

#lists all you email folders 3rd tuple
conn.list_folders()