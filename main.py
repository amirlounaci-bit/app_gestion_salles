from models.salle import Salle
from services.services_salle import ServiceSalle

service=ServiceSalle()

 # afficher liste des salles
# print("\nliste des salles :")
# salles=service.recuperer_salles()
# if salles:
#     for s in salles:
#         s.affiche_infos()
# else:
#     print(f"aucune salle trouvee:")
#
# ajout d'une salle
# print("\najouter une salle :")
# s5=Salle("s5","tp","logiciel","12")
# result,message=service.ajouter_salle(s5)
# print(message)


#  modifier une salle
# print("\n modifier une salle :")
# s5=Salle("s3","tpmodifier","logiciel app",16)
# result,message=service.modifer_salle(s5)
# print(message)

#  suprimer une salle
# print("\n suprimmer une salle :")
# message=service.supprimer_salle("s5")
# print(message)

# recherche une salle
# print("\n rechrcher une salle :")
# s=service.rechercher_salle("A1")
# if s:
#     s.affiche_infos()
# else:
#     print("salle intouvable")
#
