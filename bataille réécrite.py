import random 

class identification:
    def __init__(self) :
       pass
        
    def valeurdelacarte(carte):#methode pour determiner la valeur d'une carte 
        if carte%13 == 0:
            valeur = "deux"
        elif carte%13 == 1:
            valeur = "trois"
        elif carte%13 == 2:
            valeur = "quatre"
        elif carte%13 == 3:
            valeur = "cinq"
        elif carte%13 == 4:
            valeur = "six"
        elif carte%13 == 5:
            valeur = "sept"
        elif carte%13 == 6:
            valeur = "huit"
        elif carte%13 == 7:
            valeur = "neuf"
        elif carte%13 ==8:
            valeur = "dix"
        elif carte%13 == 9: 
            valeur = "valet"
        elif carte%13 == 10: 
            valeur = "dame"
        elif carte%13 == 11:
            valeur = "roi"
        elif carte%13 == 12:
            valeur = "as"
        return valeur 


    def couleurdelacarte(carte): #methode pour determiner la couleur d'une carte 
        if carte <= 12:
            couleur = "coeur"
        elif 13 <= carte and carte <= 27:
            couleur = "pique"
        elif 28 <= carte and carte <=40:
            couleur = "carreau"
        elif 41 <= carte:
            couleur = "trefle"
        return couleur


class distribution :# repartition du paquet de carte entre les 2 joueurs
    def __init__(self):
        self.paquet = list(range(0,52,1))#le paquet entier
        self.mainj1 = list(range(0,26,1))#la main du j1
        self.mainj2 = list(range(0,26,1))#la main du j2
        
 
    def mainjoueurs (self):
        for i in range(52):
            cartetiree = random.choice(self.paquet)#on tire une carte aleatoire du paquet 
            self.paquet.remove(cartetiree)#on enleve la carte tiree du paquet 
            if i < 26: #les 26 premieres cartes 
                self.mainj1[i] = cartetiree #on les donne a j1
                
            else:#les 26 suivantes a j2
                self.mainj2[i-26] = cartetiree

        for i in range(26): #pour annoncer les contenus des paquets qui vont s'affronter 
            print(identification.valeurdelacarte(self.mainj1[i]),identification.couleurdelacarte(self.mainj1[i]))
        print("\n\ncontre\n\n")
        for i in range(26):
            print(identification.valeurdelacarte(self.mainj2[i]),identification.couleurdelacarte(self.mainj2[i]))
            

class combat :

    def __init__(self,mainj1,mainj2) :
        self.transfert1 = mainj1[0]#la premiere carte du paquet de j1
        self.transfert2 = mainj2[0]#la premiere carte du paquet de j2
        self.transfert3 = mainj1[0:3]#les trois premieres cartes du paquet de j1 ( en cas de bataille)
        self.transfert4 = mainj2[0:3]
        self.gagnant = None
        
    def confrontation(self):
        
        print (identification.valeurdelacarte(self.transfert1),"de", identification.couleurdelacarte(self.transfert1)) 
        print("vs")
        print( identification.valeurdelacarte(self.transfert2),"de",identification.couleurdelacarte(self.transfert2)) #on dit quelle carte se bat contre quelle carte 
        
        if self.transfert1%13>self.transfert2%13:
            self.gagnant = 1#self.gagnant permet d'identifier le resultat de la confrontation  
        elif self.transfert1%13<self.transfert2%13:
            self.gagnant = 2
        elif self.transfert1%13 == self.transfert2%13:
            self.gagnant = 3

    def joueur1gagnant(self,mainj1,mainj2): #se lance si self.gagnant = 1
        print("joueur 1 l'emporte")
        del(mainj1[0]) 
        del(mainj2[0]) #on retire les premieres cartes des 2 paquets 
        mainj1.append(self.transfert1)
        mainj1.append(self.transfert2)# on les met au fond du paquet de j1

    def joueur2gagnant(self,mainj1,mainj2):# se lance si self.gagnant = 2 
        print("joueur 2 l'emporte")
        del(mainj1[0])
        del(mainj2[0])#on retire les premieres cartes des 2 paquets 
        mainj2.append(self.transfert2)
        mainj2.append(self.transfert1)# on les met au fond du paquet de j2

    def bataille(self,mainj1,mainj2):#se lance si self.gagnant = 3
        print("bataille !")

        if len(mainj1)<=2: # si j1 n'a pas 3 cartes il ne peut pas participer a la bataille 
            print(" j1 ne peut pas assumer la bataille ")
            random.shuffle(mainj2) # on mélange le jeu de j2 et qui sait, peut etre une remontada (c'est jamais arrivé)
            return
            
        if len(mainj2)<=2:#même chose avec j2
            print(" j2 ne peut pas assumer la bataille ")
            random.shuffle(mainj1)
            return
            

        print (identification.valeurdelacarte(mainj1[2]),"de", identification.couleurdelacarte(mainj1[2])) #on dit aux joeurs que les cartes du haut de leurs paquets s'affrontent, et on leur dit la valeur de leurs cartes
        print("vs")
        print( identification.valeurdelacarte(mainj2[2]),"de",identification.couleurdelacarte(mainj2[2]))

        if ((mainj1[2])%13) > ((mainj2[2])%13):
            print("j1 emporte la bataille")
            del(mainj1[0:3])
            del(mainj2[0:3])
            mainj1.extend(self.transfert4)
            mainj1.extend(self.transfert3)

        elif ((mainj1[2])%13) == ((mainj2[2])%13):
            print("double bataille !!!!!")
            print("c'est hors jeu reprennez vos cartes !")
            del(mainj1[0:3])
            del(mainj2[0:3])
            mainj1.extend(self.transfert3)
            mainj2.extend(self.transfert4)

        elif ((mainj1[2])%13) < ((mainj2[2])%13):
            print("j2 emporte la bataille")
            del(mainj1[0:3])
            del(mainj2[0:3])
            mainj2.extend(self.transfert3)
            mainj2.extend(self.transfert4)
            
                    
distributionjeu = distribution()
distributionjeu.mainjoueurs()
mainjoueur1 = distributionjeu.mainj1
mainjoueur2 = distributionjeu.mainj2
while 0==0 : #le jeu continue tant qu'un joueur n'a pas toute les cartes, voir L 167 et L 172
    match = combat(mainjoueur1,mainjoueur2)
    match.confrontation()
    if match.gagnant == 1:
        match.joueur1gagnant(mainjoueur1,mainjoueur2)
    elif match.gagnant == 2:
        match.joueur2gagnant(mainjoueur1,mainjoueur2)
    elif match.gagnant == 3:
        match.bataille(mainjoueur1,mainjoueur2)

    print(mainjoueur1)
    print(mainjoueur2)
    print(len(mainjoueur1))
    print(len(mainjoueur2))
    
    if len(mainjoueur1) == 52:
        print("joueur 1 a gagné")
        break
    if len(mainjoueur2) == 52:
        print("joueur 2 a gagné ")
        break
        
        


