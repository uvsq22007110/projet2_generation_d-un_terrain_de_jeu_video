#############################################
# groupe BI1
# Laurie MIALIN
# Fatima AIT IGHIL 
# Cecile FETRE
# Charoline JOSEPH
# Alexis BRIAND
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
T = 5
k = 1
HEIGHT = 800
WIDTH = 800
nb_cases = 50
cpt = 0
cercle = None
CurrentPosition = None
deplacements=[]
GrilleTotal = [[0 for x in range(nb_cases)] for y in range(nb_cases)]

#############################################
#definition des fonctions

def grille(cases):
    """génération de la grille"""
    #GrilleTotal = [[0 for x in range(nb_cases)] for y in range(nb_cases)]
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
    count=1
    for x in range(len(GrilleTotal)):
        for y in range(len(GrilleTotal)):
            if valeur_voisinage(k,GrilleTotal,x,y) >= T:
                grillage.itemconfigure(count, fill="blue") 
            else:
                grillage.itemconfigure(count, fill="brown")
            count=count+1
            
def creerCercle(event):
    """Dessine un rond jaune"""
    global nb_cases, cpt, cercle, CurrentPosition
    rayon = - 0.375*nb_cases+23.75
    if cpt ==0:
        x = (event.x//(WIDTH/nb_cases))*(WIDTH/nb_cases) + (WIDTH/nb_cases)/2
        y = (event.y//(HEIGHT/nb_cases))*(HEIGHT/nb_cases) + (HEIGHT/nb_cases)/2
        CurrentPosition = [int(event.x//(WIDTH/nb_cases)), int(event.y//(HEIGHT/nb_cases))]
        if GrilleTotal[CurrentPosition[0]][CurrentPosition[1]]!="blue": 
            cercle = grillage.create_oval((x-rayon, y-rayon), (x+rayon, y+rayon), fill="yellow")
            cpt+=1
                               
def droite(event):
    """faire déplacer le cercle à droite sans aller dans la casse eau"""  
    global deplacements
    if CurrentPosition[0]+1<nb_cases and GrilleTotal[CurrentPosition[0]+1][CurrentPosition[1]] == 'brown' :
        grillage.move(cercle, WIDTH/nb_cases, 0)
        CurrentPosition[0]+=1
        if event!=None:
            deplacements.append(gauche)

def gauche(event):
    """faire déplacer le cercle à gauche sans aller dans la casse eau"""
    global deplacements
    if CurrentPosition[0]-1>=0 and GrilleTotal[CurrentPosition[0]-1][CurrentPosition[1]] == 'brown' :
        grillage.move(cercle, -WIDTH/nb_cases, 0)
        CurrentPosition[0]-=1
        if event !=None:
            deplacements.append(droite)

def haut(event):
    """faire déplacer le cercle en haut sans aller dans la casse eau"""
    global deplacements
    if CurrentPosition[1]-1>=0 and GrilleTotal[CurrentPosition[0]][CurrentPosition[1]-1] == 'brown' :
        grillage.move(cercle, 0, -HEIGHT/nb_cases)
        CurrentPosition[1]-=1
        if event != None:
            deplacements.append(bas)

def bas(event):
    """faire déplacer le cercle en bas sans aller dans la casse eau"""
    global deplacements
    if CurrentPosition[1]+1<nb_cases and GrilleTotal[CurrentPosition[0]][CurrentPosition[1]+1] == 'brown' :
        grillage.move(cercle, 0, HEIGHT/nb_cases)
        CurrentPosition[1]+=1  
        if event != None:
            deplacements.append(haut)

def retirer_cercle():
    " fonction qui permet de retirer le cercle et lorqu'on clique sur une autre case terre le cercle se replace"
    global cercle, cpt 
    cpt = 0
    grillage.delete(cercle)
       

def valeur_voisinage(k,grilletotal,x,y):
    """définit la valeur du voisinage"""
    eau = 0
   
    for i in range(-k, k+1):
        for j in range(-k, k+1):
            if ((i != 0 or j != 0) and x+i >=0 and x+i< len(GrilleTotal) and y+j >= 0 and y+j < len(GrilleTotal) and GrilleTotal[x+i][y+j]=="blue"):
                eau = eau + 1
                
    return eau

def choix_parametres():
    """l'utilisateur choisit les paramètres, k, p, n, T"""
    global k, n, p, T
    fenetre1 = tk.Tk()
    label1 = tk.Label(fenetre1, text="Paramètre p (la probabilité d'avoir une case eau)").grid()
    Param1 = tk.Entry(fenetre1)
    Param1.insert(0,p)
    Param1.grid()
    label2 = tk.Label(fenetre1, text="Paramètre n (le nombre de fois où on répète l'automate)").grid()
    Param2 = tk.Entry(fenetre1)
    Param2.insert(0,n)
    Param2.grid()
    label3 = tk.Label(fenetre1, text="Paramètre T (la valeur du voisinage)").grid()
    Param3 = tk.Entry(fenetre1)
    Param3.insert(0,T)
    Param3.grid()
    label4 = tk.Label(fenetre1, text="Paramètre k (l'ordre du voisinage de Moore)").grid()
    Param4 = tk.Entry(fenetre1)
    Param4.insert(0,k)
    Param4.grid()
    valider=tk.Button(fenetre1, text="valider", command=fenetre1.quit).grid()
    fenetre1.mainloop()
    p = int(Param1.get())
    n = int(Param2.get())
    T = int(Param3.get())
    k = int(Param4.get())
    fenetre1.destroy()
    #valeur_voisinage(k)
    #generation_suivante()
    grille(p)


def choix_taille():
    """l'utilisateur choisit la taille de la grille"""
    global nb_cases
    fenetre1 = tk.Tk()
    label1 = tk.Label(fenetre1, text="Saisir le nombre de colonnes de la grille").grid()
    cases = tk.Entry(fenetre1)
    cases.insert(0, nb_cases)
    cases.grid()
    valider=tk.Button(fenetre1, text="valider", command=fenetre1.quit).grid()
    fenetre1.mainloop()
    nb_cases = int(cases.get())
    fenetre1.destroy()
    grille(p)


def annuler_deplacement():
    """annule le déplacement du personnage"""
    global deplacements
    if cpt == 1 and len(deplacements)>0:
        f= deplacements.pop()
        f(None)

def sauvegarde():
    """sauvegarde le terrain généré"""
    f = tk.filedialog.asksaveasfile()
    json.dump([CurrentPosition, GrilleTotal], f)
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

def creerBouton(text, fonction, i, j):
    bouton = tk.Button(racine, text=text, command=fonction).grid(row=i, column=j)
    return bouton
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

bouton_gen_suivante = creerBouton("Génération suivante", generation_suivante, 0, 1)
Taille = creerBouton("Taille de la grille", choix_taille, 1, 1)
Parametres = creerBouton("Paramètres", choix_parametres, 3, 1)
Button_retirer= creerBouton("Retirer personnage", retirer_cercle, 2, 1)
bouton_sauvegarder = creerBouton("Sauvegarder", sauvegarde, 0, 3)
bouton_charger = creerBouton("Charger", recharge, 1, 3)
bouton_retour = creerBouton("Retour", annuler_deplacement, 2, 3)

racine.mainloop()
#############################################
