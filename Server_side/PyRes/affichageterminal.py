#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#
import sqlite3
import os
import re
from graphique import *
from fctmail import *

ramtable=["ramTotal", "ramUsed", "ramFree", "ramShared", "ramBuffers", "ramCached"]
disktable=["total","used","free","disk.percent"]
cputable=["freq","freqmin","freqmax","cpu.percent"]
proctable=["nbproc"]
userstable=["nbusers"]
tempstable=["date"]
listtable=["temps","ram","disk","cpu","proc","users","toutes"]
listpc=["tous"]
nbdd = os.environ['BDD_Hosts']
bdd = sqlite3.connect(nbdd)
c = bdd.cursor()
requete="SELECT hostname FROM Hosts ;"
res=c.execute(requete)
res=res.fetchall()
for i in res:
    z=list(i)
    listpc.append(z[0])
print (listpc)
c.close()
listcolor=["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m"]
nbcolor=len(listcolor)
affhisto=0

def prepgraphterminal(l,lc,lg):
    print("Preparation du graphique")
    liste=[]
    donnees=[]
    for j in range (0,len(lg[0])):
        donnees.append([])
    liste=l
    for i in lc:
        liste.append(i)
    lg=list(lg)
    for i in range (0,len(lg)):
        lg[i]=list(lg[i])
    for j in range (0,len(lg[0])):
        for i in range (0,len(lg)):
            donnees[j].append(lg[i][j])
            #donnees[j].append(lg[i])
    print("Preparation du graphique termine")
    return liste,donnees

def conversionnombre(n,l):
    num=""
    lt=[]
    ct=0
    indl=0
    for x in l:
        lt.append([])
        for j in x:
            for i in re.findall('\d', j):
                num = num+str(i)
            num = int(num)
            if n[indl]=="ramTotal" or n[indl]=="ramUsed" or n[indl]=="ramBuffers" or n[indl]=="ramCached":
                lt[ct].append(num*100)
            else :
                lt[ct].append(num)
            num=""
            indl=indl+1
        ct=ct+1
        indl=0
    return lt

def prepmailterminal(pc,table,colonne):
    print("Preparation du mail")
    liste=[]
    if colonne=="toutes":
        l.append(table+" de "+str(pc))
    else :
        l.append(colonne+" de "+str(pc))
    liste.append(colonne+" de "+table+".Graphique demandé lors d un affichage via le terminal")
    liste.append('graph.svg')
    liste.append(os.environ['Stockage']+'/graph.svg')
    print("Preparation du mail termine")
    return liste

def affichagecouleur(lc,res,affhisto,graph):
    ct=0
    lg=[]
    ctcolor=0
    print()
    for i in lc:
        st=listcolor[ctcolor]+i+"\033[0m"
        print(st," | ",end="")
        ctcolor+=1
        if ctcolor==nbcolor:
            ctcolor=0
    print()
    ctcolor=0
    for i in reversed (res):
        for j in i:
            st=listcolor[ctcolor]+str(j)+"\033[0m"
            print(st,"|",end="")
            ctcolor+=1
            if ctcolor==nbcolor:
                ctcolor=0
        ct=ct+1
        ctcolor=0
        if (graph=="oui"):
            lg.append(i)
        print()
        if (ct>=affhisto and affhisto!=0):
            break
    return lg,ct

