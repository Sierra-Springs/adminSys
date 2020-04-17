#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sonde.py
#
#sudo apt install python-pip3
#pip3 install -U pip
#sudo apt-get install gcc python3-dev
#pip3 install psutil

import time
import psutil
import datetime
import tz
import os

temps=0

def affiche(l):
	print("---------------------")
	print(l)
	print("")

def cpuinfo():
	c=psutil.cpu_freq()
	c2=psutil.cpu_percent()
	# c3=os.getloadavg()  # NL : os instead of psutil & lancé pour chaque coeur -> problème selon nombre de coeur pour la bdd
	ctot=c+(c2,)
	cpuI=[]
	for i in ctot: #freq,freqmin,freqmax,cpu%,%/10 de chaque coeur
		cpuI.append(i)
	return cpuI

def temperature():
	temp=psutil.sensors_temperatures(fahrenheit=False)
	return temp

def fanspeed():
	fan=psutil.sensors_fans()
	return fan

def memoryinfo():
	m=psutil.virtual_memory()
	memoryI=[]
	for i in range (0,4): #total,available,used(%),free
		memoryI.append(m[i])
	return memoryI

def diskinfo():
	d=psutil.disk_usage('/')
	diskI=[]
	for i in d: #total,used,free,percent(%)
		diskI.append(i)
	return diskI

def processusinfo(): #nbr processus
	p=psutil.pids()
	processusI=len(p)
	return processusI

def usersinfo(): #nbre users co
	u=psutil.users()
	usersI=len(u)
	return usersI

def recup():
	cpu=cpuinfo()
	mem=memoryinfo()
	disk=diskinfo()
	proc=processusinfo()
	users=usersinfo()
	temps=[]
	date =time.localtime()
	#temps.append(date[2])
	#temps.append(date[3])
	#temps.append(date[4])
	temps=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())  # NL : format updated -> DATETIME
	L=[]
	L.append(cpu)
	L.append(disk)
	L.append(proc)
	L.append(users)
	L.append(temps)
	return L

def affichetot(L):
	affiche(L[0])
	affiche(L[1])
	affiche(L[2])
	affiche(L[3])
	affiche(L[4])
