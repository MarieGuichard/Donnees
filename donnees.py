import csv

grands_sites=[] # crée un tableau dans lequel sera rangé toutes les informations concernant le document grands_sites.csv

documents = open("grands_sites.csv",newline="") # ouvre le document grands_sites.csv
lecture = csv.DictReader(documents,delimiter=",")

for ligne in lecture:   # range dans le tableau grands_sites toutes les informations concernant le document grands_sites.csv
    grands_sites.append(dict(ligne))
documents.close()       # ferme le document grands_sites.csv

def affiche(liste):
    for i in range(len(liste)):
        print(liste[i])
        
def code_label(numero,table):
    ''' affiche la liste des grands sites dont le code label est égal au numéro'''
    liste = [] # crée un tableau dans lequel sera rangé toutes les réponses
    for i in range(len(table)):  # range dans le tableau appelé liste toutes les données de la table dont le code label est celui égal à numéro
        if table[i]["code_label"] == numero:
            liste.append(table[i])
    affiche(liste)

def identifiant(numero,table):
    '''renvoie le grand site de l'identifiant cherché'''
    liste = []
    for i in range(len(table)):
        if table[i]["id"] == numero:
            liste.append(table[i])
    affiche(liste)



