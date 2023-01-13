def fibo():
    n = int(input("Saisir une valeur: "))
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
fibo()