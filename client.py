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


class client:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("1300x1300")
        self.root.config(bg="#eff5f6")

        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS client(clid text PRIMARY KEY, nom text, prenom text, sexe text, fonction text, cni text,  nomEntreprise text, naissance text, residence text, nationalite text, consulaire text, contact text, email text, lot text, budget text, type text, typeFinition text, dateSoucription text)")
        con.commit()


        #les variables
        self.var_recherche_text=StringVar()
        self.var_clid=StringVar()
        self.var_nom=StringVar()
        self.var_prenom=StringVar()
        self.var_sexe=StringVar()
        self.var_fonction=StringVar()
        self.var_nomEntreprise=StringVar()
        self.var_cni=StringVar()
        self.var_naissance=StringVar()
        self.var_residence=StringVar()
        self.var_nationalite=StringVar()
        self.var_consulaire=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_lot=StringVar()
        self.var_budget=StringVar()
        self.var_type=StringVar()
        self.var_typefinition=StringVar()
        self.var_dateSoucription=StringVar()
        #self.var_description=StringVar()
 

        ## option de recherche
        self.reche_option=Label(self.root, text="recherche par ID", font=("times new roma", 12), bg="white")
        self.reche_option.place(x=580, y=40)

        recherche_txt=Entry(self.root, textvariable=self.var_recherche_text , font=("times new roman ", 12), bg="lightyellow").place(x=700, y=40, height=20)

        recherche_btn=Button(self.root, text="recherche", command=self.recherche,font=("times new roman", 12, "bold"), cursor="hand2", bg="blue", fg="white").place(x=900, y=40, height=25)

        recherche_btn=Button(self.root, text="tous", command=self.afficher ,font=("times new roman", 12, "bold"), cursor="hand2", bg="lightgray", fg="white").place(x=990, y=40, height=25)



        #tire
        titre =Label(self.root, text="client", font=("algerian", 13),  bg="cyan", justify=CENTER).place(x=0, y=0, width=1300)

        #contenu
                #ligne 1
        lbl_fourid=Label(self.root, text="ID Client", font=("times new roman", 13), bg="white").place(x=200, y=70)
        self.txt_fourid = Entry(self.root, textvariable=self.var_clid , font=("times new roman ", 13), bg="lightyellow")
        self.txt_fourid.place(x=200, y=90)

        lbl_nom=Label(self.root, text="Nom complet", font=("times new roman", 13), bg="white").place(x=390, y=70)
        txt_nom = Entry(self.root, textvariable=self.var_nom, font=("times new roman ", 13), bg="lightyellow")
        txt_nom.place(x=390, y=90, width=200)


        txt_contact = Entry(self.root, textvariable=self.var_prenom, font=("times new roman ", 13), bg="lightyellow").place(x=660, y=90, width=200)
        #ligne 2

        lbl_sexe=Label(self.root, text="Sexe", font=("times new roman", 13), bg="white").place(x=200, y=120)
        txt_sexe = Entry(self.root, textvariable = self.var_sexe, font=("times new roman ", 13), bg="lightyellow")
        txt_sexe.place(x=200, y=140)

        lbl_fonction=Label(self.root, text="Fonction", font=("times new roman", 13), bg="white").place(x=390, y=120)
        txt_fonction = Entry(self.root, textvariable = self.var_fonction, font=("times new roman ", 13), bg="lightyellow")
        txt_fonction.place(x=390, y=140, width=200)

        lbl_nomEntreprise=Label(self.root, text="Nom de l'Entreprise", font=("times new roman", 13), bg="white").place(x=660, y=120)
        txt_nomEntreprise = Entry(self.root, textvariable = self.var_nomEntreprise, font=("times new roman ", 13), bg="lightyellow")
        txt_nomEntreprise.place(x=660, y=140, width=200)

         # ligne 3
        lbl_cni=Label(self.root, text="CNI", font=("times new roman", 13), bg="white").place(x=200, y=170)
        txt_cni = Entry(self.root, textvariable = self.var_cni, font=("times new roman ", 13), bg="lightyellow")
        txt_cni.place(x=200, y=190)

        lbl_naissance=Label(self.root, text="Fonction", font=("times new roman", 13), bg="white").place(x=390, y=170)
        txt_naissance = Entry(self.root, textvariable = self.var_naissance, font=("times new roman ", 13), bg="lightyellow")
        txt_naissance.place(x=390, y=190, width=200)

        lbl_residence=Label(self.root, text="Lieu de résidence", font=("times new roman", 13), bg="white").place(x=660, y=170)
        txt_residence = Entry(self.root, textvariable = self.var_residence, font=("times new roman ", 13), bg="lightyellow")
        txt_residence.place(x=660, y=190, width=200)


        #ligne 4
        lbl_nationalite=Label(self.root, text="Nationalité", font=("times new roman", 13), bg="white").place(x=200, y=220)
        txt_nationalite = Entry(self.root, textvariable = self.var_nationalite, font=("times new roman ", 13), bg="lightyellow")
        txt_nationalite.place(x=200, y=240)

        lbl_consulaire=Label(self.root, text="Consulaire", font=("times new roman", 13), bg="white").place(x=390, y=220)
        txt_consulaire = Entry(self.root, textvariable = self.var_consulaire, font=("times new roman ", 13), bg="lightyellow")
        txt_consulaire.place(x=390, y=240, width=200)

        lbl_contact=Label(self.root, text="Contact", font=("times new roman", 13), bg="white").place(x=660, y=220)
        txt_contact = Entry(self.root, textvariable = self.var_contact, font=("times new roman ", 13), bg="lightyellow")
        txt_contact.place(x=660, y=240, width=200)




        #ligne 5
        lbl_email=Label(self.root, text="E-mail", font=("times new roman", 13), bg="white").place(x=200, y=260)
        txt_email = Entry(self.root, textvariable = self.var_email, font=("times new roman ", 13), bg="lightyellow")
        txt_email.place(x=200, y=280)

        lbl_lot=Label(self.root, text="Lot", font=("times new roman", 13), bg="white").place(x=390, y=260)
        txt_lot = Entry(self.root, textvariable = self.var_lot, font=("times new roman ", 13), bg="lightyellow")
        txt_lot.place(x=390, y=280, width=200)

        lbl_budget=Label(self.root, text="Contact", font=("times new roman", 13), bg="white").place(x=660, y=260)
        txt_budget = Entry(self.root, textvariable = self.var_budget, font=("times new roman ", 13), bg="lightyellow")
        txt_budget.place(x=660, y=280, width=200)



                #ligne 5
        lbl_type=Label(self.root, text="Type", font=("times new roman", 13), bg="white").place(x=200, y=290)
        txt_type = Entry(self.root, textvariable = self.var_type, font=("times new roman ", 13), bg="lightyellow")
        txt_type.place(x=200, y=310)

        lbl_typeFinition=Label(self.root, text="Type de finition", font=("times new roman", 13), bg="white").place(x=390, y=290)
        txt_typeFinition = Entry(self.root, textvariable = self.var_typefinition, font=("times new roman ", 13), bg="lightyellow")
        txt_typeFinition.place(x=390, y=310, width=200)

        lbl_dateSouscription=Label(self.root, text="Date de scoucription", font=("times new roman", 13), bg="white").place(x=660, y=290)
        txt_dateSouscription = Entry(self.root, textvariable = self.var_dateSoucription, font=("times new roman ", 13), bg="lightyellow")
        txt_dateSouscription.place(x=660, y=310, width=200)






        #button
        self.ajout_btn=Button(self.root, command=self.ajouter, text="Ajouter", font=("times new roman", 15, "bold"), cursor="hand2", bg="green", state="normal")
        self.ajout_btn.place(x=400, y=350, height=30)

        self.modifier_btn=Button(self.root, command=self.modifier,text="modifier", font=("times new roman", 15, "bold"), cursor="hand2", bg="yellow", state="disabled")
        self.modifier_btn.place(x=500, y=350, height=30)

        self.supprimer_btn=Button(self.root, command=self.supprimer, text="supprimer", font=("times new roman", 15, "bold"), cursor="hand2", bg="red", state="disabled")
        self.supprimer_btn.place(x=600, y=350, height=30)

        self.renitialiser_btn=Button(self.root, text="renitialiser", command=self.reini, font=("times new roman", 15, "bold"), cursor="hand2", bg="lightgray", state="normal")
        self.renitialiser_btn.place(x=720, y=350, height=30)

        #liste client
        listeFrame=Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=10, y=380, height=140, width=1300)

        scroll_y= Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)


        scroll_x= Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)


        self.clientliste = ttk.Treeview(listeFrame, columns=("clid", "nom","prenom", "sexe", "fonction", "nomEntreprise", "cni", "naissance", "residence", "nationalite", "consulaire", "contact", "email", "lot", "budget", "type", "typeFinition", "dateSoucription"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_y.set)

        scroll_x.config(command=self.clientliste.xview)
        scroll_y.config(command=self.clientliste.yview)
        
        self.clientliste.heading("clid", text="ID")
        self.clientliste.heading("nom", text="nom")
        self.clientliste.heading("prenom", text="prenom")
        self.clientliste.heading("sexe", text="sexe")
        self.clientliste.heading("fonction", text="fonction")
        self.clientliste.heading("nomEntreprise", text="nom de l'Entreprise")
        self.clientliste.heading("cni", text="cni")
        self.clientliste.heading("naissance", text="Naissance")
        self.clientliste.heading("residence", text="Résidence")
        self.clientliste.heading("nationalite", text="nationalite")
        self.clientliste.heading("consulaire", text="consulaire")
        self.clientliste.heading("contact", text="contact")
        self.clientliste.heading("email", text="email")
        self.clientliste.heading("lot", text="lot")
        self.clientliste.heading("budget", text="budget")
        self.clientliste.heading("type", text="type")
        self.clientliste.heading("typeFinition", text="type de finition")
        self.clientliste.heading("dateSoucription", text="date de souscription")


        self.clientliste["show"]="headings"
        self.clientliste.pack(fill= BOTH, expand=1)

        self.clientliste.bind("<ButtonRelease-1>", self.get_donne)



    def reini(self):
        self.txt_fourid.config(state="normal")
        self.ajout_btn.config(state="normal")
        self.modifier_btn.config(state="disable")
        self.supprimer_btn.config(state="disable")
        self.var_nom.set("")
        self.var_prenom.set("")
        self.var_sexe.set("")
        self.var_fonction.set("")
        self.var_cni.set("")
        self.var_naissance.set("")
        self.var_residence.set("")
        self.var_nomEntreprise.set("")
        self.var_nationalite.set("")
        self.var_consulaire.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_lot.set("")
        self.var_budget.set("")
        self.var_type.set("")
        self.var_typefinition.set("")
        self.var_dateSoucription.set("")
        

        self.var_clid.set("")
        self.var_recherche_text.set("")


        self.afficher()


    def supprimer(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()

        try:
            op=messagebox.askyesno("Confirmer", "voulez-vous vraiment supprimer")
            if op==True:
                cur.execute("delete from client where clid=?", (self.var_clid.get(),))
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
            cur.execute("update client set nom=?, prenom=?, sexe=?, fonction=?, nomEntreprise=?, cni=?, naissance=?, residence=?n Nationalité=?, Consulaire=?, contact=?, email=?, lot=?, budget=?, type=?, typeFinition=?, dateSoucription where clid=?", (

                        self.var_nom.get(),
                        self.var_prenom.get(),
                        self.var_sexe.get(),
                        self.var_fonction.get(),
                        self.var_nomEntreprise.get(),
                        self.var_cni.get(),
                        self.var_naissance.get(),
                        self.var_residence.get(),
                        self.var_nationalite.get(),
                        self.var_consulaire.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_lot.get(),
                        self.var_budget.get(),
                        self.var_type.get(),
                        self.var_typefinition.get(),
                        self.var_dateSoucription.get(),
                        self.var_clid.get()





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
        r = self.clientliste.focus()
        contenu=self.clientliste.item(r)
        row=contenu["values"]

        self.var_clid.set(row[0]),
        self.var_nom.set(row[1]),
        self.var_prenom.set(row[2]),
        #self.var_txt_description.delete("1.0", END),
        self.var_sexe.set(row[3]),
        self.var_fonction.set(row[4]),
        self.var_nomEntreprise.set(row[5]),
        self.var_cni.set(row[6]),
        self.var_naissance.set(row[7]),
        self.var_residence.set(row[8]),
        self.var_nationalite.set(row[9]),
        self.var_consulaire.set(row[10]),
        self.var_contact.set(row[11])
        self.var_email.set(row[12]),
        self.var_lot.set(row[13]),
        self.var_budget.set(row[14])
        self.var_type.set(row[15]),
        self.var_typefinition.set(row[16]),
        self.var_dateSoucription.set(row[17])








    def afficher(self):


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:

            cur.execute("select * from client")
            rows=cur.fetchall()
            self.clientliste.delete(*self.clientliste.get_children())
            for row in rows:
                self.clientliste.insert("", END, values=row)


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            if self.var_clid.get()=="":
                messagebox.showerror("Erreur", "veillez mettre un id")
            else:
                cur.execute("select * from client where clid=?", (self.var_clid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "l'ID client existe deja")
                else:
                    cur.execute("insert into client (clid, nom , prenom, sexe, fonction, nomEntreprise, cni, naissance, residence, nationalite, Consulaire, Contact, email, lot, budget, type, typeFinition, dateSoucription ) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_clid.get(),
                        self.var_nom.get(),
                        self.var_prenom.get(),
                        self.var_sexe.get(),
                        self.var_fonction.get(),
                        self.var_nomEntreprise.get(),
                        self.var_cni.get(),
                        self.var_naissance.get(),
                        self.var_residence.get(),
                        self.var_nationalite.get(),
                        self.var_consulaire.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_lot.get(),
                        self.var_budget.get(),
                        self.var_type.get(),
                        self.var_typefinition.get(),
                        self.var_dateSoucription.get()


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
                cur.execute("select * from client where clid=?", (self.var_recherche_text.get(),))
                row=cur.fetchone()
                if row!=None:
                     self.clientliste.delete(*self.clientliste.get_children())
                     self.clientliste.insert("", END, values=row)
                else:
                     messagebox.showerror("Erreur", "aucun resultat trouvé")   



        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")





if __name__=="__main__":
            root=Tk()
            client(root)
            root.mainloop()