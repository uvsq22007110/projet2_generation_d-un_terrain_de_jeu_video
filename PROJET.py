#############################################
# groupe BI1
# Laurie MIALIN
# Fatima AIT IGHIL 
# Cecile FETRE
# Charoline JOSEPH
# Aexis BRIAND
# Mecipssa HESNI
# https://github.com/uvsq22007110/projet2_generation_d-un_terrain_de_jeu_video
#############################################
import tkinter as tk
import random as rd
#############################################
#definition des constantes(M)
p = 0.5
n = 4
T = 5
k = 1
HEIGHT = 800
WIDTH = 800
cpt = 0

#############################################
#definition des variables globales
#############################################
#definition des fonctions


def grille(cases):
    """génération de la grille"""
    CG=coulour_gille(cases)
    for i in range(50):
        for j in range(50):
            pos1x = i * (WIDTH/50)            
            pos1y = j * (HEIGHT/50)
            pos2x = (i + 1)*(WIDTH/50)
            pos2y = (j + 1)*(HEIGHT/50)
            colors=rd.choice(CG)
            CG.remove(colors) 
            case = grillage.create_rectangle((pos1x, pos1y), (pos2x, pos2y), fill = colors)


def coulour_gille(p) :
    """ crée une list de 2500 elements remplit de blue et brown pour générer notre terrain """
    nombre_eau=2500*p
    nombre_terre=2500-nombre_eau
    Lbleu=["blue"]*int(nombre_eau)
    Lbrown=["brown"]*int(nombre_terre)
    Lcolors=Lbleu+Lbrown
    return Lcolors

def voisin(T):
    """si la valeur du voisinage est supérieure ou égale à T, alors une case reste ou est convertie en eau et vice vers ca"""
    pass

def cercle(event):
    """Dessine un rond jaune"""
    global cpt
    rayon = 5
    cpt +=1
    if cpt ==1:
        cercle = grillage.create_oval((event.x-rayon, event.y-rayon),
                                (event.x+rayon, event.y+rayon),
                                fill="yellow")
    else:
        pass
   

def personnage_deplacement():
    """le personnage sera représenté sous forme de cercle, déplacement du personnage""" 
    pass
def personnage_placement():
    """retire et replace le personnage"""
    pass

def valeur_voisinage(k):
    """définit la valeur du voisinage"""
    pass

def choix_parametres():
    """l'utilisateur choisit les paramètres, k, p, n, T"""
    pass

def choix_taille():
    """l'utilisateur choisit la taille de la grille"""
    pass

def annuler_deplacement():
    """annule le déplacement du personnage"""
    pass

def sauvegarde():
    """sauvegarde le terrain généré"""
    pass

def recharge():
    """recharge un nouveau terrain"""
    pass



#############################################
#programme principal
racine = tk.Tk()
grillage = tk.Canvas(racine, bg = "white", width = WIDTH, height = HEIGHT)
grillage.grid()
grillage.bind("<Button-1>", cercle)
grillage.bind("<Up>", haut)
grillage.bind("<Down>", bas)
grillage.bind("<Left>", gauche)
grillage.bind("<Right>", droite)
grille(p)
b=grillage.find_all()
racine.mainloop()
#############################################
