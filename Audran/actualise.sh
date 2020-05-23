#!/bin/bash
pop=`sudo ls /media/sf_partage/ `
for i in $pop
do
	sudo chmod -R 755 /media/sf_partage/$i
	sudo cp -r /media/sf_partage/$i ./
	sudo chmod -R 755 $i
	echo $i
done
