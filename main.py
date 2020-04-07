#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#


from sonde import *
from stockage import *
from suppression_ancienne import *
import os
import time
import sys

nbdd=sys.argv[1]
id1=int(sys.argv[2])
L=recup()
#affichetot(L)
stock(L,nbdd,id1)
deltemps(nbdd)







#import platform
#import os
#import sys
#
#print sys.platform()
#print os.name
#print platform.platform()
#print platform.uname()
