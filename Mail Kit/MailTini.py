import smtplib
fromaddr = 'tienerschoolnut@gmail.com'
toaddrs  = 'tsterenborg@odysseescholen.nl'
msg = 'hallo indy dit is een test door imsg'
username = 'tienerschoolnut@gmail.com'
password = '***'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
