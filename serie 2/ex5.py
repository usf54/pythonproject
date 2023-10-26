mh=int(input("saisir les montants des heures supplémentaires: "))
if mh<=39:
    print("les  heures sans suppplement")
elif mh>=40 and mh<=44 :
    print("les heures sont majorées de 50%",mh*0.5)  

elif mh>=45 and mh<=49 :
    print("les heures sont majorées de 75%",mh*0.75)
    
elif mh>=50 :
    print("les heures sont majorées de 100%",mh*1)