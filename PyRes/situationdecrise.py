#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#
import sqlite3
import os
from graphique import *
from fctmail import *
from affichageterminal import *

ramtable=["ramTotal", "ramUsed", "ramFree", "ramShared", "ramBuffers", "ramCached"]
disktable=["total","used","free","percent"]
cputable=["freq","freqmin","freqmax","percent"]
proctable=["nbproc"]
userstable=["nbusers"]
tempstable=["date"]

#Critere situation de crise
tempscrise=10
ramcrise=100
cpucrise=95
diskcrise=95
#fin

def prepmailcrise(i,pc):
    liste=[]
    st="Probleme avec la "+i+"sur le pc"+pc
    liste.append(st)
    st="Probleme Critique avec la "+i+"sur le pc"+pc
    liste.append(st)
    return liste

def verificationcrise(bdd,verif,machine,nb):
    crise=False
    col=""
    if verif=="ram":
        col="ram.ramFree"
    elif verif=="disk":
        col="disk.percent"
    elif verif=="cpu":
        col="cpu.percent"
    add=0
    ct=0
    if nb==1:
        if verif=="disk" or verif=="cpu":
            add=95
        else :
            add=100
        ct=ct+1
        nbdd = os.environ['BDD_Path']
        bdd = sqlite3.connect(nbdd)
        c = bdd.cursor()
        res=c.execute('SELECT ? from ? where machine_id=?;',col,verif,machine)
        for i in reversed (res):
            add=add+i(0)
            ct=ct+1
            if ct>=tempscrise:
                break
        moyenne=add/ct
        if moyenne>=95:
            crise=True
        c.close()
    else:
        nbdd = bdd
        bdd = sqlite3.connect(nbdd)
        c = bdd.cursor()
        res=c.execute('SELECT ? from ? where machine_id=?;',col,verif,machine)
        for i in reversed (res):
            add=add+i(0)
            ct=ct+1
            if ct>=tempscrise:
                break
        c.close()
        nbdd = os.environ['BDD_Path']
        bdd = sqlite3.connect(nbdd)
        c = bdd.cursor()
        res=c.execute('SELECT ? from ? where machine_id=?;',col,verif,machine)
        for i in res:
            add=add+i(0)
            ct=ct+1
            if ct>=tempscrise:
                break
        moyenne=add/ct
        if (verif=="disk" and moyenne>=95):
            crise=True
        elif (verif=="cpu" and moyenne>=cpucrise):
            crise=True
        elif (verif=="ram" and moyenne<=ramcrise):
            crise=True
        c.close()
    return crise

def detectionsituationcrise(bdd):
    nbdd = bdd
    bdd = sqlite3.connect(nbdd)
    c = bdd.cursor()
    potentielcrise=[]
    res=c.execute('SELECT cpu.percent,disk.percent,ramFree,machine_id FROM temps JOIN cpu JOIN disk JOIN proc JOIN users')
    nb=res.rowcount
    l=[]
    for i in res[nb-1]:  #ajout de tt les resultats de la derniere ligne dans une liste pour check si pas de pb
        l.append(i)
    if (l[0]>=cpucrise):
        potentielcrise.append("cpu")
    if (l[1]>=diskcrise):
        potentielcrise.append("disk")
    if (l[2]<=ramcrise):
        potentielcrise.append("ram")
    c.close()
    if (len(potentielcrise)>0):
        for i in potentielcrise:
            crise=verificationcrise(bdd,i,l[3],nb)
            if crise==True:
                #prepgraphique()
                mailpret=prepmailcrise(i,l[3])
                fctmail(mailpret)

def pcdisparu():
    nbdd = os.environ['BDD_Path']
    bdd = sqlite3.connect(nbdd)
    c = bdd.cursor()
    crise=False
    res=c.execute('SELECT date from temps where machine_id=?;',machine)
    n=res.rowcount
    l=res[n-1]
    if (1==1):      #si ca fait trop lgt
        crise=True  #declare l alerte
    if crise==True:
        mailpret=prepmailcrise("pas de signe de vie",machine)
        fctmail(mailpret)
