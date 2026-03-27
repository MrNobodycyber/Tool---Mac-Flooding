#!/bin/py
from scapy.all import *
import random
import os


os.system("clear") # rendre page vierge avant utilisation

# créer une fonction pour dessiner a chaque fois. Faire une boucle qui re affiche par exemple commande_user a chaque commande faite. Rajt une option si l'utilisateur a missclik OU
# a mit du vide -> cases diff en fct de ca .



# Var d'initiation.
dict = {}
rd_MAC = randMAC();




def affichage() :
# Affichage graphique.

# DEBUT

ascii = r"""

 .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. .   .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. .   .  .. ..  .  .. ..  .  .. ..  .  .. ..M .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  . M.. ..  .  .. ..  .  .. ..  .  .. ..  .   . ..  .  .. ..  .  .. ..  .  
.. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .K ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. M.  .  .. ..  .  .. ..  .  .. ..  .  .. .. M.  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .M .. ..  .  .. ..  .  .. ..  .  .. ..  .  .M ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. M.  .  .. ..  .  .. ..  .  .. ..  .  .. .. M.  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .M .. ..  .  .. ..  .  .. ..  .  .. ..  .  .M ..  .  .. ..  .  .. ..  .  
.. ..  .  .. ..  .  .. ..  .M .. ..  .  .. ..  .  .. ..  .  .. ..  .  .M ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. M.  .  .. ..  .  .. ..  .  .. ..  .  .. .. M.  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .MM.. ..  .  .. ..  .  .. ..  .  .. ..  .  MM ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. .M  .  .. ..  .  .. ..  .  .. ..  .  .. ..M .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .  M. ..  .  .. ..  .  .. ..  .  .. ..  . M . ..  .  .. ..  .  .. ..  .  
.. ..  .  .. ..  .  .. ..  .  :. ..  .  .. ..  .  .. ..  .  .. ..  . M.. ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. .. M.  .. ..  .  .. ..  .  .. ..  .  .. M.  .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .  ..M..  .  .. ..  .  .. ..  .  .. ..     .. ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. ..  M  .. ..  .  .. .M .  .. ..  .  ..M..  .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .  .. M.  .  .. .. MMMMMMMMM  .  .. .. Wx  .. ..  .  .. ..  .  .. ..  .  
.. ..  .  .. ..  .  .. ..  .  .. M.  .  .. .MMMMMMMMMMMMM.  .. .. M.  .. ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. ..  .MM.. ..  MMMMMMMMMMMMMMMMM.  .  MM ..  .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .  .. MMM .   MMMMMMMMMMMMMMMMMMM.. .MMM.  .. ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. ..  . MMM ..MMMMMMMMMMMMMMMMMMMMM .MMM. ..  .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .  .. ..MM   MMMMMMMMMMMMMMMMMMMMM. MM  .  .. ..  .  .. ..  .  .. ..  .  
.. ..  .  .. ..  .  .. ..  .  .. .. MM  MMMMMMMMMMMMMMMMMMMMM.MM.  .  .. ..  .  .. ..  .  .. ..  .  
  .  .. ..  .:MMMMMMMMMMMMMMMM  .  ..MM.MMMMMMMMMMMMMMMMMMMMMMM  .. ..MMMMMMMMMMMMMMMMk ..  .  .. ..
.. ..  .  .MMMMM .  .. ..  MMMMo ..  .MMMMMMMMMMMMMMMMMMMMMMMM ..  . MMMM..  .  .. .OMMMM .. ..  .  
  .  .. MMMx.  .. ..  .  .. .MMMM. .. ..MMMMMMMMMMMMMMMMMMMM  .  ..MMMM .  .. ..  .  .. .MMM.  .. ..
.. .. MM0 .. ..  .  .. ..  .  ..MMMM .  . MMMMMMMMMMMMMMMMM .. .MMMM  .. ..  .  .. ..  .  .,MM.  .  
.. .MM .  .. ..  .  .. ..  .  .. ..kMMM :. MMMMMMMMMMMMMMM  .MMMK  .  .. ..  .  .. ..  .  .. .MM .  
  XM .. ..  .  .. ..  .  .. ..  .  .. .MMMMMMMMMMMMMMMMMMMMMM .  .. ..  .  .. ..  .  .. ..  .  .dM..
. . ..  .  .. ..  .  .. ..  .  .. ..  .  .. .MMMMMMMMMMMMM.  .. ..  .  .. ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. ..  .  .. ..  MMMMMMMMMMMMMMMMN.  .  .. ..  .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .  .. ..  . MMMO.MMMMMMMMMMMM cMMM. ..  .  .. ..  .  .. ..  .  .. ..  .  
.. ..  .  .. ..  .  .. ..  .  .. ..MMMW .. MM  MMMMMMM MM   .0MMM  .  .. ..  .  .. ..  .  .. ..  .  
 .  .. ..  .  .. ..  .  .. .MMMMMM.. ..  MX .MMMMMMMMM.M..  .  MMMMMM .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  MMMMM ..  .  .Mk. M .  .. ..M .M .. ..  .MMMMM..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .MMM.  .  .. ..MM.  .. ..  .  ..  M  .  .. .. XMM .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..MW.  .. ..  . MM. ..  .  .. ..  . :M. ..  .  ..  M  .  .. ..  .  .. ..  .  
.. ..  .  .. ..  .  .. .M  .  .. ..  cMM.. ..  .  .. ..  .  OMM..  .  .. ..Mc.  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  MM .. ..  .  .MMM.  .  .. ..  .  .. .. OMM .. ..  .  .MM..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  MMM..  .  .. .. M:  .. ..  .  .. ..  .  .. M.  .  .. ..  MMM.. ..  .  .. ..  .  
  .  .. ..  .  .. .MMM.  .. ..  .  .M ..  .  .. ..  .  .. ..  . :. ..  .  .. MMM .  .. ..  .  .. ..
.. ..  .  .. ..  .MM.. ..  .  .. ..M .  .. ..  .  .. ..  .  .. .M  .  .. ..  .  MM ..  .  .. ..  .  
.. ..  .  .. ..  0M .. ..  .  .. .MW .  .. ..  .  .. ..  .  .. ..M .  .. ..  .  .MM..  .  .. ..  .  
  .  .. ..  .  .M..  .  .. ..  . M.. ..  .  .. ..  .  .. ..  .  M  ..  .  .. ..  MM .. ..  .  .. ..
.. ..  .  .. .. M.  .. ..  .  .. MM  .  .. ..  .  .. ..  .  .. ..MM.  .. ..  .  .. M.  .  .. ..  .  
  .  .. ..  .  M. ..  .  .. ..  .M .. ..  .  .. ..  .  .. ..  .  .Mx..  .  .. ..  . M.. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  M  .. ..  .  .. ..  .  .. ..  .  
.. ..  .  .. .M  .  .. ..  .  ..M..  .  .. ..  .  .. ..  .  .. ..  M  .. ..  .  .. ..M .  .. ..  .  
  .  .. ..  .  .. ..  .  .. ..  M  .. ..  .  .. ..  .  .. ..  .  ..M..  .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .  ..M..  .  .. ..  .  .. ..  .  .. ..     .. ..  .  .. ..  .  .. ..  .  
  .  .. ..  .  .. ..  .  .. ..  M  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..
.. ..  .  .. ..  .  .. ..  .  ..M..  .  .. ..  .  .. ..  .  .. ..     .. ..  .  .. ..  .  .. ..  .  
.. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  .  .. ..  X  .. ..  .  .. ..  .  .. ..  .  

   \  |   _ \       \  |         |                 |
  |\/ |  |   |       \ |   _ \   __ \    _ \    _` |  |   |
  |   |  __ <      |\  |  (   |  |   |  (   |  (   |  |   |
 _|  _| _| \_\ _) _| \_| \___/  _.__/  \___/  \__,_| \__, |
                                                     ____/
""""
print (ascii)

