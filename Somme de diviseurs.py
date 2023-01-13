n=int(input("Entrez un nombre: "))
liste=[]
S=0
for i in range(1,n+1):
    if n%i==0:
        S += i
        liste.append(i)
print(liste)
print("La somme des diviseurs de ",n," est:",S)

