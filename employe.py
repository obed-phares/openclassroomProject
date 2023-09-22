from tkinter import *
from PIL import Image
import datetime
import tkinter as tk
from PIL import Image, ImageTk
import time
import pandas as pd
from tkinter import messagebox, ttk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
import sqlite3

class index:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("1500x780+400+20")
        self.root.config(bg="#eff5f6")
        self.root.focus_force()





        #base de donnéé

        con=sqlite3.connect(database =r"C:\Users\USER\Desktop\sciam_btp\donnee\sciambase.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS employe(Matricule  text INTEGER PRIMARY KEY, Nom text, Prenom text, Sexe text, fonction text,  Date text, Contrat text, Contact text, Adresse text, Email text, Password text, Type text)")
        con.commit()

        #il reste a declarer la varible de la barre de recherche a gauche



        #les vraiable

        self.var_recherche_type=StringVar()
        self.var_recherche_text=StringVar()
        self.var_emplo_id=StringVar()
        self.var_nom=StringVar()
        self.var_prenom=StringVar()
        self.var_sexe=StringVar()
        self.var_fonction = StringVar()
        self.var_contrat=StringVar()
        self.var_date=StringVar()
        self.var_contact=StringVar()
        self.var_adresse=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_type=StringVar()





        #Frame recherche

        reche_Frame =LabelFrame(self.root, text="Recherche employé", font=("goudy old style", 20, "bold"), bd=2, relief="ridge", bg="white")
        reche_Frame.place(x=400, y =65, width=500, height=75)

        # option de recherche
        reche_option = ttk.Combobox(reche_Frame, textvariable = self.var_recherche_type, values=("nom", "prenom", "matricule"), font=("time new roman", 15), state ="r", justify ="center")
        reche_option.current(0)
        reche_option.place(x=0, y=0, width=115, height=35)


        reche_txt = Entry(reche_Frame, textvariable=self.var_recherche_text,font=("time new roman",15), bg="lightyellow").place(x=135, y=0, width = 200, height=35)

        recherche =Button(reche_Frame, text="Recherche", font=("time new roman", 15), cursor="hand2", bg="blue", fg="white").place(x=350, y=0, height=35)   

        
        #titre

        titre =Label(self.root, text="Formulaire  employé", font=("time new roman", 20), cursor="hand2", bg ="CornflowerBlue", justify="center").place(x=0, y=0, width=1300)


      
        # A revoir 



        #contenu
        #ligne1
        lbl_empid = Label(self.root,  text="Matricule", font=("goudy old style", 15), fg="black", bg="#eff5f6").place(x=250, y= 166, width=150)

        lbl_empid = Entry(self.root, textvariable= self.var_emplo_id ,font=("time new roman",15, "bold"), bg="lightyellow").place(x=260, y=190, width = 150)



        lbl_nom = Label(self.root, text="Nom", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=450, y= 166, width=150)
        lbl_nom = Entry(self.root, textvariable=self.var_nom, font=("time new roman",15), bg="lightyellow").place(x=460, y=190, width = 150)


        lbl_prenom = Label(self.root,text="prenom", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=650, y= 166, width=150)
        lbl_prenom = Entry(self.root,  textvariable=self.var_prenom, font=("time new roman",15), bg="lightyellow").place(x=660, y=190, width = 150)


         
        lbl_sexe = Label(self.root, text="Sexe", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=850, y= 166, width=150)
        lbl_sexe = Label(self.root, text="Contrat", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=450, y= 225, width=150)
        lbl_sexe= ttk.Combobox(self.root, textvariable=self.var_sexe,values=("homme", "femme"), font=("time new roman", 15), state ="r", justify ="center")
        lbl_sexe.current(0)
        lbl_sexe.place(x=860, y=190, width = 150)




        lbl_date = Label(self.root, text="Date", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=650, y= 225, width=150)
        lbl_date = Entry(self.root, textvariable= self.var_date,font=("time new roman",15), bg="lightyellow").place(x=660, y=250, width = 150)

        #ligne2

        lbl_fonction = Label(self.root, text="Fonction", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=250, y= 225, width=150)
        lbl_fonction = Entry(self.root, textvariable=self.var_fonction,font=("time new roman",15), bg="lightyellow").place(x=260, y=250, width = 150)


        lbl_contrat = Label(self.root, text="Contrat", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=450, y= 225, width=150)
        lbl_contrat= ttk.Combobox(self.root, textvariable=self.var_contrat ,values=("Journalier", "CDD", "CDI"), font=("time new roman", 15), state ="r", justify ="center")
        lbl_contrat.current(0)
        lbl_contrat.place(x=460, y=250, width=150)

         #ligne3
        lbl=contact = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=850, y= 225, width=150)
        lbl_contact = Entry(self.root, textvariable=self.var_contact,font=("time new roman",15), bg="lightyellow").place(x=860, y=250, width = 150)


        lbl_password = Label(self.root, text="Password", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=850, y= 285, width=150)
        lbl_password = Entry(self.root, textvariable=self.var_password ,font=("time new roman",15), bg="lightyellow").place(x=860, y=310, width = 150)


        lbl_E_mail = Label(self.root, text="E-mail", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=650, y= 285, width=150)
        lbl_E_mail = Entry(self.root, textvariable=self.var_email ,font=("time new roman",15), bg="lightyellow").place(x=660, y=310, width = 150)

        #derniere ligne
        lbl_adrese = Label(self.root, text="Adresse", font=("goudy old style", 15), fg="black", bg="#eff5f6").place(x=250, y= 285, width=150)

        lbl_adrese = Entry(self.root, font=("time new roman",15), bg="lightyellow").place(x=260, y=310, width = 300, height= 95)



        lbl_type = Label(self.root, text="Type", font=("goudy old style", 15, "bold"), fg="black", bg="#eff5f6").place(x=850, y= 335, width=150)
        lbl_type= ttk.Combobox(self.root, textvariable=self.var_type ,values=("Admin", "secretariat", "comptable", "technicien", "ouvrier"), font=("time new roman", 15), state ="r", justify ="center")
        lbl_type.current(0)
        lbl_type.place(x=860, y=360, width=150)


        #Ajouter un boutton

        ajout_btn =Button(self.root, command = self.ajouter,text="Ajouter", font=("time new roman", 17, "bold"), cursor="hand2", bg="green").place(x=350, y=430)

        modifier_btn =Button(self.root, text="modifier", font=("time new roman", 17, "bold"), cursor="hand2", bg="yellow").place(x=500, y=430)


        supprimer_btn =Button(self.root, text="supprimer", font=("time new roman", 17, "bold"), cursor="hand2", bg="red").place(x=650, y=430)

        reni_btn =Button(self.root, text="Renitialiser", font=("time new roman", 17, "bold"), cursor="hand2", bg="lightgray").place(x=800, y=430)



        #liste employé
        #self.listeFrame= LabelFrame(self.root, bd=5, relief="ridge").place(x=0, y=475, height=150, relwidth=1, width=150)
        #scroll_y=Scrollbar(self.listeFrame, orient=VERTICAL)
        #scroll_y.pack(side="right", fill=Y)
        #scroll_x=Scrollbar(self.listeFrame, orient=VERTICAL)
        #scroll_x.pack(side=BOTTOM, fill=X)


        #self.employeliste =ttk.Treeview(self.listeFrame, columns=("Matricule", "Nom", "Prenom", "Sexe", "Fonction, Contrat", "Date", "Durée", "Adresse", "E-mail", "Contact", "Type" ), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        #scroll_x.config(command=self.employeliste.xview)
        #scroll_y.config(command=self.employeliste.yview)


        #self.employeliste.heading("Matricule", text="Matricule")
        #self.employeliste.pack(fil="both",      expand=100)






                

        #ADDING A SCROLLBAR

        #Premiere Barre
       # self.entente = Frame(self.root, bg="#F8F8FF")
        #self.entente.place(x=65, y = 3, width=1070, height=30)
        
        #self.deconnecte = Button(self.root, text="deconnecter", font=("time new roman", 10), bd = 0, fg = "#000000", bg = "#F8F8FF", cursor="hand2", relief = "flat" )
        #self.deconnecte.place(x=880, y = 3)
        
        #self.aide = Button(self.root, text="Aide", font=("time new roman", 10), bd = 0, fg = "#000000", cursor="hand2", bg = "#F8F8FF", relief = "flat" )
        #self.aide.place(x=985, y = 3)
        
        #self.demo = Button(self.root, text="Demo", font=("time new roman", 10, "bold"), bd = 0, fg = "#000000", cursor="hand2" ,bg = "#F8F8FF", relief = "flat")
        #self.demo.place(x=700, y = 3)
        
       # self.info = Button(self.root, text="info@sciambtp.com", font=("time new roman", 10, "bold"), bd = 0, fg = "#000000", cursor="hand2", bg = "#F8F8FF", relief = "flat" )
        #self.info.place(x=500, y = 3)
        
        
        
        
        
        
        #deuxieme barre
        
        #self.entete = Frame(self.root, bg="darkorange")
       # self.entete.place(x=60, y = 0, width=1070, height=60)
        
        #self.menu = Label(self.entete, text="Bienvenue SCIAM_GESCOM", font=("time new roman", 25), fg="black", bg="darkorange", bd=10).place(x=350, y= 0)
        


       
                
        

        
        #barre a gauche
        
        
        self.FrameMenu=Frame(self.root, bg="CornflowerBlue").place(x=0, y=0, width=200, height=750)
  
        self.logoImage =Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\hyy.png")
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo=Label(self.FrameMenu, image=photo, bg="#191970")
        self.logo.image=photo
        self.logo.place(x=25, y=30)



        

        #barre de rechere 
        recherche_text =Entry(self.FrameMenu, font=("time new roman", 15), bg="white").place(x=25, y= 150, width= 150)
        
        #Menu deroulant 


      

        
                # DÃ©finitions des fonctions





        #fonction

    def ajouter(self):
        con=sqlite3.connect(database =r"C:\Users\USER\Desktop\sciam_btp\donnee\sciambase.db")
        cur=con.cursor()
        try:
                if self.var_emplo_id.get()=="" or self.var_password.get()=="" or self.var_type.get()=="":

                        messagebox.showerror("Erreur", "Veillez mettre une matricule, Password et type")
                else:
                        cur.execute("select * from employe where Matricule=?", (self.var_emplo_id.get(),))
                        row=cur.fetchone()
                        if row!= None:
                                messagebox.showerror("Erreur", "le matricule employé existe deja")
                        else:
                                cur.execute("insert into employe (Matricule, Nom , Prenom, Sexe, fonction,  Date, Contrat, Contact, Adresse, Email, Password, Type) values(?,?,?,?,?,?,?,?,?,?,?,?)",(

                                        self.var_emplo_id.get(),
                                        self.var_nom.get(),
                                        self.var_password.get(),
                                        self.var_sexe.get(),
                                        self.var_fonction.get(),
                                        self.var_date.get(),
                                        self.var_contrat.get(),
                                        self.var_contact.get(),
                                        self.var_adresse.get(),
                                        self.var_email.get(),
                                        self.var_password.get(),
                                        self.var_type.get()





                                ))
                                con.commit()
                                #self.afficher()
                                messagebox.showinfo("Succès", "Ajout effectué avec succès")


        except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


        #fonction afficher
        #def afficher(self):
         #       con=sqlite3.connect(database =r"C:\Users\USER\Desktop\sciam_btp\donnee\sciambase.db")
          #      cur=con.cursor()
        #try:
         #       cur.execute("select * employe")
          #      rows=cur.fetchall()
          #      self.employeliste.delete(*self.employeliste.get_children())
          #      for row in rows:
           #             self.employeliste.insert("", END, values=row)

#        except Exception as ex:
 #               messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")




        # Creation de l'onglet Fichier
        menuEnregistrement = Menubutton(self.FrameMenu, text='Initialisation', width='20', borderwidth=3, bg='gray', activebackground='darkorange',relief = "flat",justify="left" )
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
        menuEnregistrement.configure(menu=menuDeroulant1)


        menuBons = Menubutton(self.FrameMenu, text='Initialisation', width='20', borderwidth=3, bg='gray', activebackground='darkorange',relief = "flat",justify="left" )
        menuBons.place(x=20, y=250)
        menuDeroulant2 = Menu(menuBons, tearoff = 0)
        menuDeroulant2.add_command(label='Bon d achat' )
        menuDeroulant2.add_command(label="Bon de  livraison")
        menuDeroulant2.add_command(label="recu de sortie")
        menuDeroulant2.add_command(label="bulletins de salaire")
        menuDeroulant2.add_command(label="Autres")

                # Attribution du menu deroulant au menu Affichage
        menuBons.configure(menu=menuDeroulant2)




        # Creation de l'onglet Format
        menuEtats = Menubutton(self.FrameMenu, text='Statut', width='20', borderwidth=2, bg='gray', activebackground='darkorange',relief = "flat",justify="left")
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