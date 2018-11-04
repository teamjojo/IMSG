import smtplib
fromaddr = 'tienerschoolnut@gmail.com'
toaddrs  = 'jojoosinga@gmail.com'
msg = 'hallo indy dit is een test door imsg'
username = 'tienerschoolnut@gmail.com'
password = 'J0r@n2006'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
