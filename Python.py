import random

v = random.randint(0, 5)
z = random.randint(0, 5)

x = 6
y = 9

while x!=z or y!= v:
    x = int(input("entrez le numero de la colonne, entre 1 et 5 : "))
    y = int(input("entrez le numero de la ligne, entre 1 et 5 : "))
    while(x > 5):
	    x = int(input("entrez le numero de la colonne, entre 1 et 5"))
    while(y > 5 ):
	    y = int(input("entrez un nombre entre 1 et 5"))
    if (x==z and y==v):
	    print("Touché")
    elif (x!=z and y!=v):
	    print("A l'eau")
    elif (x!=z or y !=v):
        print("En vue")