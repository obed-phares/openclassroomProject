from tkinter import *
from PIL import Image
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from tkinter import messagebox, ttk
import sqlite3




class index:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("600x450")
        self.root.config(bg="white")


        #base de donnée


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS programme(prid text PRIMARY KEY , ville text, quartier text, nomproprietaire text, nomprogramme text, titre text, superficie text, prix text)")
        con.commit()



        #les variables
        self.var_prid=StringVar()
        self.var_ville=StringVar()
        self.var_quartier=StringVar()
        self.var_nomproprietaire=StringVar()
        self.var_nomprogramme=StringVar()
        self.var_titre=StringVar()
        self.var_superficie=StringVar()
        self.var_prix=StringVar()




        self.admin = Label(self.root, text="ENREGISTREMENT DE PROGRAMME", font=("Green", 17, "bold"), fg="DarkRed", bg="white", bd=5).pack(side=TOP, fill=X)


        txt_ville = Label(self.root, text="Ville", font=("Arial", 10, ), fg="black", bg="white").place(x=50, y= 99)
        lbl_ville = Entry(self.root, textvariable=self.var_ville, font=("Arial",10), bg="lightyellow").place(x=50, y=120, width = 200) 



        txt_quartier = Label(self.root, text="Quartier", font=("Arial", 10, ), fg="black", bg="white").place(x=260, y= 99)
        lbl_quartier = Entry(self.root, textvariable=self.var_quartier, font=("Arial",10), bg="lightyellow").place(x=260 , y=120, width = 190)


        txt_proprietaire = Label(self.root,text="Nom propriétaire terrien", font=("Arial", 10, ), fg="black", bg="white").place(x=50, y= 53)
        lbl_proprietaire = Entry(self.root,  textvariable=self.var_prid,font=("Arial",10), bg="lightyellow").place(x=50, y=75, width = 400)

        txt_programme = Label(self.root,text="Nom programme", font=("Arial", 10, ), fg="black", bg="white").place(x=50, y= 146)
        lbl_programme = Entry(self.root,  textvariable=self.var_nomprogramme, font=("Arial",10), bg="lightyellow").place(x=50, y=167, width = 400)


       
        lbl_titre = Label(self.root, text="Selectionnez un titre de proprieté", font=("Arial", 10), fg="black", bg="white").place(x=50, y= 190)
        lbl_titre= ttk.Combobox(self.root, textvariable=self.var_titre, values=("ACD", "TITRE FONCIER", "CPF", "ACP", "ATTESTION VILLAGEOISE"), font=("Arial", 10), state ="r", justify ="center")
        lbl_titre.set("selectionnez un titre")
        lbl_titre.place(x=50, y=210, width = 400)


        txt_superficie = Label(self.root,text="Superficie", font=("Arial", 10, ), fg="black", bg="white").place(x=50, y= 235)
        lbl_superficie = Entry(self.root, textvariable=self.var_superficie , font=("Arial",10), bg="lightyellow").place(x=50, y=255, width = 200)

        txt_cout = Label(self.root, text="Prix", font=("Arial", 10, ), fg="black", bg="white").place(x=260, y= 235)
        lbl_cout = Entry(self.root,  textvariable=self.var_prix,font=("Arial",10), bg="lightyellow").place(x=260, y=255, width = 190)


        self.v    = IntVar ()
        self.case = Checkbutton (variable = self.v ).place(x=190, y=280)
        txt_superficie = Label(self.root,text="Permis de construire", font=("Arial", 10, ), fg="black", bg="white").place(x=50, y= 280)


        self.A    = IntVar ()
        self.case = Checkbutton (variable = self.A).place(x=190, y=310)
        txt_superficie = Label(self.root,text="Approuvé", font=("Arial", 10, ), fg="black", bg="white").place(x=50, y= 310)

        #boutton rond a cocher pour  lotissement
        self.lotissement =IntVar ()
        self.case =Radiobutton (variable = self.lotissement).place(x=410, y=280)
        self.lotissement.get () 
        txt_superficie = Label(self.root,text="Lotissement", font=("Arial", 10, ), fg="black", bg="white").place(x=260, y=280)


        #boutton rond a cocher pour le programme immobilier
        self.immobilier =IntVar ()
        self.case =Radiobutton (variable = self.immobilier).place(x=410, y=310)
        self.immobilier.get () 
        txt_superficie = Label(self.root,text="Programme immobilier", font=("Arial", 10, ), fg="black", bg="white").place(x=260, y=310)

        #txt_id = Label(self.root, text="ID Programme", font=("Arial", 10, ), fg="black", bg="white").place(x=100, y= 200)
        #lbl_id = Entry(self.root, textvariable=self.var_prid, font=("Arial",10), bg="white", bd= 4).place(x=100, y=200, width = 100) 


        #bouton enregistrer


        self.enregistrer =Button(self.root, command=self.ajouter , text="Enregistrer", font=("Optima", 10, "bold"), cursor="hand2", bg="#1E90FF", fg="white").place(x=50, y=360, width=400)
        #fonction enregistrer

    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            if self.var_prid.get()=="":
                messagebox.showerror("Erreur", "veillez mettre un id")
            else:
                cur.execute("select * from programme where prid=?", (self.var_prid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "l'ID programme existe deja")
                else:
                    cur.execute("insert into programme (prid  , ville, quartier , nomproprietaire, nomprogramme, titre, superficie , prix) values(?,?,?,?,?,?,?,?)", (
                        self.var_prid.get(),
                        self.var_ville.get(),
                        self.var_quartier.get(),
                        self.var_nomproprietaire.get(),
                        self.var_nomprogramme.get(),
                        self.var_titre.get(),
                        self.var_superficie.get(),
                        self.var_prix.get()
                     


                    ))
                    con.commit()
                    messagebox.showinfo("Succès", "Ajout effectué avec succès")


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

if __name__=="__main__":
            root=Tk()
            index(root)
            root.mainloop()