entiers=[]
while True:
    entier=int(input("saisir in entier: "))
    if entier<0:
        break;
    entiers.append(entier)

    plus_petit=min(entiers)
    plus_grand=max(entiers)
    somme=sum(entiers)
    moyenne=somme/len(entiers)

print("plus petit entier est:",plus_petit)
print("plus grand entier est:",plus_grand)
print("la somme est : ",somme)
print("la moyenne est: ",moyenne)