import pygame #IMPORTATION PYGAME

 # INITIALISATION HAUTEUR / LARGEUR FENÊTRE
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

 # INITIALISATION COULEURS GRILLE
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

def main():
    global SCREEN
    pygame.init() #INITIALISATION PYGAME
    
    # AFFICHAGE FENÊTRE
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # DEFINITION FENÊTRE
    
    run = True
    while run:
        SCREEN.fill(BLACK)  # BACKGROUND COLOR NOIRE
        
        drawGrid() # APPEL FONCTION POUR DESSINER LA GRILLE 
        
        # AJOUT D'ITERATIONS DANS LES EVENEMENTS DEFINIS  PAR PYGAME
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # POUR FERMER LA FENÊTRE
                run = False
                
        pygame.display.update() # MAJ DE L4AFFICHAGE
    
    pygame.quit()
                #sys.exit()
                
    

def drawGrid():
    blockSize = 20 # TAILLE DES CASES
    for x in range (0, SCREEN_WIDTH, blockSize) :
        for y in range (0, SCREEN_HEIGHT, blockSize) :
            # Rect(left, top, width, height)
            rect = pygame.Rect(x, y, blockSize, blockSize)
            # rect(surface, color, rectangle à dessiner, largeur)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
            
if __name__ == "__main__":
    main()