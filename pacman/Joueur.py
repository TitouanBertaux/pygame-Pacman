import pygame

class joueur:

    def __init__(self):
        self.vie = 3
        self.vitesse = 1
        self.image = pygame.image.load("./images/pacman.png")
        self.position = self.image.get_rect()
        self.position.x = 75
        self.position.y = 75
        self.tailleX = 25
        self.tailleY = 25
        self.gauche = False
        self.droite = False
        self.haut = False
        self.bas = False
        self.prochainCoup = ""
        self.points = 0

player = joueur()
