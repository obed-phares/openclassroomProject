from tkinter import *
from PIL import Image, ImageTk
import datetime
import tkinter as tk
from PIL import Image, ImageTk
import time
from tkinter import messagebox, ttk
import sqlite3


class categorie:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("1500x1500")
        self.root.config(bg="white")


        #liste des variable
        self.var_cat_id=StringVar()
        self.var_nom = StringVar()


        # base de donnée
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS categorie(cid INTEGER PRIMARY KEY AUTOINCREMENT, nom text)")
        con.commit()

        title=Label(self.root, text="Gestion catégorie ouvrier", font=("times new roman", 20, "bold"), bg="cyan", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=10)

        #Contenu
        lbl_categorie=Label(self.root, text="Saisir catégorie materiel", font=("times new roman", 15), bg="white").place(x=50, y=80)

        txt_categorie=Entry(self.root, textvariable=self.var_nom,font=("times new roman", 15), bg="lightyellow").place(x=50, y=110, width=200)

        btn_ajouter=Button(self.root, command=self.ajouter, text="Ajouter", font=("times new roman", 15), bg="blue", cursor="hand2").place(x=300, y=100, width=100, height=30 )
        btn_supprimer=Button(self.root, command=self.suprimer, text="supprimer", font=("times new roman", 15), bg="lightgray", cursor="hand2").place(x=420, y=100, width=100, height=30 )

        #liste categorie

        listeFrame=Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=600, y=100, height=200, width=450)

        scroll_y= Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)


        scroll_x= Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.categorieliste= ttk.Treeview(listeFrame, columns = ("cid", "nom", ), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
        scroll_x.config(command=self.categorieliste.xview)
        scroll_y.config(command=self.categorieliste.yview)
        


        self.categorieliste.heading("cid", text="ID")
        self.categorieliste.heading("nom", text="nom")

        self.categorieliste["show"]="headings"
        self.categorieliste.pack(fill=BOTH, expand=1)
        self.categorieliste.bind("<ButtonRelease-1>", self.get_donne)


     
        self.afficher()

        #self.cat1=Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\images1.jpg")
        #self.cat1=self.cat1.resize((200, 200), Image.LANCZOS)
        #self.cat1=ImageTk.PhotoImage(self.cat1)

        #self.lbl_ima_cat1 =Label(self.root, bd=7, image=self.cat1)
        #self.lbl_ima_cat1.place(x=200, y=250)
    def suprimer(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            op=messagebox.askyesno("Confirmer", "voulez-vous vraiment supprimer")
            if op==True:
                cur.execute("delete from categorie where cid=?", (self.var_cat_id.get(),))
                con.commit()
                self.var_cat_id.set("")
                self.var_nom.set("")
                self.afficher()
                
                messagebox.showinfo("Succès", "suppression effectué")



        except Exception as ex:
            
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


    def get_donne(self, ev):

        r = self.categorieliste.focus()
        contenu=self.categorieliste.item(r)
        row=contenu["values"]

        self.var_cat_id.set(row[0])
        self.var_nom.set(row[1])





    def afficher(self):


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:

            cur.execute("select * from categorie")
            rows=cur.fetchall()
            self.categorieliste.delete(*self.categorieliste.get_children())
            for row in rows:
                self.categorieliste.insert("", END, values=row)


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")



    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            if self.var_nom.get()=="":
                messagebox.showerror("Erreur", "veillez saisir une categorie")
            else:
                cur.execute("select * from categorie where nom=?", (self.var_nom.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Erreur", "la categorie existe deja")
                else:
                    cur.execute("insert into categorie (nom) values (?)", (self.var_nom.get(),))
                    con.commit()
                    self.afficher()
                    self.var_cat_id.set("")
                    self.var_nom.set("")
                    messagebox.showinfo("Succès", "enregistrement effectué")


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


if __name__=="__main__":
            root=Tk()
            categorie(root)
            root.mainloop()