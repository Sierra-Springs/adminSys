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
from fctmail import *
import os  # NL : for env var


def alerte():
    ct=0
    html=""
    st='<div class="item cert-alert open">'+"\n"
    target=bytes(st, 'utf-8')
    with urllib.request.urlopen("https://www.cert.ssi.gouv.fr/") as url:
        for line in url:
            if line==target:
                ct=20
            if ct>11:
                html=html+line.decode("utf-8")
            if ct==10:
                break
            ct=ct-1
    alert=[]
    date=False
    i=0
    mot=""
    while date==False:
        if (html[i]==">"):
            if mot=='class="item-date"':
                date=True
                i=i+1
                mot=""
                while html[i]!="<":
                    mot=mot+html[i]
                    i=i+1
                alert.append(mot)
        while (html[i]==" ") :
            mot=""
            i=i+1
        mot=mot+html[i]
        i=i+1
    titre=False
    i=0
    mot=""
    while titre==False:
        if (html[i]==">"):
            if mot=='class="item-title"':
                titre=True
                i=i+1
                while html[i]!=">":
                    i=i+1
                mot=""
                i=i+1
                while html[i]!="<":
                    mot=mot+html[i]
                    i=i+1
                alert.append(mot)
        while (html[i]==" ") :
            mot=""
            i=i+1
        mot=mot+html[i]
        i=i+1
    lien=False
    i=0
    mot=""
    while lien==False:
        if (html[i]==" "):
            if mot=='class="item-link"':
                lien=True
                i=i+1
                while html[i]!="/":
                    i=i+1
                mot=""
                while html[i]!='"':
                    mot=mot+html[i]
                    i=i+1
                alert.append(mot)
        while (html[i]==" ") :
            mot=""
            i=i+1
        mot=mot+html[i]
        i=i+1
    return alert

def recupalerte(l):
    test=True
    print(os.environ['Stockage']+'/alerte.txt')
    fic = open(os.environ['Stockage']+'/alerte.txt', 'r')  # NL (env var added otherwise : "alert.txt not found")
    anc=[]
    for line in fic:
        anc.append(line)
    if len(anc)==3:
        for i in range (2):
            if anc[i]!=l[i]:
                test=False
    fic.close()
    return test

def faillemail(alert):
    mail=[]
    mail.append("Alerte : "+liste[0]+ " : "+liste[1])
    mail.append("Alerte datant du "+liste[0]+" affectant "+liste[1]+". En savoir plus : "+liste[2])
    return mail

def faille():
    t=alerte()
    print(t)
    bool=recupalerte(t)
    if bool==True:
        print("alerte non traite")
        fic = open(os.environ['Stockage']+'/alerte.txt', 'a')
        fic.write(t[0]+"\n")
        fic.write(t[1]+"\n")
        fic.write(t[2]+"\n")
        fic.close()
        m=faillemail(t)
        mail(m)
    else :
        print("alerte deja traite")

    #mail()
#import platform
#import os
#import sys
#
#print sys.platform()
#print os.name
#print platform.platform()
#print platform.uname()
