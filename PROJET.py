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
from tkinter import simpledialog
from tkinter import filedialog
import random as rd
import json
#############################################
#definition des constantes(M)
p = 0.5
n = 4
T = 4
k = 1
HEIGHT = 800
WIDTH = 800
nb_cases = 50
cpt = 0
cercle = None
GrilleTotal = [[0 for x in range(nb_cases)] for y in range(nb_cases)]
CurrentPosition = None
deplacements=[]

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
            GrilleTotal[i][j]=colors
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

def generation_suivante():
    """si la valeur du voisinage est supérieur ou égale à T, alors une case reste ou est convertie en eau vice et versa"""
    global GrilleTotal, k, T, p 
    for x in range(len(GrilleTotal)):
        for y in range(len(GrilleTotal)):
            if valeur_voisinage(GrilleTotal) >= T:
                GrilleTotal[x][y]="blue"
            else:
                GrilleTotal[x][y]="brown"
    affiche_grille()


def voisin(T):
    """si la valeur du voisinage est supérieure ou égale à T, alors une case reste ou est convertie en eau et vice vers ca"""
    pass

def creerCercle(event):
    """Dessine un rond jaune"""
    global cpt, cercle, CurrentPosition
    rayon = 5
    if cpt ==0:
        x = (event.x//(WIDTH/nb_cases))*(WIDTH/nb_cases) + (WIDTH/nb_cases)/2
        y = (event.y//(HEIGHT/nb_cases))*(HEIGHT/nb_cases) + (HEIGHT/nb_cases)/2
        CurrentPosition = [int(event.x//(WIDTH/nb_cases)),int(event.y//(HEIGHT/nb_cases))]
        cercle = grillage.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="yellow")
                               
def droite(event): 
    """faire déplacer le cercle à droite sans aller dans la casse eau"""  
    if CurrentPosition[0]+1<nb_cases and GrilleTotal[CurrentPosition[0]+1][CurrentPosition[1]] == 'brown' :
        grillage.move(cercle, WIDTH/nb_cases, 0)
        CurrentPosition[0]+=1

def gauche(event):
    """faire déplacer le cercle à gauche sans aller dans la casse eau"""
    if CurrentPosition[0]-1>=0 and GrilleTotal[CurrentPosition[0]-1][CurrentPosition[1]] == 'brown' :
        grillage.move(cercle, -WIDTH/nb_cases, 0)
        CurrentPosition[0]-=1

def haut(event):
    """faire déplacer le cercle en haut sans aller dans la casse eau"""
    if CurrentPosition[1]-1>=0 and GrilleTotal[CurrentPosition[0]][CurrentPosition[1]-1] == 'brown' :
        grillage.move(cercle, 0, -HEIGHT/nb_cases)
        CurrentPosition[1]-=1

def bas(event):
    """faire déplacer le cercle en bas sans aller dans la casse eau"""
    if CurrentPosition[1]+1<nb_cases and GrilleTotal[CurrentPosition[0]][CurrentPosition[1]+1] == 'brown' :
        grillage.move(cercle, 0, HEIGHT/nb_cases)
        CurrentPosition[1]+=1  

def retirer_cercle():
    global cercle, cpt 
    cpt = 0
    grillage.delete(cercle)
    

def valeur_voisinage(k):
    """définit la valeur du voisinage"""
    eau = 0
    for i in range(-k, k+1):
        for j in range(-k, k+1):
            if ((i != 0 or j != 0) and x+i >=0 and x+i< len(grille) and y+j >= 0 and y+j < len(grille) and grille[x+i][y+j]=="blue"):
                eau = eau + 1 
    return eau

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
    global deplacements
    if cpt == 1 and len(deplacements)>0:
        f= deplacements.pop()
        f(None)

def sauvegarde():
    """sauvegarde le terrain généré"""
    f = tk.filedialop.asksaveasfile()
    json.dump([CurrentPosition, GrilleTota], f)
    f.close()

def recharge():
    """recharge un nouveau terrain"""
    global CurrentPosition, GrilleTotal, nb_cases
    f = tk.filedialog.askopenfile()
    r = json.load(f)
    CurrentPosition = r[0]
    GrilleTotal = r[1]
    nb_cases = len(GrilleTotal)
    f.close()
    affiche_grille()

def changerP():
    global p 
    p = simpledialog.askfloat("Input", "Paramètre p:")
    grille(p)

def changerN():
    global n 
    n = simpledialog.askinteger("Input", "Paramètre n:")
    grille(p)

def changerT():
    global T
    T = simpledialog.askinteger("Input", "Paramètre T:")
    grille(p)

def changerK():
    global k
    k = simpledialog.askinteger("Input", "Paramètre k:")
    grille(p)


#############################################
#programme principal
racine = tk.Tk()

grillage = tk.Canvas(racine, bg = "white", width = WIDTH, height = HEIGHT)
grillage.grid(row=0, column=0, rowspan=30)
grillage.bind("<1>", creerCercle)
grillage.bind("<Up>", haut)
grillage.bind("<Down>", bas)
grillage.bind("<Left>", gauche)
grillage.bind("<Right>", droite)
grillage.focus_set()
grille(p)
b=grillage.find_all()

bouton_gen_suivante = tk.Button(racine, text="Génération suivante", command=generation_suivante)
bouton_gen_suivante.grid(row=0, column=1)

Taille = tk.Button(racine, text="Taille de la grille", command=choix_taille)
Taille.grid(row=1, column=1)

Button_retirer= tk.Button(racine, text="Retirer personnage", command=retirer_cercle)
Button_retirer.grid(row=2, column=1)

bouton_p = tk.Button(racine, text="Changer p", command=changerP)
bouton_p.grid(row=0, column=2)

bouton_n = tk.Button(racine, text="Changer n", command= changerN)
bouton_n.grid(row=1, column=2)

bouton_t = tk.Button(racine, text="Changer t", command = changerT)
bouton_t.grid(row=2, column=2)

bouton_k = tk.Button(racine, text="Changer k", command= changerK)
bouton_k.grid(row=3, column=2)

bouton_sauvegarder = tk.Button(racine, text="Sauvegarder", command = sauvegarde)
bouton_sauvegarder.grid(row=0, column=3)

bouton_charger = tk.Button(racine, text="Charger", command=recharge)
bouton_charger.grid(row=1, column=3)

bouton_retour = tk.Button(racine, text="Retour", command=annuler_deplacement)
bouton_retour.grid(row=2, column=3)

racine.mainloop()
#############################################
