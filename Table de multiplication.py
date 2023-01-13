nb=int(input("Saisir une valeur: "))
def tab_multi(nb):
    for i in range(1,11):
        print(nb, "*", i, "=", nb * i)
print(tab_multi(nb))