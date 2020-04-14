#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  createtable.py
#

import sqlite3

import sys


def create(nbdd):
    bdd=sqlite3.connect(nbdd)
    c=bdd.cursor()
    c.execute('''CREATE TABLE cpu ( id,freq,freqmin,freqmax,percent)''')
    c.execute('''CREATE TABLE disk ( id,total,used,free,percent)''')
    c.execute('''CREATE TABLE proc ( id, nbproc)''')
    c.execute('''CREATE TABLE users ( id, nbusers)''')
		c.execute('''CREATE TABLE temps ( id, date DATETIME)''') # NL : format DATETIME added
    #c.execute('''CREATE TABLE temps ( id,jour,heure,minute)''')
    ##manque la ram
    bdd.commit()
    bdd.close()

nbdd=sys.argv[1]
create(nbdd)
