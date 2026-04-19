from data.dao_salle import DataSalle


class ServiceSalle:
    def __init__(self):
        self.dao = DataSalle()

    def ajouter_sale(self, salle):
        if salle.code==""or salle.description=="" or salle.categorie==""or salle.capacite=="":
            return False ,"veuillez remplir tout les champs"

        if salle.capacite < 1:
            return False , "la capacite doit etre superieur ou egale a 1"

        self.dao.sales.insert(salle)

        return True,"salle ajoutee avec succes"