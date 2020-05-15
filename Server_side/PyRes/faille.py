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

def al(html):
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

def alerte():
	ct=0
	html=""
	st='<div class="item cert-alert open">'+"\n"
	target=bytes(st, 'utf-8')
	liste_alert=[]
	with urllib.request.urlopen("https://www.cert.ssi.gouv.fr/") as url:
			for line in url:
				if line==target:
					ct=20
				if ct>11:
					html=html+line.decode("utf-8")
				if ct==10:
					liste_alert.append(al(html))
					html=""
				ct=ct-1 
	return liste_alert

def recupalerte(l):
    test=False
    print(os.environ['Stockage']+'/alerte.txt')
    fic = open(os.environ['Stockage']+'/alerte.txt', 'r')  # NL (env var added otherwise : "alert.txt not found")
    #print('alerte.txt')
    #fic = open('alerte.txt', 'r') 
    anc=[]
    der=False
    for line in fic:
        anc.append(line)
    if len(anc)>=3:
        ct=2
        taille=len(anc)/3
        taille=int(taille)
        for j in range (0,taille):
            if ct==2 and anc[ct]!=l[0][2]+"\n":
                    der=True
            for i in range (0,len(l)):
                if anc[ct]!=l[i][2]+"\n":
                    test=True
            ct=ct+3
    else :
        test=True
        der=True
    fic.close()
    return test,der

def faillemail(liste):
    mail=[]
    mail.append("Alerte : "+liste[0]+ " : "+liste[1])
    mail.append("Alerte datant du "+liste[0]+" affectant "+liste[1]+". En savoir plus : "+liste[2])
    return mail

def faille():
    t=alerte()
    rd,der=recupalerte(t)
    if rd==True:
        print("changement des alertes")
        fic = open(os.environ['Stockage']+'/alerte.txt', 'w')
        #fic = open('alerte.txt', 'w')
        for i in range (0,len(t)):
            fic.write(t[i][0]+"\n")
            fic.write(t[i][1]+"\n")
            fic.write(t[i][2]+"\n")
        fic.close()
        if (der==True):
            print("nouvelle alerte")
            m=faillemail(t[0])
            fctmail(m)
    else :
        print("pas de changement")

#faille()
    #mail()
#import platform
#import os
#import sys
#
#print sys.platform()
#print os.name
#print platform.platform()
#print platform.uname()
