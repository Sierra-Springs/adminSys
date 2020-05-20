#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#
import sqlite3
import os
from graphique import *
from fctmail import *

ramtable=["ramTotal", "ramUsed", "ramFree", "ramShared", "ramBuffers", "ramCached"]
disktable=["total","used","free","percent"]
cputable=["freq","freqmin","freqmax","percent"]
proctable=["nbproc"]
userstable=["nbusers"]
tempstable=["date"]

def prepgraph(l,lc,lg):
    liste=[]
    donnees=[]
    for j in range (0,len(lg[0])):
        donnees.append([])
    liste=l
    for i in lc:
        liste.append(i)
    for j in range (0,len(lg[0])):
        for i in lg:
            donnnes[j].append(lg(i))
    return liste,donnees

def prepmail(pc,table):
    liste=[]
    liste.append(pc)
    liste.append(table)
    liste.append('graph.svg')
    liste.append(os.environ['Stockage']+'/graph.svg')
    return liste

def afficheterminal():
    pc=(input("Pour quels PCs voulez vous afficher des informations"))
    #histo=string(input("Quelle taille d'historique voulez-vous"))
    table=(input("Quelles tables de la base de données voulez-vous afficher"))
    graph="non"
    if (table!="toutes" and pc!="tous"):
        graph=(input("Voulez-vous générer un graphique"))
    lg=[]
    l=[]
    lc=[]
    listtable=["temps","ram","disk","cpu","proc","users","toutes"]
    while table not in listtable:
        print("table inconnu")
        table=string(input("Quelles tables de la base de données voulez-vous afficher"))
    if (pc=="tous"):
        if (table=="toutes"):
            nbdd = os.environ['BDD_Path']
            bdd = sqlite3.connect(nbdd)
            c = bdd.cursor()
            for i in c.execute('SELECT * FROM temps JOIN cpu JOIN disk JOIN proc JOIN users'):
                print(i)
        else :
            nbdd = os.environ['BDD_Path']
            bdd = sqlite3.connect(nbdd)
            c = bdd.cursor()
            res=c.execute('SELECT * FROM ? ;',table)
##            if (res.rowcount==0):
##                print("Cette table n'existe pas")
##            else :
            for i in res:
                print(i)
    else :
        try:
            pc=int(pc)
        except ValueError:
            print("ID machine invalid")
        if (table=="toutes"):
            nbdd = os.environ['BDD_Path']
            bdd = sqlite3.connect(nbdd)
            c = bdd.cursor()
            for i in c.execute('SELECT * FROM temps JOIN cpu JOIN disk JOIN proc JOIN users where machhine_id=?',pc):
                print(i) 
        else :
            stncol=""
            if table=="ram":
                lc=ramtable
            elif table=="disk":
                lc=disktable
            elif table=="cpu":
                lc=cputable
            elif table=="proc":
                lc=proctable
            elif table=="users":
                lc=userstable
            for i in lc:
                stncol=stncol+","+i
            nbdd = os.environ['BDD_Path']
            bdd = sqlite3.connect(nbdd)
            c = bdd.cursor()
            res=c.execute('SELECT ? FROM ? where id=?;',stncol,table,pc)
            nb=res.rowcount
            for i in res:
                print(i)
                if (graph=="oui"):
                    lg.append()
            if graph=="oui":
                l.append(pc)
                l.append(0)
                l.append(nb)
                liste,donnees=prepgraph(l,lc,lg)
                graphpygal(liste,donnees)
                mailpret=prepmail(pc,table)
                fctmail(mailpret)
                
            
