# Exercice 1

moyenne = int(input("Quelle est votre moyenne?"))
if moyenne >=16:
    print("Mention Trés Bien")
elif moyenne >=14:
    print("Mention Bien")
elif moyenne >=12:
    print("Mention Assez Bien")
elif moyenne >=10:
    print("Admis")
else:
    print("Refusé")
    
# Exercice 2:
genre= input("Indiquer votre genre (M ou F)")
nom= input("Indiquer votre nom")
if genre =="M":
    print("Cher Monsieur ",nom)
elif genre =="F":
    print("Chère Madame ", nom)
else:
    print("Je n'ai pas identifié votre genre", nom)

#Exercice 3
n=int(input("Entrer l'entier n"))
somme = 0
for i in range(n+1):
    somme = somme + i
print(somme)

# Exercice 4:
somme = float(input("Quelle somme voulez vous placer?"))
for i in range(10):
    somme = somme *1.02
print("Dans 10 ans, vous aurez," ,somme, "euros sur votre compte.")

# Exercice 5:
année = 0
loyer = 8
while loyer <12:
    loyer = loyer *1.05
    année = année +1
print("le loyer au m² aura dépassé 12€ dans ",année," ans.")

# Exercice 6:
n = int(input("Entrer votre nombre"))
nb_div = 0
i = 1
while nb_div < 3 and i <= n:
    if n%i == 0:
        nb_div = nb_div +1
    i = i+1
if nb_div == 2:
    print("le nombre ",n,"est premier")
else:
    print("le nombre ",n,"n'est pas premier.")

# Exercice 7:
multiple = 13
for i in range(0,51):
    if multiple*i%7 == 0:
        print(multiple *i)
        
# Exercice 8
#question 1
n = int(input("Entrer un nombre n"))
rep = "*"
for i in range(n):
    rep = rep +"*"
print(rep)

# question 2
n = int(input("Entrer un nombre n"))
for i in range(n):
    rep = "*"
    for j in range(n):
        rep = rep +"*"
    print(rep)

# question 3
n = int(input("Entrer un nombre n"))
rep = ''
for i in range(n):
    rep = rep +"*"
    print(rep)
    
# question 4
n = int(input("Entrer un nombre n"))

for i in range(n,0,-1):
    print("*"*i)