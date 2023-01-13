Week=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for i in range(len(Week)):
    if Week[i]==Week[4]:
        print("Chouette c'est vendredi")
    elif Week[i]==Week[5] or Week[i]==Week[6]:
        print("Repos ce week-end")
    else:
        print("Au travail")
