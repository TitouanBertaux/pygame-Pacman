import pygame
import dessin
import Joueur

class fantome:

    def __init__(self):
        self.vitesse = 1
        self.image = pygame.image.load("./images/fantome.png")
        self.position = self.image.get_rect()
        self.position.x = 675
        self.position.y = 625
        self.tailleX = 25
        self.tailleY = 25
        self.vaGauche = False
        self.vaDroite = False
        self.vaHaut = False
        self.vaBas = False
        self.count = 0

    def est_dans_cases(self, pos):
        #prochaine coordonnées du joueur
        posX = pos[0]
        posY = pos[1]
        boolPassage = False
        for i in range(len(dessin.des.lstPosCases)):
            if dessin.des.lstPosCases[i][1] == posY:
                if dessin.des.lstPosCases[i][0] <= posX and dessin.des.lstPosCases[i][0] >= posX-dessin.des.tailleX:
                    print("gaucuuhhhhhhhhhhhhhhhhhhhhhhhhh")
                    return True
            if dessin.des.lstPosCases[i][1] == posY:
                if dessin.des.lstPosCases[i][0]+dessin.des.tailleX >= posX+Joueur.player.tailleX and dessin.des.lstPosCases[i][0] <= posX+Joueur.player.tailleX:
                    print("droite OK")
                    return True
            if dessin.des.lstPosCases[i][0] == posX:
                if dessin.des.lstPosCases[i][1] <= posY and dessin.des.lstPosCases[i][1] >= posY-dessin.des.tailleY:
                    print("haut OK")
            if dessin.des.lstPosCases[i][0] == posX:
                if dessin.des.lstPosCases[i][1]+dessin.des.tailleY >= posY+Joueur.player.tailleY and dessin.des.lstPosCases[i][1] <= posY+Joueur.player.tailleY:
                    print("bas OK")
                    return True
        return boolPassage

    def direction(self):
        gauche = False
        droite = False
        haut = False
        bas = False
        self.vaGauche = False
        self.vaDroite = False
        self.vaHaut = False
        self.vaBas = False

        #gauche
        if (self.est_dans_cases((self.position.x - self.vitesse, self.position.y))):
            gauche = True
        #droite
        if (self.est_dans_cases((self.position.x + self.vitesse, self.position.y))):
            droite = True
        #haut
        if (self.est_dans_cases((self.position.x, self.position.y - self.vitesse))):
            haut = True
        #bas
        if (self.est_dans_cases((self.position.x, self.position.y + self.vitesse))):
            bas = True

        aBouger = False
        if gauche and not aBouger:
            if Joueur.player.position.x < self.position.x:
                self.vaGauche = True
                aBouger = True
                self.count = 25
        if droite and not aBouger:
            if Joueur.player.position.x > self.position.x:
                self.vaDroite = True
                aBouger = True
                self.count = 25
        if haut and not aBouger:
            if Joueur.player.position.y < self.position.y:
                self.vaHaut = True
                aBouger = True
                self.count = 25
        if bas and not aBouger:
            if Joueur.player.position.y > self.position.y:
                self.vaBas = True
                aBouger = True
                self.count = 25

        if aBouger == False:
            if gauche:
                self.vaGauche = True
                aBouger = True
                self.count = 25
            elif droite:
                self.vaDroite = True
                aBouger = True
                self.count = 25
            elif haut:
                self.vaHaut = True
                aBouger = True
                self.count = 25
            elif bas:
                self.vaBas = True
                aBouger = True
                self.count = 25



ghost = fantome()