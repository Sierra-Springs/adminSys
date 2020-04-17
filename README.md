# adminSys
administration des systèmes d'exploitation ➞ monitoring de parc informatique


## Audran

Your comments here


## Nathanaël

### Protocole de transfert (Principe général. Peut évoluer)
Remarque : un transfert peu être "long" (relativement).
On peut donc suivre le schéma suivant:
mv file file.tmp
touch file
transfert file.tmp

Fichier : 
	hote : 
		file (fichier à transférer), 
		smph (sémaphore à état multiple : "new", "transfert_attempt", "transfered", "updated")
		RSA_KEY_NomHote (cf etape 1)
		~/.ssh/authorized_key (contient autorsation pour RSA_KEY_SERVER)
	serveur:
		~/.ssh/authorized_key (etape 1 : autorsation pour RSA_KEY_NomHote)
		RSA_KEY_SERVER
		
1) Installation
[hote] :
	ssh-keygen -f RSA_KEY_NomHote -P ""
	ssh-copy-id -i ./RSA_KEY_NomHote user@IP_SERVER
	(((  SAISIR MOT DE PASSE SERVEUR )))

2) Transfert fichier
[hote] :
	Si smph == new
		smph = transfert_attempt
		scp -i ./RSA_KEY_NomHote ./file user@IP_SERVER:/the/dest/path/     &&     smph = transfered
		
[Serveur]:
	cp ./file ./file.tmp  (OU action sur le fichier)
	smph = updated (smph modifié à distance)
	

3) Modification fichier:
[hote]:
	if smph == updated 
		modifier le fichier
	else 
		ne pas modifier
	
