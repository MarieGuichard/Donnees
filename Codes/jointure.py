import csv

def jointures(t1,t2,cle1,cle2=None):
    table1=[]
    tab1 = open(t1,newline="",encoding="ISO-8859-15")
    lecture = csv.DictReader(tab1,delimiter=";")
    for ligne in lecture:
        table1.append(dict(ligne))
    tab1.close()
    table2=[]
    tab2=open(t2,newline="")
    lecture=csv.DictReader(tab2,delimiter=";")
    for ligne in lecture:
        table2. append(dict(ligne))
    tab2.close()
    if cle2==None:
        cle2 = cle1
    new_table=[]
    for ligne1 in table1:
        for ligne2 in table2:
            print(ligne2)
            print(ligne1[cle1])
            print(ligne2[cle2])
            if ligne1[cle1] == ligne2[cle2]:
                new_ligne = ligne1
                for cle in ligne2:
                    if cle!=cle2:
                        new_ligne[cle]=ligne2[cle]
                new_table.append(new_ligne)
    return new_table

def vers_csv(matable,nomdunvfich):
    table=matable
    nom_champ = table[1].keys()
    with open(nomdunvfich+'.csv','w',newline='')as fic:
        dic=csv.DictWriter(fic,fieldnames=nom_champ,delimiter=";")
        dic.writeheader()
        for ligne in table:
            dic.writerow(ligne)
    return None 