def afficheterminal():
    pc=(input("Pour quel PC voulez vous afficher des informations? : "))
    while pc not in listpc:
        print("PC inconnu")
        pc=input("Pour quel PC voulez vous afficher des informations? : ")
    table=(input("Quelles tables de la base de données voulez-vous afficher? : "))
    colonne="toutes"
    while table not in listtable:
        print("table inconnu")
        table=str(input("Quelles tables de la base de données voulez-vous afficher? : "))
    colonne=(input("Quelle colonne voulez-vous (toutes ou une colonne de la table)? : "))
    while (table=="ram" and colonne not in ramtable and colonne!="toutes") :
        print("colonne inconnu pour la table ram :ramTotal, ramUsed, ramFree, ramShared, ramBuffers, ramCached")
        colonne=(input("Quelle colonne voulez-vous (toutes)? : "))
    while (table=="cpu" and colonne not in cputable and colonne!="toutes") :
        print("colonne inconnu pour la table ram :freq,freqmin,freqmax,cpu.percent")
        colonne=(input("Quelle colonne voulez-vous (toutes)? : "))
    while (table=="disk" and colonne not in disktable and colonne!="toutes") :
        print("colonne inconnu pour la table ram :total,used,free,disk.percent")
        colonne=(input("Quelle colonne voulez-vous (toutes)? : "))
    affhisto=int((input("Combien de données voulez-vous récupérer (0=toutes)? : ")))
    graph="non"
    if (table!="toutes" and pc!="tous"):
        graph=(input("Voulez-vous générer un graphique? : "))
    l=[]
    lc=[]
    if (pc=="tous"):
        if (table=="toutes"):
            stncol=""
            lc=[]
            lc.append("machine")
            lc.append("id")
            stncol="temps.machine_id,temps.id"
            for i in tempstable:
                stncol=stncol+","+i
                lc.append(i)
            for i in cputable:
                stncol=stncol+","+i
                lc.append(i)
            for i in disktable:
                stncol=stncol+","+i
                lc.append(i)
            for i in ramtable:
                stncol=stncol+","+i
                lc.append(i)
            for i in proctable:
                stncol=stncol+","+i
                lc.append(i)
            for i in userstable:
                stncol=stncol+","+i
                lc.append(i)
            nbdd = os.environ['BDD_Path']
            bdd = sqlite3.connect(nbdd)
            requete='SELECT '+stncol+' FROM temps JOIN cpu on temps.id=cpu.id JOIN disk on temps.id=disk.id JOIN ram on temps.id=ram.id JOIN proc on temps.id=proc.id JOIN users on temps.id=users.id;'
            #requete='SELECT * FROM temps JOIN cpu on temps.id=cpu.id JOIN disk on temps.id=disk.id JOIN ram on temps.id=ram.id JOIN proc on temps.id=proc.id JOIN users on temps.id=users.id;'
            c = bdd.cursor()
            res=c.execute(requete)
            res=res.fetchall()
            affichagecouleur(lc,res,affhisto,graph)
            c.close()
        else :
            nbdd = os.environ['BDD_Path']
            bdd = sqlite3.connect(nbdd)
            requete="SELECT * FROM "+table+' ;'
            c = bdd.cursor()
            res=c.execute(requete)
            res=res.fetchall()
            lc.append("machine")
            lc.append("id")
            if table=="ram":
                lc.extend(ramtable)
            elif table=="disk":
                lc.extend(disktable)
            elif table=="cpu":
                lc.extend(cputable)
            elif table=="proc":
                lc.extend(proctable)
            elif table=="users":
                lc.extend(userstable)
            affichagecouleur(lc,res,affhisto,graph)
            c.close()
    else :
        if (table=="toutes"):
            nbdd = os.environ['BDD_Path']
            bdd = sqlite3.connect(nbdd)
            stncol=""
            lc=[]
            lc.append("id")
            stncol="temps.id"
            for i in tempstable:
                stncol=stncol+","+i
                lc.append(i)
            for i in cputable:
                stncol=stncol+","+i
                lc.append(i)
            for i in disktable:
                stncol=stncol+","+i
                lc.append(i)
            for i in ramtable:
                stncol=stncol+","+i
                lc.append(i)
            for i in proctable:
                stncol=stncol+","+i
                lc.append(i)
            for i in userstable:
                stncol=stncol+","+i
                lc.append(i)
            #requete='SELECT '+stncol+' FROM temps NATURAL JOIN cpu NATURAL JOIN disk NATURAL JOIN proc NATURAL JOIN users  where machine_id="'+str(pc)+'";'
            requete='SELECT '+stncol+' FROM temps JOIN cpu on temps.id=cpu.id JOIN disk on temps.id=disk.id JOIN ram on temps.id=ram.id JOIN proc on temps.id=proc.id JOIN users on temps.id=users.id where temps.machine_id="'+str(pc)+'";'
            #requete='SELECT '+stncol+' FROM temps JOIN cpu on temps.id=cpu.id JOIN disk on temps.id=disk.id  JOIN proc on temps.id=proc.id JOIN users on temps.id=users.id where temps.machine_id="'+str(pc)+'";'
            c = bdd.cursor()
            res=c.execute(requete)
            res=res.fetchall()
            affichagecouleur(lc,res,affhisto,graph)
            c.close()
        else :
            stncol=""
            if table=="ram":
                lc=(ramtable)
            elif table=="disk":
                lc=(disktable)
            elif table=="cpu":
                lc=(cputable)
            elif table=="proc":
                lc=(proctable)
            elif table=="users":
                lc=(userstable)
            elif table=="temps":
                lc=(tempstable)
            premiere=True
            for i in lc:
                if premiere==True:
                    stncol=i
                    premiere=False
                else :
                    stncol=stncol+","+i
            if colonne!="toutes":
                stncol=colonne
                lc=[]
                lc.append(stncol)
            nbdd = os.environ['BDD_Path']
            bdd = sqlite3.connect(nbdd)
            c = bdd.cursor()
            requete="SELECT "+stncol+" FROM "+table+' where machine_id="'+str(pc)+'" ;'
            res=c.execute(requete)
            res=res.fetchall()
            lg,ct=affichagecouleur(lc,res,affhisto,graph)
            c.close()
            if colonne=="toutes":
                l.append(table+" de "+str(pc))
            else :
                l.append(colonne+" de "+str(pc))
            if graph=="oui":
                l.append(0)
                l.append(ct)
                if table=="ram":
                    lg=conversionnombre(lc,lg)
                liste,donnees=prepgraphterminal(l,lc,lg)
                graphpygal(liste,donnees)
                mailpret=prepmailterminal(pc,table,colonne)
                fctmail(mailpret)

afficheterminal()

