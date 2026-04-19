from data.dao_salle import DataSalle
from models.salle import salle

dao = DataSalle()
# test de connexion
conn=dao.get_connection()
if conn:
    print(f"connexion reussi")
    conn.close()

# test d'ajout salle
s1=salle("A1","salle informatique","labo","35")
# dao.insert_salle(s1)
# print(f"salle ajoutee")



# test modifier une salle
# s1.description="salle reseau"
# s1.categorie="recherche"
# s1.capacite="45"
# dao.update_salle(s1)
# print(f"salle modifiee")

# test recherche d'une salle
salle=dao.get_salle("A1")
if salle:
    print(f"salle trouvee")

else:
    print(f"salle non trouvee")

# test de recupperation de toute les salles
print("\nliste des salles :")
liste=dao.get_salles()
for s in liste:
    print(s)

# teste de supression d'une salle
dao.delete_salle("A2")
print(f"salle suprimer")