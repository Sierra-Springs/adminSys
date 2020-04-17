#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#

import os
import sys
sys.path.append(os.environ['PyRes'])  # NL : allow import for modules in PyRes (sonde, stockage, ...)

from sonde import *
from stockage import *
from suppression_ancienne import *

import time

'''
nbdd=sys.argv[1]
id1=int(sys.argv[2])
L=recup()
#affichetot(L)
stock(L,nbdd,id1)
deltemps(nbdd)
'''

# update by NL (environnment variable)
id1 = int(sys.argv[1])
L=recup()
stock(L, id1)
deltemps()



#import platform
#import os
#import sys
#
#print sys.platform()
#print os.name
#print platform.platform()
#print platform.uname()
