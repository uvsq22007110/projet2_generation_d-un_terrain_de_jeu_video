# projet2_generation_d-un_terrain_de_jeu_video
Notre programme est un générateur de terrain.

Partie personnage:
Dans ce programme le personnage est représenté par un cercle de couleur jaune. On peut placer le cercle n'importe où et seulement sur une case terre.
Pour permettre le déplacement du personnage, il suffit d'utiliser les flèches du clavier qui sont définies par: def haut(event), def bas(event), def droite(event), def gauche (event).

Partie Bouton:
Le bouton " Retirer personnage ", sert à retirer le cercle de la grille,ainsi le cercle placé sur une case terre va être retiré. Une fois retiré vous devez cliquer à un autre endroit dans la grille plus précisément sur une case terre et le cercle réapparaîtra. 
Le bouton "Retour" permet d'annuler le déplacement du personnage (cercle), il fait un retour en arrière.
Le bouton " Taille de la grille" permet de changer le nombre de cases de la grille,  une fenêtre va s'ouvrir avec affiché la valeur par défaut ou la valeur précédemment renseignée.
Le bouton "Sauvegarder" permet de sauvegarder le jeu dans notre ordinateur.
Le bouton " Charger" permet de récupérer le jeu sauvegardé dans notre ordinateur, pour continuer à jouer dessus.
Le boutton " Paramètres" permet de modifier les paramètres de la grille : p (la probabilité d'avoir une case eau), n (nombre de fois où l'automate va se répéter), T (le nombre de cases eau voisins qui vont définir le type (eau/terre) de la case centrale) et k (l'ordre du voisinage de Moore).
