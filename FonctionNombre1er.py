nb=int(input("Saisir une valeur: "))
def premier(nb):
    if nb%1==0 and nb%nb==0:
        print(nb," est un nombre premier")
    else:
        print(nb," n'est pas un nombre premier")
print(premier(nb))