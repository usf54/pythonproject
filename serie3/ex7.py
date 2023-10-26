nbr=int(input("saisir un nombre entre 10 et 20: "))   
while nbr<10 or nbr>20:
    if nbr<10:
        print("plus grand!")
    elif nbr>20:
        print("plus petit!")

    nbr=int(input("saisir un nombre entre 10 et 20: "))
print("bravo")