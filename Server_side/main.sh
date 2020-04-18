
# (environnment variable declaration)
# ! main.sh doit être placé à la racine du dossier du programme de monitoring
export MainPath=`pwd`
export BDD_Path="$MainPath/data/machineData.db"
export Data="$MainPath/data"
export RSA_KEY="$Data/RSA_KEY"
export ShRes="$MainPath/ShRes"
export PyRes="$MainPath/PyRes"


# end conf host

python3 $MainPath/main.py
