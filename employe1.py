from tkinter import *
from PIL import Image
import datetime
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sqlite3

from tkinter import filedialog
import shutil
import os



class index:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("1500x1500")
        self.root.config(bg="white")
        self.root.focus_force()


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS employe(eid text PRIMARY KEY, nom text, prenom text,  sexe text, situation text, fonction text , experience text, formation text ,  poste text, salaire text, email text,  type text, contact text,  adhesion text,  password text)")
        con.commit()

        # Créer la base de données et la table si ce n'est pas déjà fait
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS fichiers(id INTEGER PRIMARY KEY, nom BLOB, chemin TEXT)")
        con.commit()

        # Créer le répertoire de stockage si ce n'est pas déjà fait
        if not os.path.exists("stockage_fichiers"):
            os.makedirs("stockage_fichiers")




        # variable
        self.var_recherche_tye =StringVar()
        self.var_recherche_text =StringVar()
        self.var_emplo_id =StringVar()
        self.var_nom =StringVar()
        self.var_prenom = StringVar()
        self.var_sexe =StringVar()
        self.var_situation=StringVar()
        self.var_fonction= StringVar()
        self.var_experience=StringVar()
        self.var_formation=StringVar()
        self.var_poste= StringVar()
        self.var_salaire =StringVar()
        self.var_email =StringVar()
        self.var_type =StringVar()
        self.var_contact =StringVar()
        self.var_adhesion =StringVar()
        self.var_password =StringVar()
        
        





        self.droite = LabelFrame(self.root, font=("goudy old style", 10, "bold"), bd=2, relief =RIDGE, bg="white")
        self.droite.place(x=800, y=130, width=280, height=300)



        titre =Label(self.droite, text="Pièce jointe", font=("time new roman", 10),  bg="cyan", justify=CENTER).place(x=0, y=0, width=280)


            #Listebox pour afficher les fichiers
        #liste_fichiers = tk.Listbox(self.droite, bd=3, relief=RIDGE)
        #liste_fichiers.place(x=2, y=150, width= 250, height= 100)



        # Bouton pour les fichier jointe
        bouton_afficher = tk.Button(self.droite, text="Pièce jointe", font=("goudy old style", 12), command=self.televerser_fichier)
        bouton_afficher.place(x= 30, y= 50)
        

        # Bouton pour afficher les fichier
        #bouton_afficher = tk.Button(self.droite, text="Afficher", font=("goudy old style", 12), command=self.afficher_fichiers)
        #bouton_afficher.place(x= 30, y= 100)
        






        #frame recherche
        reche_Frame = LabelFrame(self.root, font=("goudy old style", 10, "bold"), bd=2, relief =RIDGE, bg="white")
        reche_Frame.place(x=300, y=10, width=550, height=60)

        reche_option=ttk.Combobox(reche_Frame, textvariable=self.var_recherche_tye,values=("nom", "prenom"), font=("time new roman", 10), state="r", justify=CENTER)
        reche_option.set("selection")
        reche_option.place(x=10, y=10, width=200)


        reche_text=Entry(reche_Frame, textvariable=self.var_recherche_text,font=("time new roman", 10), bg="lightyellow").place(x=235, y=10, width=200)

        recherche=Button(reche_Frame,  text="Recherche", font=("times new roman", 10), cursor="hand2", fg="white", bg="blue" )
        recherche.place(x=450, y=2, height=30)


        # titre
        titre =Label(self.root, text="formulaire employé", font=("time new roman", 15),  bg="cyan", justify=CENTER).place(x=0, y=80, width=1200)
        
        # ligne
        self.lbl_empid = Label(self.root, text="ID employé", font=("time new roman", 10), bg="white").place(x=150, y=110)
        self.txt_empid=Entry(self.root,textvariable=self.var_emplo_id, font=("time new roman", 10), bg="lightyellow").place(x=150, y=130, width=180)

        lbl_nom = Label(self.root, text="Nom et prenom", font=("time new roman", 10), bg="white").place(x=370, y=110)
        lbl_nom=Entry(self.root,textvariable =self.var_nom , font=("time new roman", 10), bg="lightyellow").place(x=350, y=130, width=210)

        lbl_Prenom=Entry(self.root,textvariable =self.var_prenom , font=("time new roman", 10), bg="lightyellow").place(x=580, y=130, width=210)


        #lbl_contact = Label(self.root, text="Contact", font=("time new roman", 10), bg="white").place(x=800, y=110, width=100)
        #lbl_contact=Entry(self.root,textvariable= self.var_contact , font=("time new roman", 10), bg="lightyellow").place(x=900, y=120, width=150)

        #deuxieme ligne

        lbl_sexe = Label(self.root, text="sexe", font=("time new roman", 10), bg="white").place(x=150, y=160)

        txt_sexe=ttk.Combobox(self.root, textvariable=self.var_sexe, values=("homme", "femme"),font=("time new roman", 10),  state ="r", justify=CENTER)
        txt_sexe.set("selection")
        txt_sexe.place(x=150, y=180, width=180)




        lbl_situation = Label(self.root, text="Situation matrimoniale", font=("time new roman", 10), bg="white").place(x=350, y=160)

        txt_situation=Entry(self.root,textvariable=self.var_situation , font=("time new roman", 10), bg="lightyellow").place(x=350, y=180, width=210)


        lbl_fonction = Label(self.root, text="Fonction", font=("time new roman", 10), bg="white").place(x=580, y=160 )

        txt_fonction=Entry(self.root,textvariable=self.var_fonction, font=("time new roman", 10), bg="lightyellow").place(x=580, y=180, width=200)




        #troisieme demande ligne

        lbl_Experience = Label(self.root, text="Expérience Professionnelle", font=("time new roman", 10), bg="white").place(x=150, y=210)
        txt_Experience=Entry(self.root, textvariable=self.var_experience,font=("time new roman", 10), bg="lightyellow").place(x=150, y=230, width=180)

        lbl_formation = Label(self.root, text="Formation", font=("time new roman", 10), bg="white").place(x=350 , y=210)
        txt_formation=Entry(self.root, textvariable=self.var_formation ,font=("time new roman", 10), bg="lightyellow").place(x=350, y=230, width=200)


        lbl_poste = Label(self.root, text="Poste prévu", font=("time new roman", 10), bg="white").place(x=580 , y=210)
        txt_poste=Entry(self.root, textvariable=self.var_poste ,font=("time new roman", 10), bg="lightyellow").place(x=580, y=230, width=200)



        # quatrieme ligne
        lbl_salaire = Label(self.root, text="salaire", font=("time new roman", 10), bg="white").place(x=150, y=260)
        txt_salaire=Entry(self.root,textvariable= self.var_salaire,font=("time new roman", 10), bg="lightyellow").place(x=150, y=280, width=180)

        #show="*" , permet de masquer le mot de passe


        lbl_email = Label(self.root, text="E-mail", font=("time new roman", 10), bg="white").place(x=350, y=260)
        txt_email=Entry(self.root, textvariable= self.var_email, font=("time new roman", 10), bg="lightyellow").place(x=350, y=280, width=200)

        lbl_type = Label(self.root, text="Type", font=("time new roman", 10), bg="white").place(x=580, y=260 )

        txt_type=ttk.Combobox(self.root, textvariable=self.var_type,values=("Admin", "sécretaire", "stock"),font=("time new roman", 10),  state ="r", justify=CENTER)
        txt_type.set("selection")
        txt_type.place(x=580, y=280, width=200)


        #txt_naissance=Entry(self.root,textvariable=self.var_naissance , font=("time new roman", 10), bg="lightyellow").place(x=500, y=190, width=150)

        #lbl_naissance = Label(self.root, text="Date de naissance", font=("time new roman", 10), bg="white").place(x=350, y=190)

        #Cinquime ligne
        lbl_contact = Label(self.root, text="Contat", font=("time new roman", 10), bg="white").place(x=150 , y=310)
        txt_contact=Entry(self.root, textvariable=self.var_contact ,font=("time new roman", 10), bg="lightyellow").place(x=150, y=330, width=180)


        lbl_adhesion = Label(self.root, text="Date de service", font=("time new roman", 10), bg="white").place(x=350 , y=310)
        txt_adhesion=Entry(self.root, textvariable=self.var_adhesion ,font=("time new roman", 10), bg="lightyellow").place(x=350, y=330, width=200)



        lbl_password = Label(self.root, text="Mot de passe", font=("time new roman", 10), bg="white").place(x=580, y=310)
        txt_password=Entry(self.root,textvariable= self.var_password,font=("time new roman", 10), bg="lightyellow").place(x=580, y=330, width=180)




        self.ajout_btn=Button(self.root, command=self.ajouter , state="normal", text="Ajouter", font=("times new roman", 10, "bold"), cursor="hand2", bg="green")
        self.ajout_btn.place(x=270, y=380, height=25)

        self.modifier_btn=Button(self.root, command=self.modifier, text="modifier", state ="disable", font=("times new roman", 10, "bold"), cursor="hand2", bg="yellow")
        self.modifier_btn.place(x=370, y=380, height=25)

        self.supprimer_btn=Button(self.root,command=self.supprimer ,text="supprimer", state="disable",font=("times new roman", 10, "bold"), cursor="hand2", bg="red")
        self.supprimer_btn.place(x=470, y=380, height=25)

        self.reni_btn=Button(self.root, text="renitialiser",command=self.reini, font=("times new roman", 10, "bold"), cursor="hand2", bg="lightgray")
        self.reni_btn.place(x=570, y=380, height=25)

 




        #liste employé
        listeFrame=Frame(self.root, bd=3, relief=RIDGE)
        listeFrame.place(x=0, y=420, height=110, relwidth=1)

        scroll_y= Scrollbar(listeFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)


        scroll_x= Scrollbar(listeFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.employelste= ttk.Treeview(listeFrame, columns = ("eid", "nom", "prenom",  "sexe", "situation", "fonction" , "experience", "formation" ,  "poste", "salaire", "email",  "type", "contact",  "adhesion", "Password"), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.config(command=self.employelste.xview)
        scroll_y.config(command=self.employelste.yview)    
        
        self.employelste.heading("eid", text="ID")
        self.employelste.heading("nom", text="nom")
        self.employelste.heading("prenom", text="prenom")
        self.employelste.heading("sexe", text="sexe")
        self.employelste.heading("situation", text="situation")
        self.employelste.heading("fonction", text="fonction")
        self.employelste.heading("experience", text="experience")
        self.employelste.heading("formation", text="formation")
        self.employelste.heading("poste", text="poste")
        self.employelste.heading("salaire", text="salire")
        self.employelste.heading("email", text="E-mail")
        self.employelste.heading("type", text="type")
        self.employelste.heading("contact", text="contact")
        self.employelste.heading("adhesion", text="adhesion")
        self.employelste.heading("Password", text="Password")

        self.employelste["show"]="headings"


        self.employelste.bind("<ButtonRelease-1>", self.get_donne)


        self.employelste.pack(fill=BOTH, expand=1)

        self.afficher()
        #fonction 

    #def recherche(self):
     #   con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
      #  cur=con.cursor()

       # try:

        #    if self.var_recherche_text.get()=="":
         #       messagebox.showerror("Erreur", "veillez saisir dans le champ de recherche")
          #  else:
           #     cur.execute("select * from employe where"+self.var_recherche_tye.get()+"LIKE '%"+self.var_recherche_text.get()+"%'")
            #    rows=cur.fetchall()
             #   if len(rows)!=0:
              #      self.employelste.delete(*self.employelste.get_children())
               #     for row in rows:
                #        self.employelste.insert("", END, values=row)
                 #   else:
                  #      messagebox.showerror("Erreur", "aucun resultat trouvé")
        #except Exception as ex:
         #     messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")



              

    def get_donne(self, ev):

        self.ajout_btn.config(state="disable")
        self.modifier_btn.config(state="normal")
        self.supprimer_btn.config(state="normal")
        #self.txt_empid.config(state="readonly")
        r = self.employelste.focus()
        contenu=self.employelste.item(r)
        row=contenu["values"]

        self.var_emplo_id.set(row[0])
        self.var_nom.set(row[1])
        self.var_prenom.set(row[2])
        self.var_sexe.set(row[3])
        self.var_situation.set(row[4])
        self.var_fonction.set(row[5])
        self.var_experience.set(row[6])
        self.var_formation.set(row[7])
        self.var_poste.set(row[8])
        self.var_salaire.set(row[9])
        self.var_email.set(row[10])
        self.var_type.set(row[11])
        self.var_contact.set(row[12])
        self.var_adhesion.set(row[13])
        self.var_password.set(row[14])


    def reini(self):
        #self.txt_empid.config(state="normal")
        self.ajout_btn.config(state="normal")
        self.modifier_btn.config(state="disable")
        self.supprimer_btn.config(state="disable")
        self.var_emplo_id.set("")
        self.var_nom.set("")
        self.var_prenom.set("")
        self.var_sexe.set("Homme")
        self.var_situation.set("")
        self.var_fonction.set("")
        self.var_experience.set("")
        self.var_formation.set("")
        self.var_poste.set("")
        self.var_salaire.set("")
        self.var_email.set("")
        self.var_type.set("Admin")
        self.var_contact.set("")
        self.var_adhesion.set("")
        self.var_password.set("")

        self.var_recherche_text.set("")
        self.var_recherche_tye.set("nom")


    def supprimer(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()

        try:
            op=messagebox.askyesno("Confirmer", "voulez-vous vraiment supprimer")
            if op==True:
                cur.execute("delete from employe where eid=?", (self.var_emplo_id.get(),))
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
            cur.execute("update employe set  nom=?, prenom=?,  sexe=?, situation=?, fonction=? , experience=?, formation=? ,  poste=?, salaire=?, email=?,  type=?, contact=?,  adhesion =?, Password =? where eid=?", (


                        
                        self.var_nom.get(),
                        self.var_prenom.get(),
                        self.var_sexe.get(),
                        self.var_situation.get(),
                        self.var_fonction.get(),
                        self.var_experience.get(),
                        self.var_formation.get(),
                        self.var_poste.get(),
                        self.var_salaire.get(),
                        self.var_email.get(),
                        self.var_type.get(),
                        self.var_contact.get(),
                        self.var_adhesion.get(),
                        self.var_password.get(), 
                        self.var_emplo_id.get()


            ))
            con.commit()
            self.afficher()
            self.reini()
            messagebox.showinfo("Succès", "modification effectué avec succès")
        except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")
               

    def afficher(self):


        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:

            cur.execute("select * from employe")
            rows=cur.fetchall()
            self.employelste.delete(*self.employelste.get_children())
            for row in rows:
                self.employelste.insert("", END, values=row)


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")



    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()

        try:
            if self.var_emplo_id.get()=="":
                messagebox.showerror("Erreur", "veillez mettre un id")
            else:
                cur.execute("select * from employe where eid=?", (self.var_emplo_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "l'ID employé existe deja")
                else:
                    cur.execute("insert into employe (eid, nom, prenom,  sexe, situation, fonction , experience, formation ,  poste, salaire, email,  type, contact,  adhesion, Password) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (

                        self.var_emplo_id.get(),
                        self.var_nom.get(),
                        self.var_prenom.get(),
                        self.var_sexe.get(),
                        self.var_situation.get(),
                        self.var_fonction.get(),
                        self.var_experience.get(),
                        self.var_formation.get(),
                        self.var_poste.get(),
                        self.var_salaire.get(),
                        self.var_email.get(),
                        self.var_type.get(),
                        self.var_contact.get(),
                        self.var_adhesion.get(),
                        self.var_password.get()
                        


                    ))
                    con.commit()
                    self.afficher()
                    self.reini()
                    messagebox.showinfo("Succès", "Ajout effectué avec succès")





        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")


            # Fonction pour téléverser un fichier
    def televerser_fichier(self):
        # Ouvrir une boîte de dialogue de sélection de fichier
        fichier = filedialog.askopenfilename(filetypes=[("Fichiers", "*.*")])
    
        # Si un fichier est sélectionné
        if fichier:
            # Copier le fichier vers le répertoire de stockage (ici, nommé "stockage_fichiers")
            destination = os.path.join("stockage_fichiers", os.path.basename(fichier))
            shutil.copy(fichier, destination)
    
            # Insérer les informations du fichier dans la base de données
            con = sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
            cur = con.cursor()
            cur.execute("INSERT INTO fichiers (nom, chemin) VALUES (?, ?)",(os.path.basename(fichier), destination))
            con.commit()
            con.close()
    
            # Mettre à jour l'affichage des fichiers
            #self.afficher_fichiers()


    # Fonction pour afficher les fichiers
    #def afficher_fichiers(self):
        # Effacer le contenu de la liste
    #    liste_fichiers.delete(0, tk.END)
    
      #  # Récupérer les informations des fichiers depuis la base de données
     #   con = sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
    #    cur = con.cursor()
   #     cur.execute("SELECT * FROM fichiers")
  #      fichiers = c.fetchall()
 #       con.close()
#
#        # Ajouter les fichiers à la liste
#        for fichier in fichiers:
#            liste_fichiers.insert(tk.END, fichier[1])  # Utilisez le bon index pour le nom du fichier



if __name__=="__main__":
            root=Tk()
            index(root)
            root.mainloop()