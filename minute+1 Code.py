h=int(input("Veuillez entrez une heure valide: "))
m=int(input("Veuillez entrer les minutes valides: "))
if h==24:
    h=00
if m==59:
    m=00
    h=h+1
else:
    m=m+1
print("Il est: ",h,"heures et",m,"minutes")