def imc():
    poids=float(input("Entrez un poids en kg: "))
    taille=float(input("Entrez une taille en m: "))
    n=poids/taille**2
    print(n)
    if n <= 20:
        print("Votre IMC est bas")
    elif 20 < n < 25:
        print("Votre IMC est normal")
    else:
        print("Votre IMC est haute")
imc()