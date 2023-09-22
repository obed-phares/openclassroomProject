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


class lot:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("800x400")
        self.root.config(bg="white")

        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS lot(id text PRIMARY KEY, programme text, type text, budget text, debut text, prix)")
        con.commit()


        #les variables
        self.var_recherche_text=StringVar()
        self.var_id=StringVar()
        self.var_programme=StringVar()
        self.var_type=StringVar()
        self.var_prix=StringVar()
        self.var_budget=StringVar()
        self.var_debut=StringVar()

        ## option de recherche
        self.reche_option=Label(self.root, text="recherche par ID", font=("times new roma", 12), bg="white")
        self.reche_option.place(x=420, y=50)

        recherche_txt=Entry(self.root, textvariable=self.var_recherche_text , font=("times new roman ", 12, "bold"), bg="lightyellow").place(x=560, y=50)

        recherche_btn=Button(self.root, text="recherche", command=self.recherche,font=("times new roman", 12, "bold"), cursor="hand2", bg="blue", fg="white").place(x=600, y=28, height=20)

        recherche_btn=Button(self.root, text="tous", command=self.afficher ,font=("times new roman", 12, "bold"), cursor="hand2", bg="lightgray", fg="white").place(x=690, y=28, height=20)



        #tire
        titre =Label(self.root, text="ENREGISTREMENT LOT", font=("algerian", 13),  bg="cyan", justify=CENTER).pack(side=TOP, fill=X)

        #contenu
                #ligne 1
        lbl_id=Label(self.root, text="ID Lot", font=("times new roman", 13, "bold"), bg="white").place(x=10, y=50)
        self.txt_id = Entry(self.root, textvariable=self.var_id , font=("times new roman ", 12), bg="lightyellow")
        self.txt_id.place(x=200, y=50, width=150)



        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("select nomprogramme from programme")
        rows=cur.fetchall()

        
        lbl_programme=Label(self.root, text="Programme", font=("times new roman ", 13, "bold"), bg="white").place(x=10, y=100)
        txt_programme = ttk.Combobox(self.root, values=rows, textvariable=self.var_programme, state="r", justify="center", font=("times new roman", 12))
        txt_programme.place(x=200, y=100, width=150)
        txt_programme.set("selection")




        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("select type from maison")
        rows=cur.fetchall()

        
        lbl_programme=Label(self.root, text="Type maison", font=("times new roman ", 13, "bold"), bg="white").place(x=10, y=150)
        txt_programme = ttk.Combobox(self.root, values=rows, textvariable=self.var_type, state="r", justify="center", font=("times new roman", 12))
        txt_programme.place(x=200, y=150, width=150)
        txt_programme.set("selection")

        lbl_budget=Label(self.root, text="Budget Prévisionnel ", font=("times new roman", 13, "bold"), bg="white").place(x=10, y=200)
        txt_budget = Entry(self.root, textvariable = self.var_budget, font=("times new roman ", 12), bg="lightyellow")
        txt_budget.place(x=200, y=200, width=150)

        lbl_date_debut=Label(self.root, text="Date début ", font=("times new roman", 13, "bold"), bg="white").place(x=10, y=250)
        txt_date_debut = Entry(self.root, textvariable = self.var_debut, font=("times new roman ", 12), bg="lightyellow")
        txt_date_debut.place(x=200, y=250, width=150)



        lbl_prix=Label(self.root, text="Prix ", font=("times new roman", 13, "bold"), bg="white").place(x=10, y=300)
        txt_prix = Entry(self.root, textvariable = self.var_prix, font=("times new roman ", 12), bg="lightyellow")
        txt_prix.place(x=200, y=300, width=150)


        #button
        self.ajout_btn=Button(self.root, command=self.ajouter, text="Ajouter", font=("times new roman", 10, "bold"), cursor="hand2", bg="green", state="normal")
        self.ajout_btn.place(x=50, y=350, height=30)

        self.modifier_btn=Button(self.root, command=self.modifier,text="modifier", font=("times new roman", 10, "bold"), cursor="hand2", bg="yellow", state="disabled")
        self.modifier_btn.place(x=140, y=350, height=30)

        self.supprimer_btn=Button(self.root, command=self.supprimer, text="supprimer", font=("times new roman", 10, "bold"), cursor="hand2", bg="red", state="disabled")
        self.supprimer_btn.place(x=220, y=350, height=30)

        self.renitialiser_btn=Button(self.root, text="renitialiser", command=self.reini, font=("times new roman", 10, "bold"), cursor="hand2", bg="lightgray", state="normal")
        self.renitialiser_btn.place(x=300, y=350, height=30)

        #liste fournisseur
        listeFrame=Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=420, y=80, height=280, width=350)

        scroll_y= Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)


        scroll_x= Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)


        self.ilotliste = ttk.Treeview(listeFrame, columns=("id", "programme", "type","budget", "debut", "prix"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_y.set)

        scroll_x.config(command=self.ilotliste.xview)
        scroll_y.config(command=self.ilotliste.yview)
        
        self.ilotliste.heading("id", text="ID")
        self.ilotliste.heading("programme", text="programme")
        self.ilotliste.heading("type", text="type")
        self.ilotliste.heading("budget", text="budget")
        self.ilotliste.heading("debut", text="debut")
        self.ilotliste.heading("prix", text="prix")
        self.ilotliste["show"]="headings"
        self.ilotliste.pack(fill= BOTH, expand=1)

        self.ilotliste.bind("<ButtonRelease-1>", self.get_donne)



    def reini(self):
        self.txt_id.config(state="normal")
        self.ajout_btn.config(state="normal")
        self.modifier_btn.config(state="disable")
        self.supprimer_btn.config(state="disable")
        self.var_programme.set("selection")
        self.var_type.set("selection")
        self.var_budget.set("")
        self.var_debut.set("")
        self.var_prix.set("")
        self.var_id.set("")
        self.var_recherche_text.set("")

        self.afficher()


    def supprimer(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()

        try:
            op=messagebox.askyesno("Confirmer", "voulez-vous vraiment supprimer")
            if op==True:
                cur.execute("delete from lot where id=?", (self.var_id.get(),))
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
            cur.execute("update lot set programme=?, type=?,budget=?, debut=?, prix=? where id=?", (

                        self.var_programme.get(),
                        self.var_type.get(),
                        self.var_budget.get(),
                        self.var_debut.get(),
                        self.var_prix.get(),
                        self.var_id.get()


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
        self.txt_id.config(state="readonly")
        r = self.ilotliste.focus()
        contenu=self.ilotliste.item(r)
        row=contenu["values"]
        self.var_id.set(row[0])
        self.var_programme.set(row[1])
        self.var_type.set(row[2])
        self.var_budget.set(row[3])
        self.var_debut.set(row[4])
        self.var_prix.set(row[5])




    def afficher(self):


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:

            cur.execute("select * from lot")
            rows=cur.fetchall()
            self.ilotliste.delete(*self.ilotliste.get_children())
            for row in rows:
                self.ilotliste.insert("", END, values=row)


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Erreur", "veillez mettre un id")
            else:
                cur.execute("select * from lot where id=?", (self.var_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "l'ID lot existe deja")
                else:
                    cur.execute("insert into lot (id, programme , type,  budget, debut, prix  ) values(?,?,?,?,?,?)", (
                        self.var_id.get(),
                        self.var_programme.get(),
                        self.var_type.get(),
                        self.var_budget.get(),
                        self.var_debut.get(),
                        self.var_prix.get()

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
                cur.execute("select * from lot where id=?", (self.var_recherche_text.get(),))
                row=cur.fetchone()
                if row!=None:
                     self.ilotliste.delete(*self.ilotliste.get_children())
                     self.ilotliste.insert("", END, values=row)
                else:
                     messagebox.showerror("Erreur", "aucun resultat trouvé")   



        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")





if __name__=="__main__":
            root=Tk()
            lot(root)
            root.mainloop()