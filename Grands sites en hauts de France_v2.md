# Grands sites en hauts de France. 

## I. Téléchargez les données. 

a. Rendez vous sur le site dédié à l'open data des Hauts de France.  

b. Rendez vous dans la rubrique Environnement.

c. Téléchargez le jeu de données concernant les grands  sites de France en Hauts de France datant de l'année 2020 au format csv  

d. Enregistrez le document dans votre répertoire en le nommant grands_sites.csv

e. Ouvrir le document avec un tableur. 

## II. Le tableur. 

a. Afficher tous les sites ayant un code label égal à 9.  

b. Afficher tous les sites dont le nom du site est la Baie de Somme.  

c. Afficher tous les sites dont les identifiants sont inférieurs à 20.  

d. Afficher tous les sites dont les identifiants sont compris entre 5 et 25, inclus.  

e. Afficher tous les sites dont le code label est 10  ou le nom du site est Les Deux Caps Blanc-Nez, Gris-Nez.  

f. Trier les sites dans l'ordre croissant de l'identifiant.  

g. Trier les sites dans l'ordre alphabétique des nom_min.  

## III. Traiter les données à l'aide de Python. 

Il est possible d'utiliser python pour étudier des données structurées. 

1. Enregistrer le fichier donnees.py dans le même répertoire que le document grands_sites.csv

2. a. Dans le shell, exécutez la commande : `affiche(grands_sites)`

   b. Que fait la fonction `affiche()` ?  

3. a. Dans le shell, exécutez la commande :

   ​	`code_label("9",grands_sites)`

   b. Comparer la réponse obtenue avec la réponse obtenue à la question b de la partie II.

4. Quel est le grand site dont l'identifiant est égal à « 12 » ? Quelle fonction avez vous utilisé ?  

5. Écrire une fonction permettant de renvoyer la liste des grands sites en donnant le nom du site.  

6. Modifier le code de la fonction identifiant afin de pouvoir répondre aux questions c et d de la partie B.   
