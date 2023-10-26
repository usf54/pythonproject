note=float(input("saisir la note: "))
if note>14 and note<16:
    print("mention bien")
elif note<12 and note>=10:
    print("mention passable")
elif note<10 :
    print("mediocre")