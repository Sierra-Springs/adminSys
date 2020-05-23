#!/bin/bash


#nom='example.db'
echo 'La base de données est :'
#echo $nom
echo $BDD_Path

python3 $PyRes/deletetable.py $BDD_Path
python3 $PyRes/createtable.py $BDD_Path
echo "updated" > $Data/transfert_table.smph

id=0
while :
do
	python3 $MainPath/main.py $id
	echo "ramInfo"
	$ShRes/ramInfo $id # NL

	$ShRes/transfert_table # NL

	id=$(($id + 1))
	sleep 5
done
