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
#############################################
#definition des constantes(M)
p = 0.5
n = 4
T = 5
k = 1
HEIGHT = 800
WIDTH = 800

#############################################
#definition des variables globales
#############################################
#definition des fonctions


def grille():
    """génération de la grille"""
    for i in range(50):
        for j in range(50):
            pos1x = i * (WIDTH/50)            
            pos1y = j * (HEIGHT/50)
            pos2x = (i + 1)*(WIDTH/50)
            pos2y = (j + 1)*(HEIGHT/50)
            if (((i + j) % 2) ==0):
                case_terre = grillage.create_rectangle((pos1x, pos1y), (pos2x, pos2y), fill = "brown")
            else:
                case_eau = grillage.create_rectangle((pos1x, pos1y), (pos2x, pos2y), fill = "blue")
    pass


def case_terre_eau():
    """definit les cases terre ou eau aléatoirement"""
    pass


def voisin(T):
    """si la valeur du voisinage est supérieure ou égale à T, alors une case reste ou est convertie en eau et vice vers ca"""
    pass

def personnage():
 """le personnage sera représenté sous forme de cercle"""

#############################################
#programme principal
racine = tk.Tk()
grillage = tk.Canvas(racine, bg = "white", width = WIDTH, height = HEIGHT)
grillage.grid()
grille()
racine.mainloop()
#############################################
