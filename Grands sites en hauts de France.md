# Grands sites en hauts de France. 



### A: L'Open data.  



1. a. En utilisant le site de la CNIL, rechercher ce qu'est l'open data.

   b. A quelles conditions, des données peuvent-elles être mise en ligne de manière publique ?  

   c. Quelles sont les conditions de réutilisation des données publiées ?  

   

2. a. Rendez vous sur le site dédié à l'open data des Hauts de France.  

   b. Rendez vous dans la rubrique Environnement.

   c. Téléchargez le jeu de données concernant les grands  sites de France en Hauts de France. au format csv  

   d. Enregistrez le document dans votre répertoire en le nommant grands_sites.csv

   

3. a. Ouvrez le document grands_sites.csv en utilisant le bloc-note (faites un clic droit).  

   b. Que contient la première ligne ?  

   c. Que contient la deuxième ligne ? Et la troisième ?  

   c. Par quoi sont séparées les informations ?  



### B: Le tableur



1. a. Après avoir fermé le document grands_sites.csv, ouvrez le à nouveau en utilisant le tableur.  

   b. Décochez les items champ entre guillemets comme texte et Détecter les nombres spéciaux.  

   b. Quel séparateur devez vous sélectionner ?  

   c. Que se passe-t-il si vous sélectionnez le mauvais séparateur ?  

2. Sélectionner une information.  

   Afin de trouver une information rapidement, il est possible d'utiliser les filtres du tableur. Cela est particulièrement utilise lorsque la base de données contient beaucoup d'information.  

   Pour cela, dans le menu données,il faut sélectionner filtre, puis filtre standard.  

   a. Afficher tous les sites ayant un code label égal à 9.  

   b. Afficher tous les sites dont le nom du site est la Baie de Somme.  

   c. Afficher tous les sites dont les identifiants sont inférieurs à 20.  

   d. Afficher tous les sites dont les identifiants sont compris entre 5 et 25, inclus.  

   e. Afficher tous les sites dont le code label est 10  ou le nom du site est Les Deux Caps Blanc-Nez, Gris-Nez.  

3. Trier.  

   Il est parfois utile de trier les informations.  

   Pour cela, dans le menu données, il faut sélectionner trier.  

   a. Trier les sites dans l'ordre croissant de l'identifiant.  

   b. Trier les sites dans l'ordre alphabétique des nom_min.  



**Partie C : Avec python.** 



Il est possible d'utiliser python pour étudier des données structurées. 



1. Enregistrer le fichier donnees.py dans le même répertoire que le document grands_sites.csv

2. a. Dans le shell, exécutez la commande : affiche(grands_sites)

   b. Que fait la fonction affiche() ?  

3. a. Dans le shell, exécutez la commande :

   ​	code_label("9",grands_sites)

   b. Comparer la réponse obtenue avec la réponse obtenue à la question 5.b.

4. Quel est le grand site dont l'identifiant est égal à « 12 » ? Quelle fonction avez vous utilisé ?  

5. Écrire une fonction permettant de renvoyer la liste des grands sites en donnant le nom du site.  

6. Modifier le code de la fonction identifiant afin de pouvoir répondre aux questions 5. c et 5.d.  



