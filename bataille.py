import pygame
from pygame.locals import *
from random import*
pygame.init()

class Carte:
    def __init__ (self,Valeur,Couleur,NombrePoint):
        self.val=Valeur
        self.color=Couleur
        self.nbrPoint=NombrePoint

    def dessin_carte(self):
        return ("cartes/"+self.val+"_"+self.color+".gif")

    def __str__ (self):
        aff="Valeur : "+str(self.val)+"\t| Couleur : "+str(self.color)+\
        "\t| Nombre de point :"+str(self.nbrPoint)
        return aff


class Paquet_de_Cartes:
    def __init__ (self,l_cartes=[]):
        self.cartes=l_cartes

    def nbr_cartes(self):
        return len(self.cartes)

    def battre(self):
        shuffle(self.cartes)

    def ajouter(self,x):
        self.cartes.append(x)

    def affichage(self):
        for carte in range(0,self.nbr_cartes()):
            if carte < self.nbr_cartes()-2 :
                print(self.cartes[carte],end=" - ")
            else:
                print("",end="\n")

    def tirer(self):
        if len(self.cartes) > 0:
            carte = self.cartes[0]
            del(self.cartes[0])
            return carte
        else:
            return None

    def distribution(self):
        paquetj1 = Paquet_de_Cartes([])
        paquetj2 = Paquet_de_Cartes([])
        for i in range(26):
            carte = self.tirer()
            paquetj1.ajouter(carte)
            carte = self.tirer()
            paquetj2.ajouter(carte)
        return paquetj1,paquetj2


class Joueur():
    def __init__(self,Nom,Liste_Cartes,Score=0):
        self.nom = Nom
        self.main = Liste_Cartes
        self.score = Score

    def total_point(self):
        for i in range(0,len(self.main)):
            self.score += 1

    def reinit(self):
        self.main = []

def jeu_52_cartes():
    couleur = ["Pique","Trefle","Carreau","Coeur"]
    valeur = ["As","2","3","4","5","6","7","8","9","10","Valet","Dame","Roi"]
    point = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    Liste_cartes = []
    for coul in couleur:
        for j in range(0,len(valeur)):
            Liste_cartes.append( Carte(valeur[j], coul, point[j]) )
    return Liste_cartes


def tour_jeu(J1,J2):
    continuer=True
    while continuer==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                continuer=False
                break
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if J1.main.nbr_cartes() > 0 and J2.main.nbr_cartes() > 0:
                        tirage_J1 = J1.main.tirer()
                        tirage_J2 = J2.main.tirer()
                        fenetre.blit(pygame.image.load(tapis_jeu).convert_alpha(), (0,0))
                        pygame.display.flip()
                        texte1 = font.render(str(J1.nom)+" : ", True, color)
                        fenetre.blit(texte1, (100, 56))
                        pygame.display.flip()
                        texte2 = font.render(str(J2.nom)+" : ", True, color)
                        fenetre.blit(texte2, (1050, 400))
                        pygame.display.flip()
                        fenetre.blit(pygame.image.load(tirage_J1.dessin_carte()).convert_alpha(), (100,100))
                        pygame.display.flip()
                        fenetre.blit(pygame.image.load(tirage_J2.dessin_carte()).convert_alpha(), (1050,448))
                        pygame.display.flip()
                        textec1 = font.render(str(J1.main.nbr_cartes())+" cartes", True, Color("red"))
                        fenetre.blit(textec1, (100, 300))
                        pygame.display.flip()
                        textec2 = font.render(str(J2.main.nbr_cartes())+" cartes", True, Color("red"))
                        fenetre.blit(textec2, (1050, 648))
                        pygame.display.flip()
                        textepts1 = font.render(str(tirage_J1.nbrPoint)+" pts", True, Color("red"))
                        fenetre.blit(textepts1, (300, 160))
                        pygame.display.flip()
                        textepts2 = font.render(str(tirage_J2.nbrPoint)+" pts", True, Color("red"))
                        fenetre.blit(textepts2, (916, 515))
                        pygame.display.flip()

                        if tirage_J1.nbrPoint > tirage_J2.nbrPoint:
                            textetot = font.render(str(J1.nom)+" a gagné ce tirage !", True, color)
                            fenetre.blit(textetot, (500, 350))
                            pygame.display.flip()
                            J1.main.ajouter(tirage_J1)
                            J1.main.ajouter(tirage_J2)

                        elif tirage_J1.nbrPoint < tirage_J2.nbrPoint:
                            textetot = font.render(str(J2.nom)+" a gagné ce tirage !", True, color)
                            fenetre.blit(textetot, (500, 350))
                            pygame.display.flip()
                            J2.main.ajouter(tirage_J1)
                            J2.main.ajouter(tirage_J2)

                        else:
                            textetot = font.render("Bataille !", True, color)
                            fenetre.blit(textetot, (500, 350))
                            pygame.display.flip()

                    else:
                        print("Fin de partie !")
                        if J1.main.nbr_cartes() > 0:
                            print(J1.nom,"a gagné la partie !")
                        elif J2.main.nbr_cartes() > 0:
                            print(J2.nom,"a gagné la partie !")
                        if J1.main.nbr_cartes() == J2.main.nbr_cartes():
                            print(J1.nom,"et",J2.nom,"sont a égalité de points !")



#MAIN
##
##couleur=['piques','trefle','carreau','coeur']
##valeur=['as','2','3','4','5','6','7','8','9','10','valet','dame','roi']
##point=['1','2','3','4','5','6','7','8','9','10','11','12','13']
##
##
##
##jeu=Paquet_de_Cartes(jeu_52_cartes(couleur,valeur,point))
##jeu.battre()
##
##d=jeu.distribution()
##paquet1=d[0]
##paquet2=d[1]
##
##J1=Joueur("Moi",paquet1)
##J2=Joueur("Ordi",paquet2)
##
##paquet1.affichage()
##print("-------------------------------------------------------")
##paquet2.affichage()
##
##
##def tour_jeu(J1,J2):
##    c1=paquet1.tirer()
##    c2=paquet2.tirer()
##    if c1[2]>c2[2]:
##        paquet1.ajouter(c1)
##        paquet1.ajouter(c2)
##        print("joueur 1 gagne la manche")
##    if c1[2]<c2[2]:
##        paquet2.ajouter(c1)
##        paquet2.ajouter(c2)
##        print("joueur 2 gagne la manche")
##    if c1[2]==c2[2]:
##        print("bataille")


titre_fenetre = "Jeu De Carte"
tapis_jeu="cartes/tapis-jeu-bataille.jpg"
color = (217,210,210)
pygame.display.set_caption(titre_fenetre)
fenetre = pygame.display.set_mode((1280,720))
fenetre.blit(pygame.image.load(tapis_jeu).convert_alpha(), (0,0))
pygame.display.flip()
font = pygame.font.Font("Impact.ttf",30)
Liste_cartes = jeu_52_cartes()
Jeu = Paquet_de_Cartes(Liste_cartes)
Jeu.battre()
paquet1,paquet2 = Jeu.distribution()
joueur = Joueur("Vous",paquet1,0)
ordi = Joueur("Ordi",paquet2,0)
tour_jeu(joueur,ordi)


#fermeture fenetre
pygame.display.update()
pygame.time.wait(3000) # attend 3000 ms avant de terminer
pygame.quit()