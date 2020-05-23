#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mail_faille.py
#


#from sonde import *
#from stockage import *
#from suppression_ancienne import *
#import os
#import sys

import time
import os  # NL : for env var
import pygal
from fctmail import *

def graphpygal(liste,donnes):
    line_chart = pygal.Line()
    line_chart.title = str(liste[0])
    line_chart.x_labels = map(str, range(liste[1], liste[2]))
    #line_chart.y_labels = map(str, range(liste[3], liste[4]))
    y=0
    for i in range (3,len(liste)):
    	line_chart.add(str(liste[i]), donnes[y])
    	y=y+1
    line_chart.render()
    fic=str(os.environ['Stockage']+'/graph.svg')
    line_chart.render_to_file(fic)
    print("graphe termine")

#exemple :
#l=[]
#l.append("Graphique")
#l.append(2002)
#l.append(2013)
#l.append("Firefox")
#l.append("Chrome")
#l.append("IE")
#l.append("O")
#d=[]
#d.append([None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
#d.append([None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
#d.append([85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
#d.append([14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
#graphique(l,d)
