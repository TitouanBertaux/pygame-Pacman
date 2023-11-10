import pygame

import Joueur


class Dessin:
    def __init__(self):
        self.image_coin = pygame.image.load("images/mur_angle.png")
        self.image_bord = pygame.image.load("images/mur_simple.png")
        self.bord_tourne = pygame.transform.rotate(self.image_bord, 90)
        self.image_angle = pygame.image.load("images/mur_angle.png")
        self.image_angle_90 = pygame.transform.rotate(self.image_angle, 270)
        self.image_angle_180 = pygame.transform.rotate(self.image_angle, 180)
        self.image_angle_270 = pygame.transform.rotate(self.image_angle, 90)
        self.image_bout_b = pygame.image.load("images/mur_bout.png")
        self.image_bout_d = pygame.transform.rotate(self.image_bout_b, 180)
        self.image_bout_q = pygame.transform.rotate(self.image_bout_b, 90)
        self.image_bout_p = pygame.transform.rotate(self.image_bout_b, 270)
        self.image_points = pygame.image.load("images/points.png")
        self.image_trait = pygame.image.load("images/trait.png")
        self.image_trait_90 = pygame.transform.rotate(self.image_trait, 90)
        self.image_trait_180 = pygame.transform.rotate(self.image_trait, 180)
        self.image_trait_270 = pygame.transform.rotate(self.image_trait, 270)
        self.x = 50
        self.y = 50
        self.tailleX = 25
        self.tailleY = 25
        self.lstPosMurs = []
        self.lstPosCases = []
        self.lstCasesVisite = []

    """
        dessiner_murs -> tab : 
            - = mur horizontal
            | = mur vertical
            1 = angle de base
            2 = angle*90°  (sens anti-horaire)
            3 = angle*180°  (sens anti-horaire)
            4 = angle*270°  (sens anti-horaire)
            espace = du vide
            b = mur bout (angle vers le haut)
            d = mur bout (angle vers le bas)
            q = mur bout (angle vers la gauche)
            p = mur bout (angle vers la droite)
            5 = trait normal
            6 = trait*90°
            7 = trait*180°
            8 = trait*270°
    """
    def dessiner_murs(self, tab, screen):
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                for n in range(len(tab[i][j])):
                    if tab[i][j][n] == "1":
                        screen.blit(self.image_angle, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "2":
                        screen.blit(self.image_angle_90, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "3":
                        screen.blit(self.image_angle_180, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "4":
                        screen.blit(self.image_angle_270, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "|":
                        screen.blit(self.image_bord, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "-":
                        screen.blit(self.bord_tourne, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "b":
                        screen.blit(self.image_bout_b, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "d":
                        screen.blit(self.image_bout_d, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "q":
                        screen.blit(self.image_bout_q, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "p":
                        screen.blit(self.image_bout_p, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "5":
                        screen.blit(self.image_trait, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "6":
                        screen.blit(self.image_trait_90, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "7":
                        screen.blit(self.image_trait_180, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "8":
                        screen.blit(self.image_trait_270, (self.x, self.y))
                        self.lstPosMurs.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == "0":
                        screen.blit(self.image_points, (self.x, self.y))
                        self.lstPosCases.append((self.x, self.y))
                        self.x += self.tailleX
                    elif tab[i][j][n] == " ":
                        self.x += self.tailleX
                self.x = 50
                self.y += self.tailleY

    def est_dans_cases(self, pos):
        #prochaine coordonnées du joueur
        posX = pos[0]
        posY = pos[1]
        boolPassage = False
        for i in range(len(self.lstPosCases)):
            if Joueur.player.gauche:
                if self.lstPosCases[i][1] == posY:
                    if self.lstPosCases[i][0] <= posX and self.lstPosCases[i][0] >= posX-self.tailleX:
                        print("gauche OK")
                        return True
            elif Joueur.player.droite:
                if self.lstPosCases[i][1] == posY:
                    if self.lstPosCases[i][0]+self.tailleX >= posX+Joueur.player.tailleX and self.lstPosCases[i][0] <= posX+Joueur.player.tailleX:
                        print("droite OK")
                        return True
            elif Joueur.player.haut:
                if self.lstPosCases[i][0] == posX:
                    if self.lstPosCases[i][1] <= posY and self.lstPosCases[i][1] >= posY-self.tailleY:
                        print("haut OK")
                        return True
            elif Joueur.player.bas:
                if self.lstPosCases[i][0] == posX:
                    if self.lstPosCases[i][1]+self.tailleY >= posY+Joueur.player.tailleY and self.lstPosCases[i][1] <= posY+Joueur.player.tailleY:
                        print("bas OK")
                        return True

        return boolPassage


des = Dessin()

