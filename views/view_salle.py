import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle
from tkinter import ttk

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.service=ServiceSalle()
        self.title  ("Gestion Salles")
        self.geometry ("700x500")
        self.frame_information()
        self.frame_actions()

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

    def modifier_salle(self):
        code=self.EntryCode.get()
        description=self.EntryDescription.get()
        categorie=self.EntryCategorie.get()
        capacite=self.EntryCapacite.get()
        salle=Salle(code,description,categorie,int(capacite))

        message=self.service_salle.modifier_salle(salle)
        print(message)

        code=self.EntryCode.get()

        ctk.CTkButton(frame,texte="modifier", command=self.modifier_salle()).grid(row=0,column=1)

    def supprimer_salle(self):
        code=self.EntryCode.get()

        message=self.service_salle.supprimer_salle(code)
        print(message)

        ctk.CTkButton(frame,texte="supprimer", command=self.modifier_salle()).grid(row=0,column=2)

    def rechercher_salle(self):
        code=self.EntryCode.get()

        salle=self.service_salle.rechercher_salle(code)

        if salle:
            self.entry_description.delete(0,"end")
            self.entry_categorie.delete(0,"end")
            self.entry_capacite.delete(0,"end")

            self.entry_description.insert(0,salle.description)
            self.entry_categorie.insert(0,salle.categorie)
            self.entry_capacite.insert(0,salle.capacite)

        ctk.CTkButton(frame, texte="rechercher", command=self.modifier_salle()).grid(row=0, column=3)

    def frame_lister(self):
        cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)
        self.treeList = ttk.Treeview(self.cadreList, columns=("code", "description", "categorie", "capacite"),show="headings")

        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")

        self.treeList.column("code", width=50)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=100)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())

        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))



















