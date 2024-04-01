##!/usr/bin/env python3
##################################################
## Mini-Projet, Gestion d'une bibliothéque.pdf
##################################################
## Author: HOUNAOUI Nassim
## Version: 1.0
## Email: nassim.hounaoui.etu@univ-lille.fr
##################################################

import csv
from jointure import *
import util



#######
# ouverture des fichiers csv
# création des listes utiles lors du projet

listeDictLivre = []
tabLivre = open("../Data/livres.csv",newline="",encoding='UTF-8')
lectureTabLivre = csv.DictReader(tabLivre,delimiter=";")
for ligne in lectureTabLivre:
    listeDictLivre.append(dict(ligne))

print(listeDictLivre[0])

def Titre(dictLivre):
    return dictLivre["Titre"]

listeDictLivre.sort(key=Titre)

listeDictAdherent = []
tabAdherent = open("../Data/liste_abonnés.csv",newline="",encoding='UTF-8')
lectureTabAdherent = csv.DictReader(tabAdherent,delimiter=";")
for ligne in lectureTabAdherent:
    listeDictAdherent.append(dict(ligne))
    
def Nom(dictAdherent):
    return dictAdherent["Nom"]

listeDictAdherent.sort(key=Nom)

def uniqueAdherentReference(refAdherent):
    uniqueReference = True  #variable repère de double référence
    
    #####
    #  boucle de comparaison de référence pour savoir si le nouvel adhérent est déjà présent
    for adherent in listeDictAdherent:
        if refAdherent == adherent["Référence "]:
            uniqueReference = False
            
    return uniqueReference
    
def uniqueLivreReference(refLivre):
    uniqueReference = True  #variable repere de double reference
    
    #####
    #  boucle de comparaison de référence pour savoir si le nouvel adhérent est déjà présent
    for Livre in listeDictLivre:
        if refLivre == Livre["Référence"]:
            uniqueReference = False
            
    return uniqueReference
   
#####################################################

def livreLibreQuand(livreID):
    """
    Cette fonction indique dans combien de temps le livre sera empruntable.

    Args:
        livreID: la référence du livre recherché.

    Returns:
        la durée en jours (Int) avant que le livre soit empruntable.
        renvoie -1 si la référence n'est pas correcte
    
    Example:
    
    >>> livreLibreQuand(3)
    0
    
    >>> livreLibreQuand(9)
    28
    
    >>> livreLibreQuand(123456789)
    -1
    
    """
    for dictLivre in listeDictLivre:
        if dictLivre["Référence"]==str(livreID):
            return int(dictLivre['nombres de jour avant le retour'])
    return -1
            
    
    

def livresARendre(adherentID):
    """
    Cette fonction indique quels sont les livres empruntés par un adhérent et quand doit-il les rendre.

    Args:
        adherentID: la référence de l'adhérent.

    Returns:
        la liste (list) des couples (tuple) de référencres de livres empruntés (Int) par adherentID et leur délai de retour en nombre de jours (Int)
        
    Example:
    
    >>> livresARendre(4)
    [(92, 8), (19, 11)]
    
    >>> livresARendre(8)
    []
    
    """
    return [(int(dictLivre["Référence"]),int(dictLivre['nombres de jour avant le retour'])) for dictLivre in listeDictLivre if dictLivre["Emprunteur"]==str(adherentID)]


def livresDispo():
    """
    Cette fonction indique la liste des livres qui sont, à ce jour, encore disponibles

    Returns:
        la liste (list) des livres disponibles
    
    """
    return [ dictLivre for dictLivre in listeDictLivre if (dictLivre["Emprunté (0=non, 1 = oui)"]=='0')]


def addAdherent(newAdherent):
    """
    Cette fonction ajoute un nouvel adhérent à la liste des adhérents
    
    Returns:
        (True) si l'operation c'est bien passé
        (False) sinon 

    """
    
    #  si la référence est unique alors on ajoute le nouvel adhérent à la liste et on reconvertit le tout en csv 
    if uniqueAdherentReference(newAdherent["Référence "]) :
        listeDictAdherent.append(newAdherent)
        vers_csv(listeDictAdherent,"../Data/liste_abonnés")
        return True
    
    return False


def emprunt(adherentID,livreID):
    """
    Cette fonction indique dans la liste des livres qu'un livre vient d'être emprunté par un adhérent (il lui reste
    alors 28 jours pour le rendre)
    
    Args:
        adherentID: la référence de l'adherent qui emprunte.
        
        livreID: la référence du livre qui vient d'être emprunter.
    
    Returns:
        (True) si l'opération s'est bien passé
        (False) sinon
    """
    for livre in livresDispo():
        if livre["Référence"] == livreID :
            livre['Total des prêts'] = str(int(livre['Total des prêts'])+1)
            livre['Emprunté (0=non, 1 = oui)']=1
            livre['nombres de jour avant le retour']=28
            livre['Emprunteur']= adherentID
            vers_csv(listeDictLivre,"../Data/livres")
            return True
    return False
        


    
def listeAdherentSetEmprunt():
    """
    Cette fonction indique sur la liste des adhérents (.csv) le ou les références des livres qu'ils ont
    emprunté.
    """
    for adherent in listeDictAdherent:
        adherent["Référence des livres empruntés"]=[]
        for livre in listeDictLivre:
            if adherent["Référence "] == livre["Emprunteur"]:
                adherent["Référence des livres empruntés"].append(int(livre["Référence"]))
                
    vers_csv(listeDictAdherent,"../Data/liste_abonnés")
    
    
def adherentAddEmprunt(adherentID,livreID):
    """
    Cette fonction ajoute un nouveau livre à la liste d'emprunts d'un adhérent.
    
    /!\ elle ne permet pas d'emprunter /!\
    
    Args:
        adherentID: la référence de l'adhérent.
        
        livreID: la référence du livre emprunté.
    """
    listeAdherentSetEmprunt()
    for adherent in listeDictAdherent:
        if adherent["Référence "] == adherentID:
            adherent["Référence des livres empruntés"].append(livreID)
    listeAdherentSetEmprunt()


tabLivre.close()
tabAdherent.close()

if __name__ == "__main__":
    
    #######
    # Ces lignes de code servent à faire appel au module doctest
    # permettant ainsi de tester mes fonctions  
    import doctest
    #doctest.testmod(verbose=True)
    #######
    