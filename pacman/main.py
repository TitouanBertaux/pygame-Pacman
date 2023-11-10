import pygame
import Joueur
import dessin
import Fantome
import time

pygame.init()

tab_map = [
    ["1------------8------------2"],
    ["|000000000000|000000000000|"],
    ["|01--201---20|01---201--20|"],
    ["|0|  |0|   |0|0|   |0|  |0|"],
    ["|04--304---30d04---304--30|"],
    ["|0000000000000000000000000|"],
    ["|0q-p0b0q----8----p0b0q-p0|"],
    ["|00000|000000|000000|00000|"],
    ["4---205----p0d0q----701---3"],
    ["    |0|0000000000000|0|    "],
    ["    |0|01---------20|0|    "],
    ["    |0d0|         |0d0|    "],
    ["    |000|         |000|    "],
    ["    |0b0|         |0b0|    "],
    ["    |0|04---------30|0|    "],
    ["    |0|0000000000000|0|    "],
    ["1---30d0q----8----p0d04---2"],
    ["|000000000000|000000000000|"],
    ["|0q-20q----p0d0q----p01-p0|"],
    ["|000|00000000000000000|000|"],
    ["5-p0d0b0q----8----p0b0d0q-7"],
    ["|00000|000000|000000|00000|"],
    ["|0q---6----p0d0q----6---p0|"],
    ["|0000000000000000000000000|"],
    ["4-------------------------3"]
]
pygame.display.set_caption("Pacman")
screen = pygame.display.set_mode((1000, 700))

screen.blit(Joueur.player.image, Joueur.player.position)
pygame.display.flip()
dessin.des.dessiner_murs(tab_map, screen)
font = pygame.font.Font('freesansbold.ttf', 12)
score = font.render("score : " + str(Joueur.player.points), True, (255, 255, 255))

