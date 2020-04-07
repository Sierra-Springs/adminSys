#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suppression_ancienne.py
#  

import sqlite3
import os
import sys

def supp(nbdd):
	bdd=sqlite3.connect(nbdd)
	c=bdd.cursor()
	c.execute('''DROP TABLE cpu''')
	c.execute('''DROP TABLE disk ''')
	c.execute('''DROP TABLE proc ''')
	c.execute('''DROP TABLE users ''')
	c.execute('''DROP TABLE temps ''')
	bdd.commit()
	bdd.close()
	
def suppfic(nbdd):
	if (os.path.exists(nbdd)):
		os.remove(nbdd)

nbdd=sys.argv[1]
suppfic(nbdd)
