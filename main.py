# Exercice 1
# temp=6.892
# distance=19.7

# vitesse=distance/temp
# print("La vitesse est de",vitesse,"km/h")

# Exercice 2
# nom = input("Quel est votre nom ?")
# nom = str(nom)
# age = input("Quel est votre age ?")
# age = int(age)

# print("Bonjour",nom,"vous avez",age,"ans")

# Exercice 3
# number = input("Entrez un nombre :")
# number = int(number)

# if number >= 0:
#     print("La racine carrée de",number,"est",number**0.5)
# else:
#     print("Le nombre est négatif")

# Exercice 4
# mot1 = input("Entrez le premier mot :")
# mot2 = input("Entrez le second mot :")

# if len(mot1) < len(mot2):
#     print("Le mot",mot1,"est plus court que",mot2)
# elif len(mot1) > len(mot2):
#     print("Le mot",mot2,"est plus court que",mot1)
# else:
#     print("Les mots sont de même longueur")

# Exercice 5
# pression = input("Entrez la pression :")
# pression = float(pression)
# pSeuil = 2.3
# pSeuil = float(pSeuil)
# volume = input("Entrez le volume :")
# volume = float(volume)
# vSeuil = 4.41
# vSeuil = float(vSeuil)

# if pression > pSeuil and volume > vSeuil:
#     print("Arrêt immédiat")
# elif pression > pSeuil and volume <= vSeuil:
#     print("Augmenter le volume")
# elif pression <= pSeuil and volume > vSeuil:
#     print("Diminuer le volume")
# else:
#     print("Tout va bien")

# Exercice 6
# for i in range(10):
#     mail = input("Entrez votre adresse mail :")
#     if "@" in mail and mail.endswith(".com"):
#         print("Adresse mail valide")
#     else:
#         print("Adresse mail invalide")


# Exercice 7
# count = 10
# for i in range(count):
#     print(i)
#     i+=1

# Exercice 8
# mot = input("Entrez un mot :")
# for i in mot:
#     print(i)

# Exercice 9
# a = 0
# b = 10
# while a < b:
#     a+=1
#     print("A =",a,"et B =",b)

# Exercice 10
# b = input("Entrez un nombre :")
# b = int(b)
# while b > 0:
#     if b%2 != 0:
#         print(b)
#     b-=1

# Exercice 11
# number = input("Entrez un nombre compris entre 1 et 10 compris :")
# number = int(number)

# while number > 10 or number < 1:
#     number = input("Entrez un nombre compris entre 1 et 10 compris :")
#     number = int(number)

# print("Le nombre est",number)

# Exercice 12
# chaine = input("Entrez une chaine de caractère :")
# for i in chaine:
#     print(i)

# liste = [1,2,3,4,5]
# for i in liste:
#     print(i)

# i = 0
# i = int(i)
# for i in range(1,14,3):
#     print(i)

# Exercice 13
# n = input("Entrez un nombre :")
# n = int(n)
# i = 0
# i = int(i)
# while i <= n:
#     if i%2 == 0:
#         print(i)
#     i+=1

# Exercice 15 
# liste =[17, 38, 10, 25, 72]
# liste.sort()
# print(liste)

# liste.append(12)

# liste.reverse()
# print(liste)

# print(liste.index(17))

# liste.remove(38)
# print(liste)

# print(liste[1:3])

# print(liste[:2])

# print (liste[3:])

# print(liste[:])

# Exercice 16
# chaine = input("Entrez une chaine de caractère :")
# chaine = str(chaine)
# chaine = chaine[::-1]
# print(chaine)

# Exercice 17
# chaine = input("Entrez une chaine de caractère :")
# chaine = str(chaine)
# chaine = chaine[::-1]
# if chaine == chaine[::-1]:
#     print("La chaine est un palindrome")
# else:
#     print("La chaine n'est pas un palindrome")

# Exercice 18
# chaine = input("Entrez une chaine de caractère :")
# chaine = str(chaine)
# if "@" in chaine and "." in chaine and len(chaine) - chaine.rfind(".") == 4:
#     print("Adresse mail valide")
# else:
#     print("Adresse mail invalide")

# Exercice 19 
# truc = []
# machin = [0.0,0.0,0.0,0.0,0.0]
# print(truc)
# print(machin)

# Exercice 20
# a = 0
# a = int(a)
# for a in range(0, 4):
#     print(a)

# b = 0
# b = int(b)
# for b in range(4, 8):
#     print(b)

# c = 0
# c = int(c)
# for c in range(2, 9, 2):
#     print(c)

# chose = [0,1,2,3,4,5]
# print(3 in chose)
# print(6 in chose)

# Exercice 21
# nombre = input("Entrez un nombre :")
# nombre = int(nombre)
# count = 0
# count = int(count)

# while count < nombre:

#     caractere = ""
#     caractere = input("Entrez un caractère :")
#     caractere = str(caractere)
#     while len(caractere)> 1:
#         caractere = ""
#         caractere = input("Saisie incorrect, entrez un caractère :")
#         caractere = str(caractere)
#     fichier = open("data.txt", "a")
#     fichier.write(caractere)
#     fichier.close()
#     count+=1

# fichier = open("data.txt", "a")
# fichier.write("\n")
# fichier.close()

# Exercice 22
# fichier = open("data.txt", "r")
# contenu = fichier.read()
# fichier.close()
# contenu = contenu.split("\n")
# for i in contenu:
#     if "@" in i and i.endswith(".com"):
#         print("Adresse mail valide")
#     else:
#         print("Adresse mail invalide")

# Exercice 23
# def compterMots(chaine):
#     chaine = chaine.split(" ")
#     dico = {}
#     for i in chaine:
#         if i in dico:
#             dico[i] += 1
#         else:
#             dico[i] = 1
#     return dico

# chaine = input("Entrez une chaine de caractère :")
# chaine = str(chaine)
# print(compterMots(chaine))

# Exercice 24
# def cube(nombre):
#     return nombre**3

# def volumeSphere(rayon):
#     return 4/3*3.14*cube(rayon)

# rayon = input("Entrez le rayon d'une sphère :")
# rayon = int(rayon)
# print(volumeSphere(rayon))

# Exercice 25
# def somme(a,b,c):
#     return a+b+c

# a = ""
# b = ""
# c = ""

# while a=="":
#     a = input("Entrez la valeure de a :")
#     while not a.isdigit():
#         a = input("Erreur, entrez la valeure de a :")

# while b=="":
#     b = input("Entrez la valeure de b :")
#     while not b.isdigit():
#         b = input("Erreur, entrez la valeure de b :")

# while c=="":
#     c = input("Entrez la valeure de c :")
#     while not c.isdigit():
#         c = input("Erreur, entrez la valeure de c :")

# a = int(a)
# b = int(b)
# c = int(c)
# print(somme(a,b,c))

# tuple = (a,b,c)
# a,b,c = tuple
# print(a,b,c)
















    







