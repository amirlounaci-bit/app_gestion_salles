import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.service=ServiceSalle()
        self.title = "Gestion Salles"
        self.geometry = "700x500"

    def frame_information(self):

        frame=ctk.CTkFrame(self)
        frame.pack(pady=10)

        ctk.CTkLabel(frame,text="code").grid(row=0,column=0)
        self.EntryCode = ctk.CTkEntry(frame)
        self.EntryCode.grid(row=0,column=1)

        ctk.CTkLabel(frame,text="description").grid(row=1,column=0)
        self.EntryDescription = ctk.CTkEntry(frame)
        self.EntryDescription.grid(row=1,column=1)

        ctk.CTkLabel(frame,text="categorie").grid(row=2,column=0)
        self.EntryCategorie = ctk.CTkEntry(frame)
        self.EntryCategorie.grid(row=2,column=1)

        ctk.CTkLabel(frame,text="capacite").grid(row=3,column=0)
        self.EntryCapacite = ctk.CTkEntry(frame)
        self.EntryCapacite.grid(row=3,column=1)



    def frame_actions(self):
        frame=ctk.CTkFrame(self)
        frame.pack(pady=10)

        ctk.CTkButton(frame,text="ajouter").grid(row=0,column=0,padx=5)
        ctk.CTkButton(frame,text="modifier").grid(row=0,column=1,padx=5)
        ctk.CTkButton(frame,text="supprimer").grid(row=0,column=2,padx=5)
        ctk.CTkButton(frame,text="rechercher").grid(row=0,column=3,padx=5)

    def ajouter_salle(self):

        code=self.EntryCode.get()
        description=self.EntryDescription.get()
        categorie=self.EntryCategorie.get()
        capacite=self.EntryCapacite.get()

        salle=Salle(code,description,categorie,capacite)
        message=self.sevice_salle.ajouter_salle(salle)
        print(message)

        ctk.CTkButton(frame,text="ajouter",command=self.ajouter_salle).grid(row=0,column=0)













