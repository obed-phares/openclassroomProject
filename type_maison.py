
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
        self.root.geometry("500x300")
        self.root.config(bg="white")

        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS maison(id text PRIMARY KEY, type text)")
        con.commit()


        #les variables
        self.var_id=StringVar()
        self.var_type=StringVar()

 




        #tire
        titre =Label(self.root, text="type maison", font=("algerian", 15),  bg="cyan", justify=CENTER).pack(side=TOP, fill=X)

        #contenu
                #ligne 1
        self.lbl_id=Label(self.root, text="ID maison", font=("times new roman", 13), bg="white").place(x=10, y=70)
        self.txt_id = Entry(self.root, textvariable=self.var_id , font=("times new roman ", 13), bg="lightyellow")
        self.txt_id.place(x=100, y=70, width=150)

        lbl_type=Label(self.root, text="type maison", font=("times new roman", 13), bg="white").place(x=10, y=100)
        txt_type = Entry(self.root, textvariable=self.var_type, font=("times new roman ", 13), bg="lightyellow")
        txt_type.place(x=100, y=100, width=150)



        #button
        self.ajout_btn=Button(self.root, command=self.ajouter, text="Ajouter", font=("times new roman", 10, "bold"), cursor="hand2", bg="green", state="normal")
        self.ajout_btn.place(x=10, y=150, height=30)

        self.supprimer_btn=Button(self.root, command=self.supprimer, text="supprimer", font=("times new roman", 10, "bold"), cursor="hand2", bg="red", state="disabled")
        self.supprimer_btn.place(x=100, y=150, height=30)

        self.renitialiser_btn=Button(self.root, text="renitialiser", command=self.reini, font=("times new roman", 10, "bold"), cursor="hand2", bg="lightgray", state="normal")
        self.renitialiser_btn.place(x=190, y=150, height=30)

        #liste fournisseur
        listeFrame=Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=0, y=200, height=100, width=490)

        scroll_y= Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)


        scroll_x= Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)


        self.maisonliste = ttk.Treeview(listeFrame, columns=("id", "type"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_y.set)

        scroll_x.config(command=self.maisonliste.xview)
        scroll_y.config(command=self.maisonliste.yview)
        
        self.maisonliste.heading("id", text="ID")
        self.maisonliste.heading("type", text="type maison")
        self.maisonliste["show"]="headings"
        self.maisonliste.pack(fill= BOTH, expand=1)

        self.maisonliste.bind("<ButtonRelease-1>", self.get_donne)



    def reini(self):
        self.ajout_btn.config(state="normal")
        self.supprimer_btn.config(state="disable")
        self.var_type.set("")
        self.var_id.set("")
        self.afficher()


    def supprimer(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()

        try:
            op=messagebox.askyesno("Confirmer", "voulez-vous vraiment supprimer")
            if op==True:
                cur.execute("delete from maison where id=?", (self.var_id.get(),))
                con.commit()

                self.afficher()
                self.reini()
                messagebox.showinfo("Succès", "suppression effectué")

        except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")
               



    def get_donne(self, ev):


        self.ajout_btn.config(state="disable")
        self.supprimer_btn.config(state="normal")
        
        r = self.maisonliste.focus()
        contenu=self.maisonliste.item(r)
        row=contenu["values"]
        self.var_id.set([0])
        self.var_type.set([1])


    def afficher(self):


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:

            cur.execute("select * from maison")
            rows=cur.fetchall()
            self.maisonliste.delete(*self.maisonliste.get_children())
            for row in rows:
                self.maisonliste.insert("", END, values=row)


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Erreur", "veillez mettre un id")
            else:
                cur.execute("select * from maison where id=?", (self.var_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "l'ID type maison existe deja")
                else:
                    cur.execute("insert into maison (id, type  ) values(?,?)", (
                        self.var_id.get(),
                        self.var_type.get()

                    ))
                    con.commit()
                    self.afficher()
                    messagebox.showinfo("Succès", "Ajout effectué avec succès")
     
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

if __name__=="__main__":
            root=Tk()
            fournisseur(root)
            root.mainloop()