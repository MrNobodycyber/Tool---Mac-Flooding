#!/bin/py
from scapy.all import *
import random

#Fonction qui va vérifier si la val est déja dans le dict ou non des MAC utilisées.
def verify(trame_al, dict_al) :
        i = 0 
        if dict_al == {} : # Si le tableau est vide :
                print  ('tableau vide ')

        else:
                while i<len(dict_al) : # Tant que i est inférieur à la taille du tableau  -> parcours entier du tableau :
                        if trame_al != dict_al[i] : # Si La val est pas la même :
                                print ('Valeur non utilisée')
                                i+= 1
                        else :
                                raise ValueError('valeur utilisée') # Le raise va nous servir pour déclencher une erreur qui va être reconnue par le except juste en dessous !!



# Var d'init.
dict = {} # Dictionnaire a revoir, pour allier clé valeurs.
rd_MAC = randMAC();

# POUR LE MOMENT : progrm qui prend que les trames jamais prises avec MAC inconnues - optimisation. 
for i in range(100) : # Envoie de 100 trames.

        trame = Ether(dst= rd_MAC, type=0x0800) / IP(dst='255.255.255.255') # Création de la trame.

        try :
                verify(trame,dict) # Vérification
        except ValueError : # ValueError précise l'error qui est attendue -> sinon error général .
                print ('La trame n a pas pu être envoyée') # Si le raise se déclenche !

        else:                                            # Si verify s'exec jusu'au bout :
                 sendp(trame) # Envoie de la trame.



# Il faut rajouter une idée de temps, clé valeur into dict de MAC -> variation du renvoie des MAC en fct du temps.

