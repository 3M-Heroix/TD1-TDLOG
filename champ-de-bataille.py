class joueur:
    vaisseaux = vessel
    munitions = weapon.ammunitions
    if vaisseaux ==0 or munition <=22:
        return " Le joueur a perdu la bataille "
    else :
        return " Le joueur a gagné la bataille "

        def Espace(self, x, y, z) :
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
            elif z not in range(0,101):
                return "X out of range"

            L.

        def ajoutervais(vaisseaux,x1,y1,z1 ):
            assert Espace.x = x1 and Espace.y=y1 and Espace.z= z1, "Espace occupé"
            assert joueur.munitions <= 22, "plus de munitions mon mignon "

            def recevoir(self,x,y,z):
            l = [x,y,z]
            for i,elt in (self.vaisseaux):
                if elt == l:
                    self.etat = 1
                    self.L_etats[i] = 1
                    return True
      
                return False
