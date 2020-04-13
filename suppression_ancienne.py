#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suppression_ancienne.py
#
import sqlite3


def deltemps(nbdd):
	bdd = sqlite3.connect(nbdd)
	c = bdd.cursor()
	c.execute("SELECT id from temps where date<CURRENT_TIMESTAMP;")
	L=[]
	L=c.fetchall()
	D=[]
	for i in L:
		D.append(i)
	print(D)
	#WTF ? Pourquoi on fait pas "for i in L" directement ?
	#Ou meme "for i in c.fetchall()"
	for i in D:
		c.execute("DELETE from users where id=?",i)
		c.execute("DELETE from proc where id=?",i)
		c.execute("DELETE from temps where id=?",i)
		c.execute("DELETE from disk where id=?",i)
		c.execute("DELETE from cpu where id=?",i)
		## manque la ram
	bdd.commit()
	c.close()
