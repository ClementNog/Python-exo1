for i in range(0,40,2):
    print(i)

lettre = input("entrez une lettre")
chaine = input("entrez une chaine de caractère")
cpt=0
for i in range(0, len(chaine)):
    if chaine[i] == lettre:
        cpt+=1

print(cpt)

def table(nombre, i):
    y = nombre * i
    return y
nombre = int(input("entrez un nombre"))
for p in range(0,11):
    print(table(nombre,p))


nombre = int(input("choisissez un nombre"))
for i in range(1,nombre+1):
    if ((nombre%i)==0):
        print(i)

poid = float(input("donnez votre poids"))
taille = float(input("donnez votre taille"))
imc = poid//(taille**2)
print(str(imc))