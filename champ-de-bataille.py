class joueur:
    def __init__(self, Vaisseaux, Munitions):
        self.Vaisseaux = Vaisseaux
        self.Munitions = Munitions

class Espace :
    def Position(self, x, y, z):
        if x in range(0,101):
            self.x = int(x) 
        elif y not in range(0,101):
            return "X out of range"

        if y in range(0,101):
            self.y = int(y) 
        elif y not in range(0,101):
            return "Y out of range"

        if z in [-1,0,1]:
            self.z = int(z) 
        elif z not in [-1,0,1]:
            return "Z out of range"

def ajoutervais(x1,y1,z1):
        Listvess=Listvess.append(joueur.Vaisseaux)
        assert Espace.x == x1 and Espace.y==y1 and Espace.z==z1, "Espace occupé"
        assert joueur.munitions <= 22, "Plus de munitions "

def recevoir(joueur,x,y,z):
        vess=joueur.Vaisseaux
        for i in (vess):
            if i[0]==x and i[1]==y and i[2]==z :
                vess.remove(i)
                return True
        return False

def Gameover(joueur):
    if len(joueur.Vaisseaux) ==0 or joueur.Munitions <=22:
        return " Le joueur a perdu la bataille "
    elif len(joueur.Vaisseaux) !=0 and joueur.Munitions >22:
        return " La bataille continue "

#------------------------------------------------------------------------------------------------------#

J1= joueur([[2,3,0]],18)
J2= joueur([[51,4,-1]],22)

recevoir(J1,2,3,0) # Le joueur J1 reçoit une attaque dans la position [2,3,0], la méthode retourne True.
Gameover(J1) # Retourne "Le joueur a perdu la bataille"  car J1 est touché.

# Le joueur J1 perd la bataille puisqu'il n'a plus de vaisseaux disponibles.
