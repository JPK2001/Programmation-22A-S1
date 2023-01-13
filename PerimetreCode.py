import math
print("Veuillez choisir l'une des formes geometriques suivantes.")
print("TAPEZ: 1 pour cercle, 2 pour carre ou 3 pour rectangle")
geoform=int(input("SAISIR ICI VOTRE SELECTION: "))
if geoform==1:
    r=float(input("Veuillez saisir le rayon r de votre cercle: "))
    p=2*(math.pi)*r
    print("Le perimetre de votre cercle est: ",p)
elif geoform==2:
    c=float(input("Veuillez saisir le cote c de votre carre: "))
    p=4*c
    print("Le perimetre de votre carre est: ", p)
else:
    L=float(input("Veuillez saisir la longueur L du rectangle: ",))
    l=float(input("Veuillez saisir la largeur l du rectangle: "))
    p=(L+l)*2
    print("Le perimetre de votre rectangle est: ", p)