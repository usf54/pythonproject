a=int(input("saisir in nombre: "))
b=int(input("saisir in nombre: "))
pgcd=float
if a*b>0:
    if a> b:
        print(pgcd==a-b,a)
    elif a<b:
        print( pgcd==a,b-a)
    else:
        print(pgcd==a )