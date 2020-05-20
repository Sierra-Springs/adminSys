#!/bin/bash

# conf host
# (environnment variable declaration)
# ! main.sh doit être placé à la racine du dossier du programme de monitoring
export hostname="machine1"

export MainPath=`pwd`
export BDD_Path="$MainPath/data/$hostname.db"
export Data="$MainPath/data"
export RSA_KEY_Path="$Data/RSA_KEY"
export RSA_KEY="$RSA_KEY_Path/RSA_KEY_$hostname"
export ShRes="$MainPath/ShRes"
export PyRes="$MainPath/PyRes"


# Server remote var:
export port="44"
export username="monitor"
export ip="192.168.1.81"
export dest_transfert="/home/$username/transfert_db"
# end conf host


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
