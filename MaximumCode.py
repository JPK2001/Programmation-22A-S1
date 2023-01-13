X=int(input("Veuillez saisir la valeur de X: "))
Y=int(input("Veuillez saisir la valeur de Y: "))
Z=int(input("Veuillez saisir la valeur de Z: "))
if X>Y and X>Z:
    print("X est le maximum")
elif Y>X and Y>Z:
    print("Y est le maximum")
else:
    print("Z est le maximum")