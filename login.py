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
import os
import smtplib
#import email_password




class caisse:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("1500x1500")
        self.root.config(bg="white")
        self.root.focus_force()


        self.code_envoie=""

        login_frame = Frame(self.root, bg="cyan")
        login_frame.place(x=300, y=100, width=400, height=400)
        title= Label(login_frame, text="Connexion", font=("Algerian", 40, "bold"), bg="cyan", fg="black").pack(side=TOP, fill=X)

        lbl_id= Label(login_frame, text="ID Employé", font=("times new roman", 15), bg="cyan").place(x=150, y=100)
        lbl_id= Label(login_frame, text=" Mot de passe", font=("times new roman", 15), bg="cyan").place(x=150, y=200)

        self.txt_id_employe = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_id_employe.place(x=100, y=130)

        self.txt_password = Entry(login_frame, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=100, y=240)

        connecter_btn=Button(login_frame, text="Connexion",command=self.connexion , cursor="hand2", font=("times new roman ", 15, "bold"), bg="lightgray", fg="green").place(x=150, y=280)
        oublie__btn=Button(login_frame, text="mot de passe oublié",command=self.password_oublie_fenetre ,cursor="hand2", font=("times new roman ", 9), bg="cyan", fg="red").place(x=150, y=350)
    
    

    def password_oublie_fenetre(self):
        if self.txt_id_employe.get()=="":
            messagebox.showerror("Erreur", "Veillez saisir votre ID EMployé")
        else:
            con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
            cur=con.cursor()

        try:
            cur.execute("select email from employe where eid=?", (self.txt_id_employe(), ))
            email= cur.fetchone()
            if email==None:
                messagebox.showerror("Erreur", "l'ID Employé est invalide")
            else:
                chk=self.envoie_mail(email[0])
                if chk =="f":

                    messagebox.showerror("Erreur", "Veillez verifier votre connexion")
                else:
                    self.var_code = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_conf_pass = StringVar()

                    self.root2=Toplevel()
                    self.root2.title("Renitialiser mot de passe")
                    self.root2.config(bg="white")
                    self.root2.geometry("400x400+800+500")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    title = Label(self.root2, text="Mot de passe oublé", font=("Algerian", 15, "bold"), bg="red").pack(side=TOP, fill=X)
                    ##code
                    aff_code= Label(self.root2, text="saisir le code reçu par mail", font=("times new roman", 10, "bold")).place(x=70, y=50)
                    txt=reset= Entry(self.root2, textvariable=var_code, font=("times new roman", 10), bg="lightgray").place(x=70, y=100, width=200)
                    self.code_btn= Button(self.root2, command= self.code_valide, text="Valider", cursor="hand2", font=("times new roman", 10, "bold"), bg="lightgray", fg="green")
                    self.code_btn.place(x=300, y=90)

                    #### pour le nouveau mot de pass
                    nouveau_password=Label(self.root2, text="Nouveau mot de passe", font=("times new roman", 10, "bold"), bg="white").place(x=70, y=150)
                    txt_nex_pass=Entry(self.root2, font=("times new roman", 10), textvariable=self.var_new_pass, bg="lightgray").place(x=70, y=200, width=250)

                    #### pour le confirmer mot de pass
                    confirm_password=Label(self.root2, text="confirme mot de passe", font=("times new roman", 10, "bold"), bg="white").place(x=70, y=250)
                    txt_confirm_pass=Entry(self.root2, font=("times new roman", 10), textvariable=self.var_new_pass, bg="lightgray").place(x=70, y=300, width=250)

                    #### modifier le mot de passe
                    self.changer_btn = Button(self.root2,  text="Modifier", cursor="hand2",state="r", command=self.modifier, font=("times new roman", 10, "bold"), bg="gray")
                    self.changer_btn.place(x=160, y=360)


        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def modifier(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Erreur", "Veillez saisirvotre mot de passe.")
        elif self.var_new_pass.get()!= self.var_conf_pass.get():
            messagebox.showerror("Erreur", "le nouveau mot de passe et le confirme de mot de passe doivent être identique ")
        else:
            try:
                con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
                cur=con.cursor()
                cur.execute("update set password=? were eid=?", (self.var_new_pass.get(), self.text_id_employe.get(),))
                con.commit()
                messagebox.showinfo("Succès", "Mot de passe mofifié avec succès")
                self.root2.destroy()


            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")
        


    def code_valide(self):
        if int(self.code_envoie)==int(self.var_code.get()):
            self.changer_btn.config(state=NORMAL)
            self.code_btn.config(state=DISABLED)
        else:

            messagebox.showerror("Erreur", "le code entré est invalide. Entrez le bon code")

    def connexion(self):
        con=sqlite3.connect(database=r"C:\Users\USER\Desktop\sciam_btp\donnee\sciamdatabase.db")
        cur=con.cursor()
        try:
            if self.txt_id_employe.get() =="" or self.txt_password.get()=="":
                messagebox.showerror("Erreur", "Veillez donnez votre Id Employé et votre mot de passe ")
            else:
                cur.execute("select type from employe where eid = ? AND password=?", (self.txt_id_employe.get(), self.txt_password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Erreur", "l'ID Employé ou mot de passe n'existe pas")
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python C:/Users/USER/Desktop/sciam_btp/admin/index.py")
                    else:
                        self.root.destroy()
                        os.system("python C:/Users/USER/Desktop/sciam_btp/caisse.py")

        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")
    


    def envoie_mail():
        s =smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        email_=email_password.email_
        pass_=email_password.pass_

        s.login(email_, pass_)

        #permettre a ce que le code ne se repète pas deux fois. donc on faire un plus a la seconde

        self.code_envoie=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        subj="GESCOM code de renitialisation"
        msg=f"Bonjour Monsieur/Madame\n\n Votre code de reinitialisation est : {self.code_envoie}\n Merci d avoir utiliser notre service" 
        msg="subject: {}\n\n".format(subj, msg)
        s.sendmail(email_, to_, msg)
        chk=s.ehlo()
        if chk [0]==250:
            return 's'
        else:
            return 'f'

if __name__=="__main__":
            root=Tk()
            caisse(root)
            root.mainloop()