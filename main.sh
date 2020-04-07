#!/bin/bash
nom='example.db'
echo 'La base de données est :'
echo $nom
python3 deletetable.py $nom
python3 createtable.py $nom
id=0
while :
do
	python3 main.py $nom $id
	
	id=$(($id + 1))
	sleep 20
done
