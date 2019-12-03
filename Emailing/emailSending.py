import smtplib

#domian email server and port number
conn = smtplib.SMTP('smtp.gmail.com', 587)

#start the connection to server. Hello method
conn.ehlo()
#start tls begin encryption
conn.starttls()

#pass login credentials
conn.login('name@gmail.com', 'password')
#sendmail (from address, to address, email body)
conn.sendmail('name@gmail.com', 'name@gmail.com', 'Subject:python test\n\nDear Kevin,\nHello World.\n')


#after sending disconnect
conn.quit()