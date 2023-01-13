print("Veuillez choisir le type de température.")
print("TAPEZ: c pour convertir en dégré celcius ou f pour convertir en dégré fahrenheit")
temp=input("SAISIR ICI VOTRE SELECTION: ")
if temp=="c":
    f=int(input("Veuillez saisir la température à convertir: "))
    c=(f-32)/1.8
    print("La température est: ",c," dégrés celcius")
else:
    c=int(input("Veuillez saisir la température à convertir: "))
    f=(c*1.8)+32
    print("La température est: ",f," dégrés fahrenheit")