import pygame #IMPORTATION PYGAME

pygame.init() #INITIALISATION PYGAME

 # INITIALISATION HAUTEUR / LARGEUR FENÊTRE
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

 # INITIALISATION COULEURS GRILLE
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

# AFFICHAGE FENÊTRE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:

# AJOUT D'ITERATIONS DANS LES EVENEMENTS DEFINIS  PAR PYGAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # POUR FERMER LA FENÊTRE
            run = False

pygame.quit()