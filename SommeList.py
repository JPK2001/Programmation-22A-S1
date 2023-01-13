def som_liste():
    l=int(input("Combien de nombres voulez-vous?: "))
    s=0
    for i in range(l):
       n=int(input("Saisir un nombre: "))
       s+=n
    print("La somme de ces nombres est: ",s)
som_liste()
