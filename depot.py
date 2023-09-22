from tkinter import *
from PIL import Image, ImageTk
import datetime
import tkinter as tk
from PIL import Image, ImageTk
import time
from tkinter import messagebox, ttk
import sqlite3





class depot:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("1000x1000")
        self.root.config(bg="white")


        #liste des variable
        self.var_cat_id=StringVar()
        self.var_nom = StringVar()


        # base de donnée
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS depot(cid INTEGER PRIMARY KEY AUTOINCREMENT, nom text)")
        con.commit()

        #Premiere Barre
        self.entente = Frame(self.root, bg="orange")
        self.entente.place(x=0, y = 0, width=1070, height=30)
        
        self.deconnecte = Button(self.root, text="deconnecter", font=("time new roman", 10), bd = 0, fg = "#000000", bg = "orange", cursor="hand2", relief = "flat" )
        self.deconnecte.place(x=800, y = 3)
        
        self.aide = Button(self.root, text="Aide", font=("time new roman", 10), bd = 0, fg = "#000000", cursor="hand2", bg = "orange", relief = "flat" )
        self.aide.place(x=905, y = 3)
        
        self.demo = Button(self.root, text="Demo", font=("time new roman", 10, "bold"), bd = 0, fg = "#000000", cursor="hand2" ,bg = "orange", relief = "flat")
        self.demo.place(x=620, y = 3)
        
        self.info = Button(self.root, text="info@sciambtp.com", font=("time new roman", 10, "bold"), bd = 0, fg = "#000000", cursor="hand2", bg = "orange", relief = "flat" )
        self.info.place(x=420, y = 3)
        
        
        self.demo = Button(self.root, text="Demo", font=("time new roman", 10, "bold"), bd = 0, fg = "#000000", cursor="hand2" ,bg = "orange", relief = "flat")
        self.demo.place(x=620, y = 3)
        
        
        #corps de la page

       

        self.lFrame =LabelFrame(self.root, bg="GhostWhite")
        self.lFrame.place(x=0, y = 30, width=400, height=700)
        title = Label(self.lFrame, text=" Enregistrement depot", font=("time new roman", 15), bd= 3, bg="blue").pack(side=TOP, fill=X)
        
        depot=Label(self.root, text="Nom depot", font=("times new roman", 15), bg="white").place(x=470, y=80)

        depot=Entry(self.root, textvariable= self.var_nom ,font=("times new roman", 15), bg="lightyellow").place(x=470, y=110, width=200)

        btn_ajouter=Button(self.root, command=self.ajouter, text="Ajouter", font=("times new roman", 15), bg="blue", cursor="hand2").place(x=700, y=110, width=110, height=30 )
        btn_supprimer=Button(self.root, command=self.suprimer, text="supprimer", font=("times new roman", 15), bg="lightgray", cursor="hand2").place(x=820, y=110, width=100, height=30 )


        #liste categorie


        scroll_y= Scrollbar(self.lFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)


        scroll_x= Scrollbar(self.lFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.depoliste= ttk.Treeview(self.lFrame, columns = ("cid", "nom", ), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
        scroll_x.config(command=self.depoliste.xview)
        scroll_y.config(command=self.depoliste.yview)
        


        self.depoliste.heading("cid", text="ID")
        self.depoliste.heading("nom", text="nom")

        self.depoliste["show"]="headings"
        self.depoliste.pack(fill=BOTH, expand=1)
        self.depoliste.bind("<ButtonRelease-1>", self.get_donne)


     
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
                cur.execute("delete from depot where cid=?", (self.var_cat_id.get(),))
                con.commit()
                self.var_cat_id.set("")
                self.var_nom.set("")
                self.afficher()
                
                messagebox.showinfo("Succès", "suppression effectué")



        except Exception as ex:
            
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


    def get_donne(self, ev):

        r = self.depoliste.focus()
        contenu=self.depoliste.item(r)
        row=contenu["values"]

        self.var_cat_id.set(row[0])
        self.var_nom.set(row[1])





    def afficher(self):


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:

            cur.execute("select * from depot")
            rows=cur.fetchall()
            self.depoliste.delete(*self.depoliste.get_children())
            for row in rows:
                self.depoliste.insert("", END, values=row)


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")



    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            if self.var_nom.get()=="":
                messagebox.showerror("Erreur", "veillez saisir le nom depot")
            else:
                cur.execute("select * from depot where nom=?", (self.var_nom.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Erreur", "la depot existe deja")
                else:
                    cur.execute("insert into depot (nom) values (?)", (self.var_nom.get(),))
                    con.commit()
                    self.afficher()
                    self.var_cat_id.set("")
                    self.var_nom.set("")
                    messagebox.showinfo("Succès", "enregistrement effectué")


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


if __name__=="__main__":
            root=Tk()
            depot(root)
            root.mainloop()