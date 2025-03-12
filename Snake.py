import random
import pyxel

# On initialise des constantes
COLOR_BG = 13
COLOR_POMME = 9
COLOR_HEAD = 7
COLOR_SNAKE = 8
COLOR_TEXT = 0
# des vecteurs qui représentent les directions
NORD  = (0, -1)
SUD   = (0, 1)
EST   = (1, 0)
OUEST = (-1, 0)

LARGEUR, HAUTEUR = 40, 40

# tableau représentant le serpent
serpent = [[5, 5], [5, 4], [5, 3]]  # initialisation avec un serpent de 3 segments
pomme = [30, 30]

# Direction actuelle du serpent
direction = SUD

# Score du joueur
score = 0

def update_clavier(direction):
    """
    Reçoit les entrées clavier et renvoie la nouvelle direction
    """
    if pyxel.btn(pyxel.KEY_Q):
        print("STOP")
        pyxel.quit()
        return None
    
   # boutons pour la direction, un seul en même temps
    if pyxel.btn(pyxel.KEY_UP):
        return NORD
    elif pyxel.btn(pyxel.KEY_DOWN):
        return SUD
    elif pyxel.btn(pyxel.KEY_LEFT):
        return OUEST
    elif pyxel.btn(pyxel.KEY_RIGHT):
        return EST
        
    return direction

def update_snake(serpent, direction):
    """
     Fait avancer le serpent dans la bonne direction
    serpent: tableau de paires d'entiers, les morceaux du serpent
    direction: NORD, SUD, EST ou OUEST la direction du serpent
    return: tableau de paires d'entiers, le serpent déplacé
    """
    tete = serpent[0].copy()
    tete_x = tete[0]
    tete_y = tete[1]
    
    corps1 = serpent[1]
    corps2 = serpent[2]

    if direction == NORD :
        tete_y = tete_y -1
    
    elif direction == SUD :
        tete_y = tete_y +1
    
    elif direction == EST :
        tete_x = tete_x +1
    
    elif direction == OUEST :
        tete_x = tete_x -1

    tete = [tete_x,tete_y]
    return [tete] + serpent[:-1] 

def update_death(serpent):
    """
    Verifie si le serpent est mort
    serpent: tableau de paires d'entiers, tous les morceaux du serpent
    return: bool, si le serpent est mort
    """
    tete = serpent[0]
    if tete[0] < 0 or tete[0] >= LARGEUR or tete[1] < 0 or tete[1] >= HAUTEUR:
        print("STOP")
        pyxel.quit()
        return None  
    if tete in serpent[1:]:
        print("STOP")
        pyxel.quit()
        return None  
    
    # 1 on vérifie si il y a une collision avec le corp du serpent avec lui même
    # 2 on vérifie si le serpent touche un bord (avec LARGEUR et HAUTEUR)

def eatpomme(serpent):
    global pomme, score, COLOR_SNAKE
    if serpent[0] == pomme:
        pomme[0] = random.randint(0,39)
        pomme[1] = random.randint(0,39)
        serpent.append(serpent[-1])  
        
        score += 1 
        COLOR_SNAKE = random.randint(1,12)
        
def draw():
    # 1 on recolorie le fond
    pyxel.cls(COLOR_BG)
    # 2 on colorie chaque morceau du serpent
    for morceau in serpent:
        pyxel.pset(morceau[0], morceau[1],col = COLOR_SNAKE)
    pyxel.pset(serpent[0][0], serpent[0][1],col = COLOR_HEAD) 
    
    pyxel.pset(pomme[0], pomme[1],col = COLOR_POMME) 
   
    pyxel.text(1, 1, f"Score: {score}", COLOR_TEXT)

def update():
    global serpent, direction, pomme, score
    # 1 update les entrées
    direction = update_clavier(direction)
    serpent = update_snake(serpent, direction)
    death = update_death(serpent)
    eatpomme(serpent)

pyxel.init(LARGEUR, HAUTEUR, title="Snake!", fps=10, display_scale=12, capture_scale=6)
pyxel.run(update, draw)
