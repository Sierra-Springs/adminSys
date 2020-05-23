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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os  # NL : for env var

def fctmail(liste):
    sub=str(liste[0])
    txt=str(liste[1])
    exp="bert.audran@gmail.com"
    #dest="audran.bert@hotmail.fr"
    dest="nathanael-1999@hotmail.fr"
    mdp="lol"
    if (mdp!="lol"):
        msg=MIMEMultipart()
        msg['From']=exp
        msg['To']=dest
        msg['Subject']=sub
        msg.attach(MIMEText(txt))
        if len(liste)==4: #piece jointe
            fichier=str(liste[2])
            piece=open(str(liste[3]),"rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((piece).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "piece; filename= %s" % fichier)
            msg.attach(part)
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.starttls()
        mail.login(exp, mdp)
        mail.sendmail(exp, dest, msg.as_string())
        mail.quit()
        print("Mail envoyé")
    else :
        print("Pas de mot de passe pour envoyer le mail")

    #mail()
#import platform
#import os
#import sys
#
#print sys.platform()
#print os.name
#print platform.platform()
#print platform.uname()
