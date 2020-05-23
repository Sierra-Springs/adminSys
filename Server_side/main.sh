# python3 $MainPath/main.py
# echo $BDD_Path
# echo ""
(python3 $PyRes/createtable.py && echo "la base de donnée a été recréée")|| echo "La Base de donnée existait deja"
while [ 1 ]
do
	#$ShRes/updateBdd
	$ShRes/verifyRequest
done
