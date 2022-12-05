from random import randrange

h=input("0 pour quitter et n'importe quelle autre touche pour continuer: ")
while h!="0":



  
    nombre_secret = randrange(1,501)#nombre_secret
    
        
    print("vous devez entrer un nombre compris entre 1 et 500.\n ")     
    essaie=5  
    while  essaie >=1 :
        nombre_choisi = int(input("Entrez un nombre: "))
        if nombre_choisi == nombre_secret  :
            print("vous avez gagne")
            break
        
        else  :
            if nombre_choisi<nombre_secret :
                print("Le nombre choisi est inferieur au nombre secret.")
                print("Entrez un nombre a nouveau.")
        
            else : 
                print("le nombre choisi est superieur au nombre secret.")
                print("Entrez un nombre a nouveau.")
            
        essaie -= 1
        print("Nombre d'essaies restants: ",essaie)
        
     
    print("Le nombre secret etait:", nombre_secret )   
    h=input("0 pour quitter et n'importe quelle autre touche pour continuer: ")  
 

    
    

        