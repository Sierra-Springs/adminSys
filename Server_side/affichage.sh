# (environnment variable declaration)
# ! main.sh doit être placé à la racine du dossier du programme de monitoring
export MainPath=`pwd`
export BDD_Path="$MainPath/data/Data.db"
export BDD_Hosts="$MainPath/data/Hosts.db"
export Data="$MainPath/data"
export Ressources="$Data/Ressources"
export RSA_KEY_Path="$Data/RSA_KEY"
export RSA_KEY="$RSA_KEY_Path/RSA_KEY_SERVER"
export ShRes="$MainPath/ShRes"
export PyRes="$MainPath/PyRes"
export Stockage="$MainPath/Stockage"

export transfertDb="/home/monitor/transfert_db"

# Host remote var:
export transfert_table_smph_PATH="/home/audran/adminSys/Host_side/data/transfert_table.smph"
# end conf host

# python3 $MainPath/main.py
# echo $BDD_Path
# echo ""
python3 $PyRes/affichageterminal.py

