nbr=int(input("saisir un nombre :"))
if nbr>100:
    k=1
elif nbr<=0:
    print("programme termine.")
i=1
s=nbr
while nbr>0: 
    if nbr>100:
        k+=1 
    i+=1
    s+=nbr
    nbr=int(input("saisir un nombre :"))
print("les nombres saisie sont: ",i," nombres")
print("la somme est: ",s)
print("les nombres superieures a 100 sont:",k)