# FIN
def action () :
# affiche l'input utilisateur
commande_user = input("Use a command, or type h to have some help ;) >>> ")

# AJout d'une condition en fct de l'entrée utilisateur !!
match commande_user:
        case "help" : # Cas Numéro 1
                help() # Appel de fct help.

        case "simple switch" : # Cas Numéro 2
                simple_flooding(dict,rd_MAC) # utiliser la fct simple_flooding.

        case "" : # Cas numéro 3 : l'utilisateur a missclick.





#Fonction qui va vérifier si la val est déja dans le dict ou non des MAC utilisées.
def verify(trame_al, dict_al) :
        i = 0
        if dict_al == {} : # Si le tableau est vide :
                print  ('tableau vide ')

        else:
                while i<len(dict_al) : # Tant que i est inférieur à la taille du tableau  -> parcours entier du tableau :
                        if trame_al != dict_al{i} : # Si La val est pas la même :
                                print ('Valeur non utilisée')
                                i+= 1
                        else :
                                raise ValueError('valeur utilisée') # Le raise va nous servir pour déclencher une erreur qui va être reconnue par le except juste en dessous !!



# Attaque simple.
def simple_flooding (dict,rd_MAC) :
# POUR LE MOMENT : progrm qui prend que les trames jamais prises avec MAC inconnues - optimisation. 
for i in range(100) : # Envoie de 100 trames.

        trame = Ether(dst= rd_MAC, type=0x0800) / IP(dst='255.255.255.255') # Création de la trame.

        try :
                verify(trame,dict) # Vérification
        except ValueError : # ValueError précise l'error qui est attendue -> sinon error général .
                print ('La trame n a pas pu être envoyée') # Si le raise se déclenche !

        else:                                            # Si verify s'exec jusu'au bout :
                 sendp(trame) # Envoie de la trame.






def iterative_attack ():


        pass






def help () :
        x = r"""

        < type -h to get some help. >
        < type -s to try a simple flooding attack. >
        < type ...>

"""
        print (x)
