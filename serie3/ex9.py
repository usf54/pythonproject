nbr=int(input("saisir un nombre : "))
d=0
if nbr>0:
    for i in range(1,nbr+1):
        if nbr%i==0:
            print("ce nombre est divise par ",i)
            d+=1  
        
if d==2:
    print("ce nombre est premier")
else:
    print("ce nombre n'est pas premier")