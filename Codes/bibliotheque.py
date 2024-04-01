import csv
livres =[]

documents = open("livres.csv",newline="")
lecture_livre = csv.DictReader(documents,delimiter=";")
for ligne in lecture_livre:
    livres.append(dict(ligne))
documents.close()
print(livres)
abonnes = []
documents = open("liste_abonnés.csv",newline="")
lecture_abonnes = csv.DictReader(documents,delimiter=";")
for ligne in lecture_abonnes:
    abonnes.append(dict(ligne))
print(abonnes)
documents.close()

def disponibilité(livredemande):
    rep = [l["nombres de jour avant le retour"] for l in livres if l["Titre"]==livredemande]
    return int(rep[0])

def liste_emprunt(nomadh,prenomadh):
    numad=[l["Référence"] for l in abonnes if l["Nom"]==nomadh and l["Prénom"]==prenomadh]
    print(numad)
    num = numad[0]
    liste_emprunt=[(l["Titre"],l["nombres de jour avant le retour"]) for l in livres if l["Emprunte"]==num]
    for i in range(len(liste_emprunt)):
        print("vous avez emprunté" + liste_emprunt[i][0]+".Il vous reste"+liste_emprunt[i][1]+" pour le rendre")