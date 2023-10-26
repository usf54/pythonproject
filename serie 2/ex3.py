number=int(input("entrez un nombre : "))
if number%2==0:
    print(number,"est pair")
elif number%2!=0 and number %3==0:
    print("le nombre est impair ,mais est multiple de 3 ")
else:
    print("le nombre n'est ni pair ni multiple de 3 ")