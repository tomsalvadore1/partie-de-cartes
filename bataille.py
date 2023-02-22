import random 


def valeurdelacarte(a):#fonction qui attribue un chiffre a sa valeur en tant que carte (il y a 13 types de cartes)
    if a%13 == 0:
        b = "deux"
    if a%13 == 1:
        b = "trois"
    if a%13 == 2:
        b = "quatre"
    if a%13 == 3:
        b = "cinq"
    if a%13 == 4:
        b = "six"
    if a%13 == 5:
        b = "sept"
    if a%13 == 6:
        b = "huit"
    if a%13 == 7:
        b = "neuf"
    if a%13 ==8:
        b = "dix"
    if a%13 == 9: 
        b = "valet"
    if a%13 == 10: 
        b = "dame"
    if a%13 == 11:
        b = "roi"
    if a%13 == 12:
        b = "as"
    return b 


def couleurdelacarte(cartetirée):#meme chiose avec les 4 couleurs de carte 
    if cartetirée <= 13:
        c = "coeur"
    if 14 <= cartetirée and cartetirée <= 26:
        c = "pique"
    if 27 <= cartetirée and cartetirée <=39:
        c = "carreau"
    if 40 <= cartetirée:
        c = "trefle"
    return c


mainj1 = list(range(0,26,1))#main du joueur 1 est une suite de 26 cartes (un tableau de capacité 26, son contenu n'a pas d'importance, il sera remplacé ) 
print(mainj1)
mainj2 = list(range(0,26,1))#main du joueur 2 est une suite de 26 cartes (un autre tableau de capacité 26)
paquet= (list(range(0,52,1))) # le paquet entier de carte, lui il contient les 52 cartes donc il est bien comme ca (un tableau de capacité 52)
for i in range(52):#on distribue 52 fois 
    print(paquet)
    cartetirée = random.choice(paquet) #on tire un carte aléatoire du paquet 
    print(cartetirée)
    print(couleurdelacarte(cartetirée),valeurdelacarte(cartetirée))
    paquet.remove(cartetirée) #si on tire la carte elle est plus dans le paquet, du coup on l'enleve
    if i < 26:#on distribue les 26 premieres cartes a j1
        mainj1[i] = cartetirée
    if i >= 26:#les 26 suivantes a j2
        mainj2[i-26] = cartetirée
    
print(mainj1)
print(mainj2)
#for i in range(100):
while 0 == 0  :
    transfert1 = [-1]
    transfert2 = [-1]
    print (valeurdelacarte(mainj1[0]),"de", couleurdelacarte(mainj1[0])) #on dit au joueurs que les cartes du haut de leurs paquets s'affrontent, et on leur dit en valeur de carte 
    print("vs")
    print( valeurdelacarte(mainj2[0]),"de",couleurdelacarte(mainj2[0]))
    transfert1[0] = mainj1[0]
    transfert2[0] = mainj2[0]
   

    if ((mainj1[0])%13) > ((mainj2[0])%13): #si la carte du j1 est plus forte que la carte du j2
        
            print("joueur 1 l'emporte")
            del(mainj2[0])
            del(mainj1[0])
            mainj1.extend(transfert1)
            mainj1.extend(transfert2)
            
            


    elif ((mainj1[0])%13) == ((mainj2[0])%13):# si les cartes ont la même valeur 

            print("bataille !")
            transfert3 = [-1 , -1 , -1]
            transfert4 = [-1 , -1 , -1]
            if len(mainj1)<=2:
                print("joueur 1 a perdu sur une bataille ")
                break

            if len(mainj2)<=2:
                print("joueur 2 a perdu sur une bataille ")
                break

            print (valeurdelacarte(mainj1[2]),"de", couleurdelacarte(mainj1[2])) #on dit au joeurs que les cartes du haut de leurs paquets s'affrontent, et on leur dit en valeur de carte
            print("vs")
            print( valeurdelacarte(mainj2[2]),"de",couleurdelacarte(mainj2[2]))

            if ((mainj1[2])%13) > ((mainj2[2])%13):
                print("j1 emporte la bataille")
                transfert3 = mainj1[0:3]
                transfert4 = mainj2[0:3]
                mainj1.extend(transfert3)
                mainj1.extend(transfert4)

            elif ((mainj1[2])%13) == ((mainj2[2])%13):
                print("double bataille §!!!!!")
                print("c'est hors jeu ")

                transfert3 = mainj1[0:3]
                transfert4 = mainj2[0:3]
                mainj1.extend(transfert3)
                mainj2.extend(transfert4)

            elif ((mainj1[2])%13) < ((mainj2[2])%13):
                print("j2 emporte la bataille")
                transfert3 = mainj1[0:3]
                transfert4 = mainj2[0:3]
                mainj2.extend(transfert4)
                mainj2.extend(transfert3)
        

            del(mainj2[0:3])
            del(mainj1[0:3])
            

    elif ((mainj1[0])%13) < ((mainj2[0])%13):

            print("joueur 2 l'emporte") 
            del(mainj2[0])
            del(mainj1[0])
            mainj2.extend(transfert2)
            mainj2.extend(transfert1)
            

    print(mainj1)
    print(mainj2)
    if len(mainj1) == 0:
        print("JOUEUR 1 A PERDU")
        break

    if len(mainj2) == 0:
        print("JOUEUR 2 A PERDU")
        break
   