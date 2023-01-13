n=int(input("Veuillez saisir le nombre de photocopies: "))
if n<11:
    t=n*3
elif n<31:
    t=(10*3)+((n-10)*2)
else:
    t=(10*3)+(20*2)+(n-30)
print("le prix des ",n," photocopies est: ",t,"$")