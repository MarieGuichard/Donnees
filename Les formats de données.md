# Les formats de données. 

## I. Données structurées. 

Une donnée est une valeur représentant une information. 

Afin de pouvoir les utiliser, les données sont structurées, c'est à dire sont organisées sous forme d'un tableau appelé table de données. 

La première ligne décrit la forme des lignes suivantes: ce sont les descripteurs. 

Les lignes suivantes sont  appelées des objets: elles sont la liste des valeurs de chacun des descripteurs. 

Prenons un exemple:

| Nom       | Prenom  | DatedeNaissance | Classe |
| --------- | ------- | --------------- | ------ |
| Elhadjen  | Djawed  | 14/10/2008      | 2d3    |
| Grastier  | Camille | 22/01/2008      | 2d4    |
| Monnier   | Logan   | 16/02/2008      | 2d3    |
| Parker    | Pierre  | 01/03/2008      | 2d5    |
| Quenardel | Elise   | 31/12/2008      | 2d5    |

**Exercice 1**:Compléter avec les mots suivants: descripteurs, objets et valeurs. 

a. Nom est .............

b. Logan est ...............

c. La première ligne correspond à l'ensemble des .............;

d. La troisième ligne correspond à un exemple parmi l'ensemble des ................

## II. Données personnelles. 

Une donnée personnelle est toute information se rapportant à une personne physique identifiée ou identifiable. Mais, parce qu’elles concernent des personnes, celles-ci doivent en conserver la maîtrise.

Une personne physique peut être identifiée :

- directement (exemple : nom et prénom) ;
- indirectement (exemple : par un numéro de téléphone ou de plaque d’immatriculation, un identifiant tel que le numéro de sécurité sociale, une adresse postale ou courriel, mais aussi la voix ou l’image).

L’identification d’une personne physique peut être réalisée :

- à partir d’une seule donnée (exemple : nom) ;
- à partir du croisement d’un ensemble de données (exemple : une femme vivant à telle adresse, née tel jour et membre dans telle association).



## III. Formats de données. 

Pour pouvoir stocker, transmettre et exploiter ce type de tableau de valeurs, il peut être représenté sous différentes formes appelées **format**.

Les principaux formats utilisés pour représenter un ensemble de données sont le CSV , le JSON et le XML.

#### 1. Le CSV. 

**Comma-separated values**, connu sous le sigle *CSV*, est un format texte ouvert représentant des données tabulaires sous forme de valeurs séparées par des virgules, des points virgules ou des tabulations. 

En CSV, les données sont stockées dans un fichier texte :

- où la première ligne donne la liste des descripteurs, ,
- où chaque autre ligne du tableau correspond à un objet,
- où les valeurs (d'un objet) sont séparées par une virgule.

Exemple: Voici comment sont écrites les données du tableau précédent au format CSV. 

```csv
Nom, Prenom, DatedeNaissance, Classe
Elhadjen, Djawed, 14/10/2008, 2d3
Grastier, Camille, 22/01/2008, 2d4
Monnier, Logan , 16/02/2008, 2d3
Parker, Pierre, 01/03/2008, 2d5
Quenardel, Elise, 31/12/2008, 2d5
```

**Exercice 2:** 

a. Quel est le séparateur utilisé dans cet exemple ? 

b. Comment feriez vous pour ajouter l'élève Zabu Gaspard, né le 30/11/2008 appartenant à la classe 2d4 ? 

#### 2. Le JSON. 

**JavaScript Object Notation**, connu sous le sigle JSON , est un format léger d'échange de données. Il est facile à lire ou à écrire pour des humains. Il est basé sur un sous-ensemble du langage de programmation Javascript. 

Voici comment sont écrites les données du tableau de l'exercice précédent au format JSON:

```json
{
    {
    "Nom":"Elhadhjen",
    "Prenom": "Djawed",
    "DateDeNaissance":"14/10/2008",
    "Classe":"2d3"
	}
	{
    "Nom":"Grastier",
    "Prenom": "Camille",
    "DateDeNaissance":"22/01/2008",
    "Classe":"2d4"
	}
	{
    "Nom":"Monnier",
    "Prenom": "Logan",
    "DateDeNaissance":"16/02/2008",
    "Classe":"2d3"
	}
    "Nom":"Parker",
    "Prenom": "Pierre",
    "DateDeNaissance":"01/03/2008",
    "Classe":"2d5"
	}
}
```

**Exercice 3:**: 

a. Comment sont utilisés les descripteurs en JSON ? 

b. Compléter le code précédent afin d'ajouter l'élève Elise Quenardel. 

#### 3. Le format XML.

L'eXtensible Markup Language, connu sous le signe XML, est un langage de balisage. 

Voici comment sont écrites les données du tableau de l'exercice précédent au format XML:

```xml
<eleve>
	<Nom>Elhadjen</Nom>
    <Prenom>Djawed</Prenom>
    <DateDeNaissance>22/01/2008</DateDeNaissance>
    <Classe>2d3</Classe>
</eleve>
<eleve>
	<Nom>Grastier</Nom>
    <Prenom>Camille</Prenom>
    <DateDeNaissance>14/10/2008</DateDeNaissance>
    <Classe>2d4</Classe>
</eleve>
<eleve>
	<Nom>Monnier</Nom>
    <Prenom>Logan</Prenom>
    <DateDeNaissance>16/02/2008</DateDeNaissance>
    <Classe>2d3</Classe>
</eleve>
<eleve>
	<Nom>Parker</Nom>
    <Prenom>Pierre</Prenom>
    <DateDeNaissance>01/03/2008</DateDeNaissance>
    <Classe>2d5</Classe>
</eleve>
```

Le format XML avec son système de balises est plus long à écrire mais permet une bonne interopérabilité entre des systèmes d'informations hétérogènes. Il est aussi plus rapide à traiter par la machine.

**Exercice 4:**: 

a. Comment sont utilisés les descripteurs en XML? 

b. Compléter le code précédent afin d'ajouter l'élève Elise Quenardel. 
