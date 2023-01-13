exa=int(input("Entrez la note d'examen: "))
td=int(input("Entrez la note de td: "))
tp=int(input("Entrez la note de tp: "))
moy=(3/5)*exa+(1/5)*td+(1/5)*tp
print("La moyenne finale est: ",moy)
if moy<10:
    print("Ajourné")
elif moy>=10 and moy<12:
    print("Admis Mention Passable")
elif moy>=12 and moy<14:
    print("Admis Mention Assez Bien")
elif moy>=14 and moy<16:
    print("Admis Mention Bien")
elif moy>=16 and moy<=20:
    print("Admis Mention Tres Bien")