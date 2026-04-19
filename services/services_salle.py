from data.dao_salle import DataSalle


class ServiceSalle:
    def __init__(self):
        self.dao = DataSalle()

    def ajouter_sale(self, salle):
        if salle.code==""or salle.description=="" or salle.categorie==""or salle.capacite=="":
            return False ,"veuillez remplir tout les champs"

        if salle.capacite < 1:
            return False , "la capacite doit etre superieur ou egale a 1"

        self.dao_salle.insert_salle(salle)

        return True,"salle ajoutee avec succes"

    def modifer_sale(self, salle):
        if salle.code=="" or salle.description==""or salle.categorie=="" or salle.capacite=="":
            return False ,"veuillez remplir tout les champs"
        if salle.capacite < 1:
            return False , "la capacite doit etre superieur ou egale a 1"
        self.dao_salle.update_salle(salle)
        return True,("salle modifie avec succes")