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
    c.execute('''CREATE TABLE cpu (machine_id, id, freq, freqmin, freqmax, percent)''')
    c.execute('''CREATE TABLE disk (machine_id, id, total, used, free, percent)''')
    c.execute('''CREATE TABLE proc (machine_id, id, nbproc)''')
    c.execute('''CREATE TABLE users (machine_id, id, nbusers)''')
    c.execute('''CREATE TABLE temps (machine_id, id, date DATETIME)''')  # NL : format DATETIME added
    c.execute('''CREATE TABLE ram (machine_id, id, ramTotal, ramUsed, ramFree, ramShared, ramBuffers, ramCached)''')  # NL : ram 
    #c.execute('''CREATE TABLE temps ( id,jour,heure,minute)''')
    bdd.commit()
    bdd.close()

nbdd = os.environ['BDD_Path']# NL (env variable)
create(nbdd)
