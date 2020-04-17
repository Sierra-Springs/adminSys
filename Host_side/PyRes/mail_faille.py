#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mail_faille.py
#


#from sonde import *
#from stockage import *
#from suppression_ancienne import *
#import os
#import sys

import time
import urllib.request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail():
    exp="bert.audran@gmail.com"
    dest="nathanael-1999@hotmail.fr"
    sub="Alerte sécurite!"
    mdp="lol"
    msg=MIMEMultipart()
    msg['From']=exp
    msg['To']=dest
    msg['Subject']=sub
    txt="Ce mail a été envoyé dans le cadre du projet d'admin sys pour tester l envoie des mails"
    msg.attach(MIMEText(txt))
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.starttls()
    mail.login(exp, mdp)
    mail.sendmail(exp, dest, msg.as_string())
    mail.quit()
    print("Mail envoyé")

def alerte():
    ct=0
    alert=""
    target="b'"+'<div class="item cert-alert open">'+chr(92)+"n'"

    with urllib.request.urlopen("https://www.cert.ssi.gouv.fr/") as url:
        for line in url:
            ct=ct+1
            if ct==132:
                print(line)
            if line==target:
                print("yes")
    print(alert)
    print(target)
    return True

def recupalerte():
    return 0

t=alerte()
if (t==True):
    recupalerte()
    #mail()
#import platform
#import os
#import sys
#
#print sys.platform()
#print os.name
#print platform.platform()
#print platform.uname()