running = True
print(dessin.des.lstPosCases)
while running:
    pygame.draw.rect(screen, (0, 0, 0), Joueur.player.position)
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, score.get_width(), score.get_height()))
    pygame.draw.rect(screen, (0, 0, 0), Fantome.ghost.position)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            # droite
            if keys[pygame.K_RIGHT]:
                Joueur.player.prochainCoup = "droite"
            # gauche
            if keys[pygame.K_LEFT]:
                Joueur.player.prochainCoup = "gauche"
            # haut
            if keys[pygame.K_UP]:
                Joueur.player.prochainCoup = "haut"
            # bas
            if keys[pygame.K_DOWN]:
                Joueur.player.prochainCoup = "bas"
            # infos
            if keys[pygame.K_SPACE]:
                print("haut : ", Joueur.player.haut, "\nbas : ", Joueur.player.bas, "\ngauche : ", Joueur.player.gauche, "\ndroite : ", Joueur.player.droite)

    if Joueur.player.prochainCoup == "gauche":
        sauv1 = Joueur.player.gauche
        sauv2 = Joueur.player.bas
        sauv3 = Joueur.player.haut
        sauv4 = Joueur.player.droite
        Joueur.player.droite = False
        Joueur.player.gauche = True
        Joueur.player.bas = False
        Joueur.player.haut = False
        if(dessin.des.est_dans_cases((Joueur.player.position.x+Joueur.player.vitesse, Joueur.player.position.y))):
            Joueur.player.prochainCoup = ""
        else:
            Joueur.player.gauche = sauv1
            Joueur.player.bas = sauv2
            Joueur.player.haut = sauv3
            Joueur.player.droite = sauv4
    elif Joueur.player.prochainCoup == "droite":
        sauv1 = Joueur.player.gauche
        sauv2 = Joueur.player.bas
        sauv3 = Joueur.player.haut
        sauv4 = Joueur.player.droite
        Joueur.player.droite = True
        Joueur.player.gauche = False
        Joueur.player.bas = False
        Joueur.player.haut = False
        if(dessin.des.est_dans_cases((Joueur.player.position.x+Joueur.player.vitesse, Joueur.player.position.y))):
            Joueur.player.prochainCoup = ""
        else:
            Joueur.player.gauche = sauv1
            Joueur.player.bas = sauv2
            Joueur.player.haut = sauv3
            Joueur.player.droite = sauv4
    elif Joueur.player.prochainCoup == "haut":
        sauv1 = Joueur.player.gauche
        sauv2 = Joueur.player.bas
        sauv3 = Joueur.player.haut
        sauv4 = Joueur.player.droite
        Joueur.player.droite = False
        Joueur.player.gauche = False
        Joueur.player.bas = False
        Joueur.player.haut = True
        if(dessin.des.est_dans_cases((Joueur.player.position.x, Joueur.player.position.y-Joueur.player.vitesse))):
            Joueur.player.prochainCoup = ""
        else:
            Joueur.player.gauche = sauv1
            Joueur.player.bas = sauv2
            Joueur.player.haut = sauv3
            Joueur.player.droite = sauv4
    elif Joueur.player.prochainCoup == "bas":
        sauv1 = Joueur.player.gauche
        sauv2 = Joueur.player.bas
        sauv3 = Joueur.player.haut
        sauv4 = Joueur.player.droite
        Joueur.player.droite = False
        Joueur.player.gauche = False
        Joueur.player.bas = True
        Joueur.player.haut = False
        if(dessin.des.est_dans_cases((Joueur.player.position.x, Joueur.player.position.y+Joueur.player.vitesse))):
            Joueur.player.prochainCoup = ""
        else:
            Joueur.player.gauche = sauv1
            Joueur.player.bas = sauv2
            Joueur.player.haut = sauv3
            Joueur.player.droite = sauv4

    time.sleep(0.01)

    if Joueur.player.gauche:
        if(dessin.des.est_dans_cases((Joueur.player.position.x-Joueur.player.vitesse, Joueur.player.position.y))):
            Joueur.player.position.x -= Joueur.player.vitesse
    elif Joueur.player.droite:
        if(dessin.des.est_dans_cases((Joueur.player.position.x+Joueur.player.vitesse, Joueur.player.position.y))):
            Joueur.player.position.x += Joueur.player.vitesse
    elif Joueur.player.haut:
        if(dessin.des.est_dans_cases((Joueur.player.position.x, Joueur.player.position.y-Joueur.player.vitesse))):
            Joueur.player.position.y -= Joueur.player.vitesse
    elif Joueur.player.bas:
        if(dessin.des.est_dans_cases((Joueur.player.position.x, Joueur.player.position.y+Joueur.player.vitesse))):
            Joueur.player.position.y += Joueur.player.vitesse

    xJ = Joueur.player.position.x
    yJ = Joueur.player.position.y
    for i in dessin.des.lstPosCases:
        if i in dessin.des.lstCasesVisite:
            pass
        else:
            xC = i[0]
            yC = i[1]
            if (yJ == yC and xJ+12 == xC) or (yJ+12 == yC and xJ == xC) or (yJ == yC and xJ-12 == xC) or (yJ-12 == yC and xJ == xC):
                dessin.des.lstCasesVisite.append(i)
                Joueur.player.points += 10

    if Fantome.ghost.count == 0:
        Fantome.ghost.direction()
    if Fantome.ghost.count > 0:
        if Fantome.ghost.vaHaut:
            Fantome.ghost.position.y -= Fantome.ghost.vitesse
        if Fantome.ghost.vaBas:
            Fantome.ghost.position.y += Fantome.ghost.vitesse
        if Fantome.ghost.vaDroite:
            Fantome.ghost.position.x += Fantome.ghost.vitesse
        if Fantome.ghost.vaGauche:
            Fantome.ghost.position.x -= Fantome.ghost.vitesse
        Fantome.ghost.count -= 1


    score = font.render("score : " + str(Joueur.player.points), True, (255, 255, 255))
    screen.blit(Joueur.player.image, Joueur.player.position)
    screen.blit(Fantome.ghost.image, Fantome.ghost.position)
    screen.blit(score, (0, 0))
    pygame.display.flip()
