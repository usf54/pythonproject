rext=int(input("saisir le rayon du disque ext : "))
pi=3.14
sext=pi*rext*rext
print(sext)
rint=int(input("saisir le rayon du disque int  : "))
sint=pi*rint*rint
print(sint)
a=sext-sint
print("La surface est du disque découpé est : ",a)