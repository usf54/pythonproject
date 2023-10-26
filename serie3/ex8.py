N=int(input("saisir le nombre d'entiers :"))
s=0
i=0
for i in range(N):
    entier=int(input("saisir un entier :"))
    i+=1
    s+=entier
m=s/i
print("la somme est : ",s)
print("la moyenne est : ",m)