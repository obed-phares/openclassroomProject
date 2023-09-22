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


class fournisseur:
    def __init__(self, root):
        self.root =root
        self.root.title("GESCO SCIAM")
        self.root.geometry("1300x1300")
        self.root.config(bg="white")

        self.var_nfacture=StringVar()
        self.var_list_facture=[]

        title = Label(self.root, text="Consulter les differents bons", font=("time new roman", 15), bg="cyan", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=10)
        lbl_N_facture = Label(self.root, text="Numero Facture", font=("time new roman", 13), bg="white").place(x=50, y=60)
        txt_N_facture=Entry(self.root, textvariable=self.var_nfacture, font=("times new roman", 13), bg="lightyellow").place(x=200, y=60, width=200)

        btn_reherche= Button(self.root,  command=self.recherche, text="rechercher", font=("times new roman", 10, "bold"), bg="green", cursor="hand2").place(x=415, y=60)

        btn_reini= Button(self.root, command=self.reini , text="Renitialiser", font=("times new roman", 10, "bold"), bg="lightgray", cursor="hand2").place(x=500, y=60)

        venteFrame=Frame(self.root, bd=3, relief=RIDGE)
        venteFrame.place(x=10, y=110, height=420, width=300)

        scroll_y= Scrollbar(venteFrame, orient=VERTICAL)
        
        self.list_vente=Listbox(venteFrame, font=("times new roman ", 13), bg="white", yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_y.config(command=self.list_vente.yview)
        self.list_vente.pack(fill=BOTH, expand=1)
        self.list_vente.bind("<ButtonRelease-1>", self.recuperDonne)

        #### espace facture
        FactureFrame=Frame(self.root, bd=3, relief=RIDGE)
        FactureFrame.place(x=350, y=110, height=420, width=300)

        title=Label(FactureFrame, text="Bon de sortie", font=("goudy old style", 15, "bold"), bg="orange").pack(side=TOP, fill=X)
        scroll_y2=Scrollbar(FactureFrame, orient=VERTICAL)
        self.espaceFacture=Text(FactureFrame, font=("goudy old style", 9), bg="lightyellow", yscrollcommand=scroll_y2.set)
        scroll_y2.pack(side=RIGHT, fill=Y)
        scroll_y2.config(command=self.espaceFacture.yview)
        self.espaceFacture.pack(fill=BOTH, expand=1)


        self.afficher()

    def afficher(self):
        del self.var_list_facture[:]
        self.list_vente.delete(0, END)
        for  i in os.listdir(r"C:\Users\USER\Desktop\sciam_btp\facture"):
            if i.split(".")[-1]=="txt":
                self.list_vente.insert(END, i)
                self.var_list_facture.append(i.split(".")[0])
                
    def recuperDonne(self, ev):
        index_=self.list_vente.curselection()
        nom_fichier= self.list_vente.get(index_)
        fichier_ouvert =open(fr"C:\Users\USER\Desktop\sciam_btp\facture\{nom_fichier}", "r")
        self.espaceFacture.delete("1.0", END)
        for i in fichier_ouvert:
            self.espaceFacture.insert(END, i)
        fichier_ouvert.close()

    def recherche(self):
        if self.var_nfacture.get()=="":
            messagebox.showerror("Erreur", "Donnez un numero de facture")
        else:
            if self.var_nfacture.get() in self.var_list_facture:
                #seulement les fichiers qui contiennent les numero de facture pourront etre ouvert
                fichier_ouvert =open(fr"C:\Users\USER\Desktop\sciam_btp\facture\{self.var_nfacture.get()}.txt", "r")
                self.espaceFacture.delete("1.0", END)
                for i in fichier_ouvert:
                    self.espaceFacture.insert(END, i)
                    fichier_ouvert.close()
            else:
                messagebox.showerror("Erreur", "Numerode facture invalide" )

    def reini(self):

        self.afficher()
        self.espaceFacture.delete("1.0", END)
        self.var_nfacture.set("")



if __name__=="__main__":
            root=Tk()
            fournisseur(root)
            root.mainloop()