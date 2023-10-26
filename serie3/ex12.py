n=int(input("saisir un nombre: "))
d=0
for i in range(1,n):
    if n%i==0:
        d+=i
if d==n:
    print("le nombre est parfait")
else:
    print("c'est pas parfaits")