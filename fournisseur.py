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
import sqlite3


class fournisseur:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("1300x1300")
        self.root.config(bg="white")

        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS fournisseur(forid text PRIMARY KEY, nom text, contact text, description text, entreprise text, NumeroCompte text, Numerolivraison text, categorie text, Quantité text, prixU text, prix text)")
        con.commit()


        #les variables
        self.var_recherche_text=StringVar()
        self.var_fourni_id=StringVar()
        self.var_nom=StringVar()
        self.var_contact=StringVar()
        self.var_txt_description=StringVar()
        #self.var_description=StringVar()
 

        ## option de recherche
        self.reche_option=Label(self.root, text="recherche par ID", font=("times new roma", 12), bg="white")
        self.reche_option.place(x=580, y=50)

        recherche_txt=Entry(self.root, textvariable=self.var_recherche_text , font=("times new roman ", 12), bg="lightyellow").place(x=700, y=50, height=20)

        recherche_btn=Button(self.root, text="recherche", command=self.recherche,font=("times new roman", 12, "bold"), cursor="hand2", bg="blue", fg="white").place(x=900, y=50, height=25)

        recherche_btn=Button(self.root, text="tous", command=self.afficher ,font=("times new roman", 12, "bold"), cursor="hand2", bg="lightgray", fg="white").place(x=990, y=50, height=25)



        #tire
        titre =Label(self.root, text="fournisseur", font=("algerian", 15),  bg="cyan", justify=CENTER).place(x=0, y=0, width=1300)

        #contenu
                #ligne 1
        lbl_fourid=Label(self.root, text="ID fournisseur", font=("times new roman", 15), bg="white").place(x=50, y=70)
        self.txt_fourid = Entry(self.root, textvariable=self.var_fourni_id , font=("times new roman ", 15), bg="lightyellow")
        self.txt_fourid.place(x=200, y=70, width=200)

        lbl_nom=Label(self.root, text="Nom", font=("times new roman", 15), bg="white").place(x=50, y=140)
        txt_nom = Entry(self.root, textvariable=self.var_nom, font=("times new roman ", 15), bg="lightyellow")
        txt_nom.place(x=200, y=140, width=200)


        lbl_contact=Label(self.root, text="Contact", font=("times new roman", 15), bg="white").place(x=50, y=210)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("times new roman ", 15), bg="lightyellow").place(x=200, y=210, width=200)


        lbl_description=Label(self.root, text="Description", font=("times new roman", 15), bg="white").place(x=50, y=280)
        txt_description = Entry(self.root, textvariable = self.var_txt_description, font=("times new roman ", 15), bg="lightyellow")
        txt_description.place(x=200, y=280, width=200, height=100)




        #button
        self.ajout_btn=Button(self.root, command=self.ajouter, text="Ajouter", font=("times new roman", 15, "bold"), cursor="hand2", bg="green", state="normal")
        self.ajout_btn.place(x=100, y=400, height=30)

        self.modifier_btn=Button(self.root, command=self.modifier,text="modifier", font=("times new roman", 15, "bold"), cursor="hand2", bg="yellow", state="disabled")
        self.modifier_btn.place(x=200, y=400, height=30)

        self.supprimer_btn=Button(self.root, command=self.supprimer, text="supprimer", font=("times new roman", 15, "bold"), cursor="hand2", bg="red", state="disabled")
        self.supprimer_btn.place(x=300, y=400, height=30)

        self.renitialiser_btn=Button(self.root, text="renitialiser", command=self.reini, font=("times new roman", 15, "bold"), cursor="hand2", bg="lightgray", state="normal")
        self.renitialiser_btn.place(x=420, y=400, height=30)

        #liste fournisseur
        listeFrame=Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=550, y=100, height=300, width=500)

        scroll_y= Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)


        scroll_x= Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)


        self.fournisseurliste = ttk.Treeview(listeFrame, columns=("forid", "nom","contact", "description"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_y.set)

        scroll_x.config(command=self.fournisseurliste.xview)
        scroll_y.config(command=self.fournisseurliste.yview)
        
        self.fournisseurliste.heading("forid", text="ID")
        self.fournisseurliste.heading("nom", text="nom")
        self.fournisseurliste.heading("contact", text="contact")
        self.fournisseurliste.heading("description", text="description")

        self.fournisseurliste["show"]="headings"
        self.fournisseurliste.pack(fill= BOTH, expand=1)

        self.fournisseurliste.bind("<ButtonRelease-1>", self.get_donne)



    def reini(self):
        self.txt_fourid.config(state="normal")
        self.ajout_btn.config(state="normal")
        self.modifier_btn.config(state="disable")
        self.supprimer_btn.config(state="disable")
        self.var_nom.set("")
        self.var_contact.set("")
        self.var_txt_description.set("")
        self.var_fourni_id.set("")
        self.var_recherche_text.set("")

        self.afficher()


    def supprimer(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()

        try:
            op=messagebox.askyesno("Confirmer", "voulez-vous vraiment supprimer")
            if op==True:
                cur.execute("delete from fournisseur where forid=?", (self.var_fourni_id.get(),))
                con.commit()

                self.afficher()
                self.reini()
                messagebox.showinfo("Succès", "suppression effectué")

        except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")
               

    def modifier(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()

        try:
            cur.execute("update fournisseur set nom=?, contact=?, description=? where forid=?", (

                        self.var_nom.get(),
                        self.var_contact.get(),
                        self.var_txt_description.get(),
                        self.var_fourni_id.get()


            ))
            con.commit()
            self.afficher()
            self.reini()
            messagebox.showinfo("Succès", "modification effectué avec succès")
        except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")
 




    def get_donne(self, ev):

        self.ajout_btn.config(state="disable")
        self.modifier_btn.config(state="normal")
        self.supprimer_btn.config(state="normal")
        self.txt_fourid.config(state="readonly")
        r = self.fournisseurliste.focus()
        contenu=self.fournisseurliste.item(r)
        row=contenu["values"]

        self.var_fourni_id.set(row[0])
        self.var_nom.set(row[1])
        self.var_contact.set(row[2])
        #self.var_txt_description.delete("1.0", END),
        self.var_txt_description.set(row[3])








    def afficher(self):


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:

            cur.execute("select * from fournisseur")
            rows=cur.fetchall()
            self.fournisseurliste.delete(*self.fournisseurliste.get_children())
            for row in rows:
                self.fournisseurliste.insert("", END, values=row)


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            if self.var_fourni_id.get()=="":
                messagebox.showerror("Erreur", "veillez mettre un id")
            else:
                cur.execute("select * from fournisseur where forid=?", (self.var_fourni_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "l'ID fournisseur existe deja")
                else:
                    cur.execute("insert into fournisseur (forid, nom , contact, description  ) values(?,?,?,?)", (
                        self.var_fourni_id.get(),
                        self.var_nom.get(),
                        self.var_contact.get(),
                        self.var_txt_description.get()

                    ))
                    con.commit()
                    self.afficher()
                    messagebox.showinfo("Succès", "Ajout effectué avec succès")


     


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def recherche(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
             if self.var_recherche_text.get()=="":
                messagebox.showerror("Erreur", "Qu'est ce que vous rechercher?")
             else:
                cur.execute("select * from fournisseur where forid=?", (self.var_recherche_text.get(),))
                row=cur.fetchone()
                if row!=None:
                     self.fournisseurliste.delete(*self.fournisseurliste.get_children())
                     self.fournisseurliste.insert("", END, values=row)
                else:
                     messagebox.showerror("Erreur", "aucun resultat trouvé")   



        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")





if __name__=="__main__":
            root=Tk()
            fournisseur(root)
            root.mainloop()