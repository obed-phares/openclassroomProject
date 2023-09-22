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
import time
import sqlite3
import os




class caisse:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("1500x1500")
        self.root.config(bg="white")
        self.root.focus_force()

        self.cart_list=[]
        self.ck_print=0

        self.var_cname=StringVar()
        self.var_contact=StringVar()
        self.var_facture=StringVar()

        # titre
        self.icon_title=ImageTk.PhotoImage(file=r"C:\Users\USER\Desktop\sciam_btp\image\logo.png")
        titre =Label(self.root, image=self.icon_title, text="Gestion SCIAM", font=("times new roman ", 15, "bold"), bg="cyan", fg="black", anchor="w", padx=20, compound=LEFT).place(x=0, y=0, width=1400, height=30)

        #bouton deconnecter
        btn_deconnecter=Button(self.root, command=self.deconnecter ,text="Déconnecter", font=("times new roman ", 11), bg="blue", fg="black", bd=3).place(x=950, y=0, width=90)
        #heure
        self.lbl_heure= Label(self.root, text="Bienvenue à SCIAM GESCOM \t\t Date: DD-MM-YYY \t\t Heure: HH:MM:SS ", font=("times new roman ", 12), bg="black", fg="white")
        self.lbl_heure.place(x=0, y=33, relwidth=1, height=30)
        self.modifier_heure()

        #produit qui represente le materiel

        self.var_recherche=StringVar()

        produitFrame1=Frame(self.root,bd=4, relief=RIDGE, bg="white")
        produitFrame1.place(x=10, y=70, width=300, height=450)
        ptitre=Label(produitFrame1, text="Ensemble matériel", font=("times new roman ", 10, "bold"), bg="cyan", bd=3, relief=RIDGE).pack(side=TOP, fill=X)

        produitFrame2=Frame(produitFrame1,bd=4, relief=RIDGE, bg="white")
        produitFrame2.place(x=5, y=40, width=280, height=150)
        

        lbl_recherche=Label(produitFrame2, text="Recherche materiel | nom", font=("goudy old style", 10, "bold"), bg="lightgreen", bd=3, relief=RIDGE).place(x=2, y=10)

        lbl_nom=Label(produitFrame2, text="Nom matériel",  font=("goudy old style", 10, "bold"), bg="white").place(x=2, y=50)

        txt_recherche= Entry(produitFrame2, textvariable=self.var_recherche,  font=("times new roman", 10), bg="lightyellow").place(x=90, y=50, width=100)

        recherche_btn=Button(produitFrame2, text="Recherche", command=self.recherche, font=("times new roman", 10), bg="blue", cursor="hand2").place(x=200, y=9, height=25)

        tous_btn=Button(produitFrame2, text="Tous", font=("times new roman", 10), bg="lightgray", cursor="hand2").place(x=200, y=48, height=25)



   
        produitFrame3=Frame(produitFrame1, bd=3, relief=RIDGE)
        produitFrame3.place(x=2, y=180, height=230, width=295)

        scroll_y= Scrollbar(produitFrame3, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)


        scroll_x= Scrollbar(produitFrame3, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        #le produit remplace la matiere dans notre cas
        self.produit_table = ttk.Treeview(produitFrame3, columns=("pid", "nom", "quantite", "prix",  "status", "categorie", "fournisseur" ), yscrollcommand=scroll_y.set, xscrollcommand=scroll_y.set)

        scroll_x.config(command=self.produit_table.xview)
        scroll_y.config(command=self.produit_table.yview)
        
        self.produit_table.heading("pid", text="ID", anchor="w")
        self.produit_table.heading("nom", text="nom", anchor="w")
        self.produit_table.heading("quantite", text="quantite", anchor="w") 
        self.produit_table.heading("prix", text="prix", anchor="w") 
        self.produit_table.heading("status", text="status", anchor="w")
        self.produit_table.heading("categorie", text="categorie", anchor="w")
        self.produit_table.heading("fournisseur", text="fournisseur", anchor="w")
        self.produit_table["show"]="headings"
        self.produit_table.pack(fill= BOTH, expand=1)


        self.produit_table.bind("<ButtonRelease-1>", self.get_donne)


        lbl_note=Label(produitFrame1, text="Note: Entrer 0 Qantité pour retirer le matériel du stock", anchor="w", font=("time new roman", 8), bg="white", fg="red").pack(side=BOTTOM, fill=X)

        # Frame Client est ouvrier
        self.afficher()
        client_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="white")
        client_Frame.place(x=320,y=70, width=400, height=140)

        titre=Label(client_Frame, text="Detail ouvriel", font=("goudy old style ", 10), relief=RIDGE, bg="gold").pack(side=TOP, fill=X)


        lbl_nom=Label(client_Frame, text=" Nom", font=("goudy old style ", 10), bg="white").place(x=10, y=25)
        txt_nom=Entry(client_Frame, textvariable=self.var_cname,font=("goudy old style", 10), bg="lightyellow").place(x=110, y=25, width=150)

        #lbl_contact c est le programme
        lbl_nom=Label(client_Frame, text=" Programme", font=("goudy old style ", 10), bg="white").place(x=15, y=50)
        txt_nom=Entry(client_Frame, font=("goudy old style", 10), bg="lightyellow").place(x=110, y=50, width=150)
        
        lbl_type=Label(client_Frame, text=" Nature", font=("goudy old style ", 10), bg="white").place(x=15, y=80)
        txt_type=Entry(client_Frame, font=("goudy old style", 10), bg="lightyellow").place(x=110, y=80, width=150)

        #ajout du lot
        lbl_lot=Label(client_Frame, text=" Lot", font=("goudy old style ", 10), bg="white").place(x=15, y=110)
        txt_lot=Entry(client_Frame, font=("goudy old style", 10), bg="lightyellow").place(x=110, y=110, width=150)


        #
        #calculatrice
        #self.var_cal_input=StringVar()
        calcul_cart_Frame =Frame(self.root, bd=4, relief=RIDGE, bg="white")
        calcul_cart_Frame.place(x=320, y=210, width=400, height=230)



   
        cart_Frame=Frame(calcul_cart_Frame, bd=3, relief=RIDGE)
        cart_Frame.place(x=2, y=2, height=220, width=400)
       
        self.ctitle=Label(cart_Frame, text="Materiel \t Total stock : [0]", font=("goudy old style", 10), bg="gold")
        self.ctitle.pack(side=TOP, fill=X)


        scroll_y= Scrollbar(cart_Frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)


        scroll_x= Scrollbar(cart_Frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        #le produit remplace la matiere dans notre cas
        self.cartTable = ttk.Treeview(cart_Frame, columns=("pid", "nom",  "quantite", "prix",  "status", "categorie", "fournisseur"  ), yscrollcommand=scroll_y.set, xscrollcommand=scroll_y.set)

        scroll_x.config(command=self.cartTable.xview)
        scroll_y.config(command=self.cartTable.yview)
        
        self.cartTable.heading("pid", text="ID", anchor="w")
        self.cartTable.heading("nom", text="nom", anchor="w")
        self.cartTable.heading("quantite", text="quantite", anchor="w")
        self.cartTable.heading("prix", text="prix", anchor="w") 
        self.cartTable.heading("status", text="status", anchor="w")
        self.cartTable.heading("categorie", text="categorie", anchor="w")
        self.cartTable.heading("fournisseur", text="fournisseur", anchor="w")
                  
        self.cartTable["show"]="headings"
        self.cartTable.pack(fill= BOTH, expand=1)
        self.produit_table.bind("<ButtonRelease-1>", self.get_donne_cart)

        #declaration  de la fonction afficher
        self.afficher()

        self.var_id=StringVar()
        self.var_pname=StringVar()
        self.var_quantite=StringVar()
        self.var_prix=StringVar()
        self.var_status=StringVar()
        
        #self.lbl_p_var_stock=StringVar()
        self.var_stock=StringVar()


        Button_Frame=Frame(self.root, bd=6, relief=RIDGE, bg="white")
        Button_Frame.place(x=320, y=440, width=400, height=95)

        lbl_p_nom=Label(Button_Frame, text="nom materiel", font=("goudy old style ", 10), bg="white").place(x=5, y=0)
        txt_p_nom=Entry(Button_Frame, font=("goudy old style", 10), textvariable=self.var_pname, bg="lightyellow", state="r").place(x=5, y=20, width=100)

        lbl_p_prix=Label(Button_Frame, text="prix materiel", font=("goudy old style ", 10), bg="white").place(x=150, y=0)
        txt_p_prix=Entry(Button_Frame, font=("goudy old style", 10), textvariable=self.var_prix, bg="lightyellow", state="r").place(x=150, y=20, width=100) 


        lbl_p_quantite=Label(Button_Frame, text="Quantité", font=("goudy old style ", 10), bg="white").place(x=280, y=0)
        txt_p_quantite=Entry(Button_Frame, font=("goudy old style", 10), textvariable=self.var_quantite, bg="lightyellow").place(x=280, y=20, width=100)   


        self.lbl_p_stock=Label(Button_Frame, text="En stock  [0]", font=("goudy old style ", 10), bg="white")
        self.lbl_p_stock.place(x=5, y=50)


        btn_clean_cart=Button(Button_Frame, command=self.clear_cart, text="Réinitialiser", cursor="hand2", font=("times new roman", 10), bg="lightgray").place(x=150, y=50)
        btn_ajout_cart=Button(Button_Frame, text="Ajouter | Modifier", command=self.ajout_modifier, cursor="hand2", font=("times new roman", 10), bg="darkorange").place(x=280, y=50)

 
        FactureFrame=Frame(self.root, bd=7, relief=RIDGE, bg="white")
        FactureFrame.place(x=725, y=69, height=420, width=350)
        ctitre=Label(FactureFrame, text="Bon de sortie", bg="gold", bd=3, relief=RIDGE, font=("times new roman", 10)).pack(side=TOP, fill=X)


        scroll_y= Scrollbar(FactureFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.txt_espace_facture=Text(FactureFrame, yscrollcommand=scroll_y.set)
        self.txt_espace_facture.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_espace_facture.yview)

        #### button

        FactureMenu=Frame(self.root, bd=4, relief=RIDGE, bg="white")
        FactureMenu.pack(side=RIGHT, fill=Y)

        self.lbl_montant_facture=Label(FactureMenu, text="montant materiel \n [0]", font=("goudy old style", 10), bg="#3f51b5", fg="white", bd=7)
        self.lbl_montant_facture.place(x=20, y=150, width=50)


        FrameBas=Frame(self.root, bd=7, relief=RIDGE, bg="white")
        FrameBas.place(x=725, y=490, height=40, width=350)


        self.imprimer=Button(FrameBas, command=self.imprimer_facture, text="imprimer", font=("goudy old style ", 10), bg="blue").place(x=0, y=0, width=120)
        self.reini=Button(FrameBas, command=self.clear_all, text="renitialiser", font=("goudy old style ", 10), bg="green").place(x=120, y=0, width=120)
        self.gener=Button(FrameBas, text="Générer", command=self.generer_facture, font=("goudy old style ", 10), bg="gray").place(x=230, y=0, width=110)

        ###foncton
    def afficher(self):


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:

            cur.execute("select pid produit, nom, quantite, prix, status,  fournisseur  from produit where status='Actif' ")
            rows=cur.fetchall()
            self.produit_table.delete(*self.produit_table.get_children())
            for row in rows:
                self.produit_table.insert("", END, values=row)


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def recherche(self):

        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            if self.var_recherche.get()=="":
                messagebox.showerror("Erreur", "Saisir le materiel à rechercher")
            else:
                                                            
                cur.execute("select pid produit, nom , quantite,  prix,  status,  fournisseur  from produit from where nom LIKE '%"+self.var_recherche.get()+"%' and  status='Actif'" )
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.produit_table.delete(self.produit_table.get_children())
                    for row in rows:
                        self.produit_table.insert("", END, values=row)

                else:
                    messagebox.showerror("Erreur", "Aucun resultat ")




        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def get_donne(self, ev):


        r = self.produit_table.focus()
        contenu=self.produit_table.item(r)
        row=contenu["values"]
        self.var_id.set(row[0])
        self.var_pname.set(row[1])
       
        self.lbl_p_stock.config(text=f"En stock [{str(row[2])}]")
        self.var_stock.set(row[2])
        
        self.var_prix.set(row[3])
        self.var_quantite.set(1)
        
 





    def get_donne_cart(self, ev):


        r = self.produit_table.focus()
        contenu=self.produit_table.item(r)
        row=contenu["values"]
        self.var_id.set(row[0])
        self.var_pname.set(row[1])
       
        self.lbl_p_stock.config(text=f"En stock [{str(row[2])}]")
        self.var_stock.set(row[2])
        
        self.var_prix.set(row[3])
        self.var_quantite.set(1)
 
    def ajout_modifier(self):
        if self.var_id.get()=="":
            messagebox.showerror("Erreur", "Selectionnez un materiel")
        elif self.var_quantite.get()=="":
            messagebox.showerror("Erreur", "Donnez la quantité")
        elif int(self.var_quantite.get()) > int(self.var_stock.get()):
            messagebox.showerror("Erreur", "la quantité n est pas disponible")

        else:
            prix_cal= self.var_prix.get()
            cart_donne=[self.var_pname.get(), self.var_prix.get(), self.var_quantite.get(), self.var_stock.get()]
            present="nom"
            index = 0
            for row in self.cart_list:
                if self.var_id.get==row[0]:
                    present="oui"
                    break
                index_+=1
            if present=="oui":
                op=messagebox.askyesno("Confirmer", "le produit est deja present\n tu veux vraiment modier | supprimer de la liste")
                if op==True:
                    if self.var_quantite.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        self.cart_list[index_][3]=self.var_quantite.get()
            else:
                self.cart_list.append(cart_donne)
           
        self.afficher_cart()
        self.facture_modifier()

    def afficher_cart(self):

        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")



    def facture_modifier(self):
        self.montant_facture=10
        self.net_payer=0
        self.remise=10
        for row in self.cart_list:
            self.montant_facture= self.montant_facture+(float(row[2])*int(row[3]))
        self.remise = (self.montant_facture * 5)/100
        self.net_payer=self.montant_facture-self.remise
        self.lbl_montant_facture.config(text=f"montant materiel \n [str(self.montant_facture)]")
        #self.lbl_net_payer.config(text=f"net à payer \n [{str(self.net_payer)}] ")
        #self.lbl_remis_facture.config(text=f"net à payer \n [{str(self.remise)}] ")
        self.ctitle.config(text=f"Materiel \t Total stock : [{str(len(self.cart_list))}]")
        
        #generer facture
    def generer_facture(self):
        if self.var_pname.get =="":
            messagebox.showerror("Erreur", "Saisir le nom du client")
        elif len(self.cart_list)==0:
            messagebox.showerror("Erreur", "Ajouter des materiels dans le panier")
        else:
            self.entete_facture()
            self.corp_facture()
            self.footer_facture()

            fp=open(fr"C:\Users\USER\Desktop\sciam_btp\facture\{str(self.var_facture)}.txt", "w")
            fp.write(self.txt_espace_facture.get("1.0", END))
            fp.close
            messagebox.showinfo("Sauvegarder", "Enregistrer/ Générer éffectuer avec succès")
            self.ck_print =1

    def entete_facture(self):
        self.facture= int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%y"))
        #Pour eviter la repetition de la facture
        # doitr etre au niveau de  numero facture  \t\t Date:{str(time.strtime("%d%m%y"))}
        facture_ente= f'''
\tSOCIETE DE CONSTRUCTION IMMOBILIER \n \tET D AMENAGEMENT
BON DE SORTIE DES MATERIEL N... 
{str("="*30)}
Nom gestionnaire stock : {self.var_cname.get()}
Nom du Technicien : {self.var_cname.get()}
tel  Technicien: {self.var_contact.get()}
numero Facture: {str(self.var_pname)}
nom ouvrier: {self.var_cname}
batiment: {self.var_cname}
Travaux à exécuter: {self.var_pname}
Designation  \t Quantité \t retour
{str("="*30)}
        '''  
        self.txt_espace_facture.delete("1.0", END)
        self.txt_espace_facture.insert("1.0", facture_ente)


    def corp_facture(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:

            for row in self.cart_list:
                pi=row[0]
                nom=row[1]
                quantite=int(row[3])-int(row[2])
                if int(row[2])==int(row[3]):
                    status= "Inactif"
                if int(row[2])!=int(row[3]):
                    status="Actif"
                #prix=float(row[2])*float(row[3])
                #prix=str(prix)
                self.txt_espace_facture.insert(END, "\n\t"+nom+"\t"+row[2])
                cur.execute("update produit set ,  quantite=?, status=? where pid=?", (
                   quantite,
                   status,
                   pid
                   
                ))
            #A revoir
                con.commit()
            con.close()
            self.afficher()

        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")
    

    def footer_facture(self):

        facture_footer=f'''
{str("="*30)}
signature de l'ouvrier \t signature \n \t\tresponable techenique signature \n \t\t\t du service logisqtique
{str("="*30)}

        '''
    def clear_cart(self):
        self.var_id.set("")
        self.var_pname.set("")
        self.var_quantite.set("")
        self.var_prix
        self.lbl_p_stock.config("En stock")
        self.var_stock.set("")

    def clear_all(self):
        del self.cart_list[:]
        self.var_pname.set("")
        self.txt_espace_facture.delete("1.0", END)
        self.ctitle.config(text=f"Materiel \t Total stock : [0]")
        self.var_recherche.set("")
        self.ck_print=0
        self.clear_cart()
        self.afficher()
        self.afficher_cart()


    def modifier_heure(self):
        heure_=(time.strftime("%H:%M:%S"))
        date_= (time.strftime("%d-%m-%Y"))
        self.lbl_heure.config(text=f"Bienvenue à SCIAM GESCOM \t\t Date: {str(date_)} \t\t Heure: {str(heure_)}")
        self.lbl_heure.after(200, self.modifier_heure)

    def imprimer_facture(self):
        if self.ck_print==1:

            messagebox.showinfo("imprimer", "veillez patienter pendant l'impresion")
            fichier= tempfile.mktemp(".txt")
            open(fichier, "w").write(self.txt_espace_facture.get("1.0", END))
            os.startfile(fichier, "print")

        else:
            messagebox.showerror("Erreur","Veillez generer la")







    def deconnecter(self):
        self.root.destroy()
        self.obj= os.system("python C:/Users/USER/Desktop/sciam_btp/login.py")

if __name__=="__main__":
            root=Tk()
            caisse(root)
            root.mainloop()