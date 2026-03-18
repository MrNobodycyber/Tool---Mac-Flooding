#!/bin/py
from scapy.all import *
import random

#Fonction qui va vérifier si la val est déja dans le dict ou non des MAC utilisées.
def verify(trame_al, dict_al) :
	i = 0
	while i<len(dict_al) -1 : # Tant que i est inférieur à la taille du tableau -1 -> parcours entier du tableau :
		if trame_al =! dict_al[i] : # Si La val est pas la même :
			print ('Valeur non utilisée')
			i+= 1
		else :
			print('Value used')
			break



# Var d'init.
dict = []
rd_MAC = rand_MAC();

# POUR LE MOMENT : progrm qui prend que les trames jamais prises avec MAC inconnues - optimisation. 
for i in range(100) : # Envoie de 100 trames.

	trame = Ether(src=rd_MAC, dst= rd_MAC, type=0x0800) / IP(dst='255.255.255.255') # Création de la trame.
	trame.verify(trame,dict) # Vérification

	if (trame.verify()) { # Si verify s'exec jusu'au bout :
		dict [i] = trame # On met dans le dictionnaire.
 		sendp(trame) # Envoie de la trame.
	else :

		pass # On passe le programme, qui va reboucler et recréer une MAC aléatoire.

}

# Il faut rajouter une idée de temps, clé valeur into dict de MAC -> variation du renvoie des MAC en fct du temps.



# Rajouter une idée de dictionnaire clé valeur -> variation de l'envoie de l'adresse MAC avec le temps ou elle est apparue pour la première fois !

