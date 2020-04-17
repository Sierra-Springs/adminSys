#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stockage.py
#
#  sudo apt install sqlite3

import sqlite3
import os
#bdd = sqlite3.connect('example.db')
#c = bdd.cursor()
##c.execute("INSERT INTO cpu VALUES (cpuI[0],cpuI[1],cpuI[2],cpuI[3])")
#c.execute("INSERT INTO cpu VALUES (1,2,3,4)")
#bdd.commit()
#c.close()


def stockcpu(L,c,id1):
	c.execute("INSERT INTO cpu VALUES  (?,?,?,?,?)",(id1,L[0],L[1],L[2],L[3]))

def stockdisk(L,c,id1):
	c.execute("INSERT INTO disk VALUES  (?,?,?,?,?)",(id1,L[0],L[1],L[2],L[3]))

def stockproc(L,c,id1):
	c.execute("INSERT INTO proc VALUES  (?,?)",(id1,L))

def stockusers(L,c,id1):
	c.execute("INSERT INTO users VALUES  (?,?)",(id1,L))

def stocktemps(L,c,id1):
	#c.execute("INSERT INTO temps VALUES  (?,?,?,?)",(id1,L[0],L[1],L[2]))
	c.execute("INSERT INTO temps VALUES  (?,?)",(id1,L))

def stock(L,id1):  # NL : stock(L,nbdd,id1)
	# NL : RAM added in main.sh
	nbdd = os.environ['BDD_Path']# NL (env variable)
	bdd = sqlite3.connect(nbdd)
	c = bdd.cursor()
	#c.execute("INSERT INTO cpu VALUES (cpuI[0],cpuI[1],cpuI[2],cpuI[3])")
	stockcpu(L[0],c,id1)
	stockdisk(L[1],c,id1)
	stockproc(L[2],c,id1)
	stockusers(L[3],c,id1)
	stocktemps(L[4],c,id1)
	bdd.commit()
	affbdd(c)
	c.close()

def affbdd(c):
	print("XXXXXXXX BDD XXXXXXXX")
	print("XX CPU XX")
	for row in c.execute('SELECT * FROM cpu'):
		print (row)
	print("XX DISK XX")
	for row in c.execute('SELECT * FROM disk'):
		print (row)
	print("XX PROCESSUS XX")
	for row in c.execute('SELECT * FROM proc'):
		print (row)
	print("XX USERS XX")
	for row in c.execute('SELECT * FROM users'):
		print (row)
	print("XX TEMPS XX")
	for row in c.execute('SELECT * FROM temps'):
		print (row)
