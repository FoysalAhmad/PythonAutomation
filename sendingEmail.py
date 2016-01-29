#!usr/bin/env

import smtplib, getpass

smtpObj = smtplib.SMTP('smtp-mail.outlook.com',587)
smtpObj.ehlo()
smtpObj.starttls()
passw = getpass.getpass()
#passw = raw_input()
smtpObj.login('foysal.eee.bd@outlook.com',passw)

smtpObj.sendmail('foysal.eee.bd@outlook.com','foysal.eee.bd@gmail.com','Subject: Testing again.\n')

{
'testing from python'
}

smtpObj.quit()

