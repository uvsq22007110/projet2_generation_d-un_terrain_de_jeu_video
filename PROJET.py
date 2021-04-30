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
nb_cases = 50
cpt = 0

#############################################
#definition des variables globales
#############################################
#definition des fonctions


def grille(cases):
    """génération de la grille"""
    CG=coulour_gille(cases)
    for i in range(nb_cases):
        for j in range(nb_cases):
            pos1x = i * (WIDTH/nb_cases)            
            pos1y = j * (HEIGHT/nb_cases)
            pos2x = (i + 1)*(WIDTH/nb_cases)
            pos2y = (j + 1)*(HEIGHT/nb_cases)
            colors=rd.choice(CG)
            CG.remove(colors) 
            case = grillage.create_rectangle((pos1x, pos1y), (pos2x, pos2y), fill = colors)


def coulour_gille (p) :
    """ crée une list de 2500 elements remplit de blue et brown pour générer notre terrain """
    nombre_eau=nb_cases*nb_cases*p
    nombre_terre=(nb_cases*nb_cases)-nombre_eau
    Lbleu=["blue"]*int(nombre_eau)
    Lbrown=["brown"]*int(nombre_terre)
    Lcolors=Lbleu+Lbrown
    return Lcolors

def voisin(T):
    """si la valeur du voisinage est supérieure ou égale à T, alors une case reste ou est convertie en eau et vice vers ca"""
    pass

def creerCercle(event):
    """Dessine un rond jaune"""
    global cpt
    global cercle
    rayon = 5
    cpt +=1
    if cpt ==1:
        x = (event.x//(WIDTH/nb_cases))*(WIDTH/nb_cases) + (WIDTH/nb_cases)/2
        y = (event.y//(HEIGHT/nb_cases))*(HEIGHT/nb_cases) + (HEIGHT/nb_cases)/2
        cercle = grillage.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="yellow")
    else:
        pass
   
"""faire les déplacement du cercle"""   
def droite(event):
    grillage.move(cercle, WIDTH/nb_cases, 0)
def gauche(event):
    grillage.move(cercle, -WIDTH/nb_cases, 0)
def haut(event):
    grillage.move(cercle, 0, -HEIGHT/nb_cases)
def bas(event):
    grillage.move(cercle, 0, HEIGHT/nb_cases)


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
    global nb_cases
    nb_cases = int(input("Choisir le nombre de cases de la grille"))
    grille(p)

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
Taille = tk.Button(racine, text="Taille de la grille", bd=10, bg="grey", fg="black", activeforeground="white", activebackground="red", command=choix_taille, padx=10, pady=10, relief="groove")
Taille.grid(row=0, column=1)
grillage = tk.Canvas(racine, bg = "white", width = WIDTH, height = HEIGHT)
grillage.grid(row=0, column=0)
grillage.bind("<1>", creerCercle)
grillage.bind("<Up>", haut)
grillage.bind("<Down>", bas)
grillage.bind("<Left>", gauche)
grillage.bind("<Right>", droite)
grillage.focus_set()
grille(p)
b=grillage.find_all()
racine.mainloop()
#############################################
