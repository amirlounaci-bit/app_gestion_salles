from data.dao_salle import DataSalle


class ServiceSalle:
    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):
        if salle.code==""or salle.description=="" or salle.categorie==""or salle.capacite=="":
            return False ,"veuillez remplir tout les champs"

        if salle.capacite < 1:
            return False , "la capacite doit etre superieur ou egale a 1"

        self.dao_salle.insert_salle(salle)

        return True,"salle ajoutee avec succes"

    def modifer_salle(self, salle):
        if salle.code=="" or salle.description==""or salle.categorie=="" or salle.capacite=="":
            return False ,"veuillez remplir tout les champs"
        if salle.capacite < 1:
            return False , "la capacite doit etre superieur ou egale a 1"
        self.dao_salle.update_salle(salle)
        return True,("salle modifie avec succes")

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)
        return True, "salle suprimee avec succes"

    def rechercher_salle(self, code):
        resultat=self.dao_salle.get_salle(code)
        if resultat:
            return salle (resultat[0], resultat[1], resultat[2], resultat[3])
        else:
            return None
