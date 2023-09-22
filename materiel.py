from tkinter import *
from PIL import Image
import datetime
import tkinter as tk
from PIL import Image, ImageTk
import time
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




class index:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("1366x2000")
        self.root.config(bg="#eff5f6")



        scrollbar = Scrollbar(self.root)
        scrollbar.pack( side = RIGHT, fill = Y )




         

        
                

        #ADDING A SCROLLBAR

        #Premiere Barre
        self.entente = Frame(self.root, bg="#F8F8FF")
        self.entente.place(x=65, y = 3, width=1070, height=30)
        
        self.deconnecte = Button(self.root, text="deconnecter", font=("time new roman", 10), bd = 0, fg = "#000000", bg = "#F8F8FF", cursor="hand2", relief = "flat" )
        self.deconnecte.place(x=880, y = 3)
        
        self.aide = Button(self.root, text="Aide", font=("time new roman", 10), bd = 0, fg = "#000000", cursor="hand2", bg = "#F8F8FF", relief = "flat" )
        self.aide.place(x=985, y = 3)
        
        self.demo = Button(self.root, text="Demo", font=("time new roman", 10, "bold"), bd = 0, fg = "#000000", cursor="hand2" ,bg = "#F8F8FF", relief = "flat")
        self.demo.place(x=700, y = 3)
        
        self.info = Button(self.root, text="info@sciambtp.com", font=("time new roman", 10, "bold"), bd = 0, fg = "#000000", cursor="hand2", bg = "#F8F8FF", relief = "flat" )
        self.info.place(x=500, y = 3)
        
        
        
        
        
        
        #deuxieme barre
        
        self.entete = Frame(self.root, bg="darkorange")
        self.entete.place(x=60, y = 30, width=1070, height=60)
        
        self.menu = Label(self.entete, text="Bienvenue SCIAM_GESCOM", font=("time new roman", 25), fg="black", bg="darkorange", bd=10).place(x=350, y= 3)
        


       
                
        

        
        #barre a gauche
        
        
        self.FrameMenu=Frame(self.root, bg="CornflowerBlue").place(x=0, y=0, width=200, height=750)
  
        self.logoImage =Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\hyy.png")
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo=Label(self.FrameMenu, image=photo, bg="#191970")
        self.logo.image=photo
        self.logo.place(x=25, y=30)

        self.admin = Label(self.FrameMenu, text="Admin", font=("time new roman", 10), bg="white").place(x=30, y=0)

        

        #barre de rechere 
        recherche_text =Entry(self.FrameMenu, font=("time new roman", 15), bg="white").place(x=25, y= 150, width= 150)
        
        #Menu deroulant 


      

        
                # DÃ©finitions des fonctions




        # Creation de l'onglet Fichier
        menuEnregistrement = Menubutton(self.FrameMenu, text='Enregistrement', width='20', borderwidth=3, bg='gray', activebackground='darkorange',relief = "flat",justify="left" )
        menuEnregistrement.place(x=20, y=200)

               # Creationn d'un menu defilant
        menuDeroulant1 = Menu(menuEnregistrement, tearoff=0)
        menuDeroulant1.add_command(label='Nouveau client' )
        menuDeroulant1.add_command(label="Personnel")
        menuDeroulant1.add_command(label="Programme")
        menuDeroulant1.add_command(label="Chantier")
        menuDeroulant1.add_command(label="maison")
        menuDeroulant1.add_command(label="depot de materiel")
        menuDeroulant1.add_command(label="materiel")


                # Attribution du menu deroulant au menu Affichage
        menuEnregistrement.configure(menu=menuDeroulant1)





        # Creation de l'onglet Edition
        menuBons = Menubutton(self.FrameMenu, text='Bons', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = "flat",justify="left")
        menuBons.place(x=20, y=250)



                 # Creationn d'un menu defilant
        menuDeroulant2 = Menu(menuBons, tearoff = 0)
        menuDeroulant2.add_command(label='Bon d achat' )
        menuDeroulant2.add_command(label="Bon de  livraison")
        menuDeroulant2.add_command(label="recu de sortie")
        menuDeroulant2.add_command(label="bulletins de salaire")
        menuDeroulant2.add_command(label="Autres")

                # Attribution du menu deroulant au menu Affichage
        menuBons.configure(menu=menuDeroulant2)




        # Creation de l'onglet Format
        menuEtats = Menubutton(self.FrameMenu, text='Etats', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = "flat",justify="left")
        menuEtats.place(x=20, y=300)


                 # Creationn d'un menu defilant
        menuDeroulant3 = Menu(menuEtats , tearoff = 0)
        menuDeroulant3.add_command(label='Etat programme' )
        menuDeroulant3.add_command(label="chantier")
        menuDeroulant3.add_command(label="maison")
        menuDeroulant3.add_command(label="terrain")
        menuDeroulant3.add_command(label="en cours de construction")
        menuDeroulant3.add_command(label="Autres")

                # Attribution du menu deroulant au menu Affichage
        menuEtats.configure(menu=menuDeroulant3)






        # Creation de l'onglet Affichage
        menumateriaux = Menubutton(self.FrameMenu, text='vente', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = "flat",justify="left")
        menumateriaux.place(x=20, y=350)

        # Creationn d'un menu defilant
        menuDeroulant8 = Menu(menumateriaux, tearoff = 0)
        menuDeroulant8.add_command(label='terrain' )
        menuDeroulant8.add_command(label="Maison")
        


        # Attribution du menu deroulant au menu Affichage
        menumateriaux.configure(menu=menuDeroulant8)




                # Creation de l'onglet Format
        menuMateriels = Menubutton(self.FrameMenu, text='Materiels', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = "flat",justify="left")
        menuMateriels.place(x=20, y=400)


                 # Creationn d'un menu defilant
        menuDeroulant4 = Menu(menuMateriels , tearoff = 0)
        menuDeroulant4.add_command(label='Marçonnerie' )
        menuDeroulant4.add_command(label="Electricité")
        menuDeroulant4.add_command(label="Plomberie")
        menuDeroulant4.add_command(label="Menusierie")
        menuDeroulant4.add_command(label="Carollage")

                # Attribution du menu deroulant au menu Affichage
        menuMateriels.configure(menu=menuDeroulant4)




                # Creation de l'onglet Format
        menuTresorerie = Menubutton(self.FrameMenu, text='Tresorerie', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = "flat",justify="left")
        menuTresorerie.place(x=20, y=450)


                 # Creationn d'un menu defilant
        menuDeroulant5 = Menu(menuTresorerie, tearoff = 0)
        menuDeroulant5.add_command(label='Depense par programme' )
        menuDeroulant5.add_command(label="Depense par chantier")
        menuDeroulant5.add_command(label="Depense par maison ")
        menuDeroulant5.add_command(label="Autres depenses")
        menuDeroulant5.add_command(label="Depense/jours/semaines/mois/année")

                # Attribution du menu deroulant au menu Affichage
        menuTresorerie.configure(menu=menuDeroulant5)





                # Creation de l'onglet Format
        menuMissions = Menubutton(self.FrameMenu, text='Missions', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = "flat",justify="left")
        menuMissions.place(x=20, y=500)


                 # Creationn d'un menu defilant
        menuDeroulant6 = Menu(menuMissions, tearoff = 0)
        menuDeroulant6.add_command(label='Petit format' )
        menuDeroulant6.add_command(label="Normal")
        menuDeroulant6.add_command(label="Grand format")
        menuDeroulant6.add_command(label="Fond clair")
        menuDeroulant6.add_command(label="Fond sombre")

                # Attribution du menu deroulant au menu Affichage
        menuMissions.configure(menu=menuDeroulant6)





                # Creation de l'onglet Format
        menuUtilisateurs = Menubutton(self.FrameMenu, text='Utilisateurs', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = "flat",justify="left")
        menuUtilisateurs.place(x=20, y=600)


                 # Creationn d'un menu defilant
        menuDeroulant7 = Menu(menuUtilisateurs , tearoff = 0)
        menuDeroulant7.add_command(label='Petit format' )
        menuDeroulant7.add_command(label="Normal")
        menuDeroulant7.add_command(label="Grand format")
        menuDeroulant7.add_command(label="Fond clair")
        menuDeroulant7.add_command(label="Fond sombre")

                # Attribution du menu deroulant au menu Affichage
        menuUtilisateurs.configure(menu=menuDeroulant7)





        menuAlerte = Menubutton(self.FrameMenu, text='Alertes', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = "flat",justify="left")
        menuAlerte.place(x=20, y=650)


                 # Creationn d'un menu defilant
        menuDeroulant9 = Menu(menuAlerte , tearoff = 0)
        menuDeroulant9.add_command(label='Petit format' )
        menuDeroulant9.add_command(label="Normal")
        menuDeroulant9.add_command(label="Grand format")
        menuDeroulant9.add_command(label="Fond clair")
        menuDeroulant9.add_command(label="Fond sombre")

                # Attribution du menu deroulant au menu Affichage
        menuAlerte.configure(menu=menuDeroulant9)



        menuDocumentation = Menubutton(self.FrameMenu, text='Documentation', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = "flat",justify="left")
        menuDocumentation.place(x=20, y=700)


                 # Creationn d'un menu defilant
        menuDeroulant10 = Menu(menuUtilisateurs , tearoff = 0)
        menuDeroulant10.add_command(label='Petit format' )
        menuDeroulant10.add_command(label="Normal")
        menuDeroulant10.add_command(label="Grand format")
        menuDeroulant10.add_command(label="Fond clair")
        menuDeroulant10.add_command(label="Fond sombre")

                # Attribution du menu deroulant au menu Affichage
        menuDocumentation.configure(menu=menuDeroulant10)


if __name__=="__main__":
            root=Tk()
            index(root)
            root.mainloop()