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

        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS produit(pid INTEGER PRIMARY KEY AUTOINCREMENT, categorie text, fournisseur text, nom text, prix text, quantite text, status text)")
        con.commit()
        


        #les variable

        self.var_recherche_type=StringVar()
        self.recherche_txt=StringVar()
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_four=StringVar()
        self.var_nom=StringVar()
        self.var_prix=StringVar()
        self.var_quantite=StringVar()
        self.var_status=StringVar()


        #self.four_liste=[]
        #self.liste_four()



        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("select nom from categorie")
        rows=cur.fetchall()
        # recuperation d un element dans la base de donné
        # l'element fournisseur va s afficher dans la partie produit
        produit_frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        produit_frame.place(x=10, y=10, width=500, height=400)
        titre =Label(produit_frame, text="Détail materiel", font=("times new roman", 15), bg="cyan").pack(side=TOP, fill=X)
     
        # recuperation d un element dans la base de donné
        # l'element categorie va s afficher dans la partie produit
        
        lbl_categorie=Label(produit_frame, text="Catégorie", font=("times new roman ", 15), bg="white").place(x=5, y=30)
        txt_categorie = ttk.Combobox(produit_frame, values=rows, textvariable= self.var_cat, state="r", justify="center", font=("times new roman", 15))
        txt_categorie.place(x=150, y=30)
        txt_categorie.set("selection")


        # recuperation d un element dans la base de donné
        # l'element fournisseur va s afficher dans la partie produit
        
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("select nom from fournisseur")
        rows=cur.fetchall()

        
        lbl_fournisseur=Label(produit_frame, text="Fournisseur", font=("times new roman ", 15), bg="white").place(x=5, y=80)
        txt_fournisseur = ttk.Combobox(produit_frame, values=rows, textvariable=self.var_four, state="r", justify="center", font=("times new roman", 15))
        txt_fournisseur.place(x=150, y=80)
        txt_fournisseur.set("selection")

        lbl_nom=Label(produit_frame, text="Nom materiel", font=("times new roman ", 15), bg="white").place(x=5, y=130)
        txt_nom=Entry(produit_frame, textvariable=self.var_nom , font=("times new roman", 15), bg="lightyellow").place(x=150, y=130, width=220)

        lbl_prix=Label(produit_frame, text="Prix", font=("times new roman ", 15), bg="white").place(x=5, y=180)
        txt_prix=Entry(produit_frame, textvariable=self.var_prix, font=("times new roman", 15), bg="lightyellow").place(x=150, y=180, width=220)

        lbl_quantité=Label(produit_frame, text="Quantité", font=("times new roman ", 15), bg="white").place(x=5, y=230)
        txt_quantité=Entry(produit_frame, textvariable=self.var_quantite, font=("times new roman", 15), bg="lightyellow").place(x=150, y=230, width=220)

        lbl_status=Label(produit_frame, text="Status", font=("times new roman ", 15), bg="white").place(x=5, y=280)
        txt_status = ttk.Combobox(produit_frame, textvariable=self.var_status, values=["Actif", "Inactif"], state="r", justify="center", font=("times new roman", 15))
        txt_status.place(x=150, y=280)
        txt_status.current(0)


        #button

        self.ajouter_btn= Button(produit_frame, command=self.ajouter, text="Ajouter",state="normal" , font=("times new roman", 13), cursor="hand2", bg="green", bd=3)
        self.ajouter_btn.place(x=30, y=330, width=80)

        self.modifier_btn= Button(produit_frame, text="modifier", command=self.modifier ,state="disabled" , font=("times new roman", 13), cursor="hand2", bg="red", bd=3)
        self.modifier_btn.place(x=130, y=330, width=80)

        self.supprimer_btn= Button(produit_frame,  command=self.supprimer ,text="supprimer",state="disabled" , font=("times new roman", 13), cursor="hand2", bg="yellow", bd=3)
        self.supprimer_btn.place(x=230, y=330, width=80)

        self.reini_btn= Button(produit_frame, command=self.reini, text="renitialiser", font=("times new roman", 13), cursor="hand2", bg="gray", bd=3)
        self.reini_btn.place(x=330, y=330, width=80)


        #frame recherche

        reche_frame = LabelFrame(self.root, text="Rechercher matière", font=("times new roman ", 15), bd=3, relief=RIDGE, bg="white")
        reche_frame.place(x=550, y=10, height=70, width=500)

        txt_reche_option = ttk.Combobox(reche_frame, values=["categorie", "fournisseur", "nom"], textvariable=self.var_recherche_type ,  state="r", justify="center", font=("times new roman", 15))
        txt_reche_option.place(x=5, y=5, width=150)
        txt_reche_option.current(0)
        txt_reche=Entry(reche_frame, font=("times new roman", 15), textvariable=self.recherche_txt, bg="lightyellow").place(x=160, y=5, width=180)

        rechercher_btn= Button(reche_frame, command=self.recherche ,text="Recherche", font=("times new roman", 13), cursor="hand2", bg="blue", bd=3)
        rechercher_btn.place(x=350, y=5, height=25)
        tous_btn= Button(reche_frame, text="Tous", command=self.afficher, font=("times new roman", 13), cursor="hand2", bg="red", bd=3)
        tous_btn.place(x=445, y=5, height=25)

        listeFrame=Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=550, y=100, height=300, width=530)

        scroll_y= Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)


        scroll_x= Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        #le produit remplace la matiere dans notre cas
        self.produitliste = ttk.Treeview(listeFrame, columns=("pid", "categorie", "fournisseur", "nom", "prix", "quantite", "status"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_y.set)

        scroll_x.config(command=self.produitliste.xview)
        scroll_y.config(command=self.produitliste.yview)
        
        self.produitliste.heading("pid", text="ID")
        self.produitliste.heading("categorie", text="categorie")
        self.produitliste.heading("fournisseur", text="fournisseur")
        self.produitliste.heading("nom", text="nom")
        self.produitliste.heading("prix", text="prix")
        self.produitliste.heading("quantite", text="quantite")
        self.produitliste.heading("status", text="status")
        self.produitliste["show"]="headings"
        self.produitliste.pack(fill= BOTH, expand=1)

        #on appelle la fonction get_donne
        self.produitliste.bind("<ButtonRelease-1>", self.get_donne)
        self.afficher()


#fonction
   # def liste_four(self):
    #    self.four_liste.append("vide")
     #   con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
      #  cur=con.cursor()
       # try:
        #    cur.execute("select nom from fournisseur")
         #   four=cur.fetchall()
          #  if len(four)>0:
           #     del self.four_liste[:]
            #    self.four_liste.append("selection")
             #   for i in four:
              #      sel.four_liste.append(i[0])



       # except Exception as ex:
        #      messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def reini(self):
        self.ajouter_btn.config(state="normal")
        self.modifier_btn.config(state="disable")
        self.supprimer_btn.config(state="disable")
        self.var_pid.set("")
        self.var_cat.set("selection")
        self.var_nom.set("selection")
        self.var_prix.set("")
        self.var_quantite.set("")
        self.var_status.set("Active")
        self.recherche_txt.set("")

        self.afficher()



    def supprimer(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()

        try:
            op=messagebox.askyesno("Confirmer", "voulez-vous vraiment supprimer")
            if op==True:
                cur.execute("delete from produit where pid=?", (self.var_pid.get(),))
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
            if self.var_pid.get()=="":
                messagebox.showerror("Erreur", "Selectionnez un ID")
            else:
                cur.execute("select * produit where pid=?", (self.var_pid.get(),))
                row=cur.fetchall()
                if row==None:
                    messagebox.showerror("Erreur", "veillez Selectionnez un materiel sur la liste")
                else:
                    cur.execute("update produit set categorie=?, fournisseur=?, nom=?, quantite=?, status=? where pid=?", (



                        self.var_cat.get(),
                        self.var_four.get(),
                        self.var_nom.get(),
                        self.var_prix.get(),
                        self.var_quantite.get(),
                        self.var_status.get(),
                        self.var_pid.get()




                    ))

                    con.commit()
                    self.afficher()
                    #self.reini()
                messagebox.showinfo("Succès", "modification effectué avec succès")
        except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")
 


        #la fonction get_donne permet la selection
    def get_donne(self, ev):

        self.ajouter_btn.config(state="disable")
        self.modifier_btn.config(state="normal")
        self.supprimer_btn.config(state="normal")
        
        r = self.produitliste.focus()
        contenu=self.produitliste.item(r)
        row=contenu["values"]
        self.var_pid.set([0])
        self.var_cat.set([1])
        self.var_four.set([2])
        self.var_nom.set([3])
        self.var_prix.set([4])
        self.var_quantite.set([5])
        self.var_status.set([6])
        #self.reini()




    def afficher(self):


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:

            cur.execute("select * from produit")
            rows=cur.fetchall()
            self.produitliste.delete(*self.produitliste.get_children())
            for row in rows:
                self.produitliste.insert("", END, values=row)


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")





    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            if self.var_cat.get()=="selection":
                messagebox.showerror("Erreur", "veillez selection une categorie")
            else:
                cur.execute("select * from produit where nom=?", (self.var_nom.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "le materiel existe deja")
                else:
                    cur.execute("insert into produit (categorie, fournisseur , nom, prix, quantite, status  ) values(?,?,?,?,?,?)", (
                        self.var_cat.get(),
                        self.var_four.get(),
                        self.var_nom.get(),
                        self.var_prix.get(),
                        self.var_quantite.get(),
                        self.var_status.get()

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
             if self.var_recherche_txt.get()=="":
                messagebox.showerror("Erreur", "Qu'est ce que vous rechercher?")
             else:
                cur.execute("select * from produit where" +self.var_recherche_txt.get()+  "LIKE '%'" +self.var_recherche_txt.get()+"'%")
                rows=cur.fetchone()
                if len(rows)!=0:
                    self.produitliste.delete(*self.produitliste.get_children())
                    for row in rows:
                        self.produitliste.insert("", END, values=row)
                else:
                     messagebox.showerror("Erreur", "aucun resultat trouvé")   



        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")




if __name__=="__main__":
            root=Tk()
            categorie(root)
            root.mainloop()