#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  createtable.py
#

import sqlite3
import os
import sys


def create(nbdd):
    bdd=sqlite3.connect(nbdd)
    c=bdd.cursor()
    c.execute('''CREATE TABLE cpu (id_machine, id, freq, freqmin, freqmax, percent)''')
    c.execute('''CREATE TABLE disk (id_machine, id,total, used, free, percent)''')
    c.execute('''CREATE TABLE proc (id_machine, id, nbproc)''')
    c.execute('''CREATE TABLE users (id_machine, id, nbusers)''')
    c.execute('''CREATE TABLE temps (id_machine, id, date DATETIME)''')  # NL : format DATETIME added
    c.execute('''CREATE TABLE ram (id_machine, id, ramTotal, ramUsed, ramFree, ramShared, ramBuffers, ramCached)''')  # NL : ram 
    #c.execute('''CREATE TABLE temps ( id,jour,heure,minute)''')
    bdd.commit()
    bdd.close()

nbdd = os.environ['BDD_Path']# NL (env variable)
create(nbdd)
