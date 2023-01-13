notes=[]
n=int(input("Combien de notes avez-vous? "))
while len(notes)<n:
    a=int(input("Entrez une note: "))
    notes.append(a)
print("Votre moyenne est:",sum(notes)/n)