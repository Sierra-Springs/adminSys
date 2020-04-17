#!/bin/bash

# conf host
# (environnment variable declaration)
# ! main.sh doit être placé à la racine du dossier du programme de monitoring
export MainPath=`pwd`
export BDD_Path="$MainPath/data/machineData.db"
export ShRes="$MainPath/ShRes"
export PyRes="$MainPath/PyRes"
# end conf host


#nom='example.db'
echo 'La base de données est :'
#echo $nom
echo $BDD_Path

python3 $PyRes/deletetable.py $BDD_Path
python3 $PyRes/createtable.py $BDD_Path

id=0
while :
do
	python3 $MainPath/main.py $id
	echo "ramInfo"
	$ShRes/ramInfo $id # NL

	id=$(($id + 1))
	sleep 20
done
