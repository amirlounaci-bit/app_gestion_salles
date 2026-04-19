from data.dao_salle import DataSalle
from models.salle import Salle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if salle.code==""or salle.description=="" or salle.categorie==""or salle.capacite=="":
            return False ,"veuillez remplir tout les champs"
        try :
            capacite=int(salle.capacite)
        except :
            return False ,"capacite invalide"

        if capacite < 1:
            return False , "la capacite doit etre superieur ou egale a 1"
        salle.capacite=capacite

        self.dao_salle.insert_salle(salle)

        return True,"salle ajoutee avec succes"

    def modifer_salle(self, salle):
        if salle.code=="" or salle.description==""or salle.categorie=="" or salle.capacite=="":
            return False ,"veuillez remplir tout les champs"
        try :
            capacite=int(salle.capacite)
        except :
            return False ,"capacite invalide"
        if salle.capacite < 1:
            return False , "la capacite doit etre superieur ou egale a 1"
        salle.capacite = capacite
        self.dao_salle.update_salle(salle)
        return True,("salle modifie avec succes")

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)
        return True, "salle suprimee avec succes"

    def rechercher_salle(self, code):
        resultat=self.dao_salle.get_salle(code)
        if resultat:
            return Salle (resultat[0], resultat[1], resultat[2], resultat[3])
        else:
            return None

    def recuperer_salles(self):
        rows=self.dao_salle.get_salles()
        salles=[]
        for row in rows:
            salles.append(Salle(row[0], row[1], row[2], row[3]))

        return salles