from tkinter import *
from PIL import Image
import datetime
import tkinter as tk
from PIL import Image, ImageTk
import tkinter as tk
import time
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class Dashboard:
	def __init__(self, root):
		self.root =root
		self.root.title("Tableau de bord")
		self.root.geometry("1366x768")
		self.root.config(bg="#eff5f6")

		#icon = PhotoImage(file=r"C:\Users\USER\Desktop\sciam_btp\image\images.jpg")
		#self.root.iconphoto(True, icon)
		
		



		### en tete activebackground = "#808080"
		self.entente = Frame(self.root, bg="#0000FF")
		self.entente.place(x=300, y = 0, width=1070, height=60)

		self.deconnecte = Button(self.root, text="Deconnecter", bg= "#00FF00", font=("time new roman", 13, "bold"), bd = 0, fg = "white", cursor="hand2", activebackground = "#808080" )
		self.deconnecte.place(x=950, y = 15)


		#menucls
		self.FrameMenu=Frame(self.root, bg="#ffffff").place(x=0, y=0, width=300, height=750)
		
		self.logoImage =Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\hyy.png")
		photo = ImageTk.PhotoImage(self.logoImage)
		self.logo=Label(self.FrameMenu, image=photo, bg="#ffffff")
		self.logo.image=photo
		self.logo.place(x=70, y=80)


		self.Nom=Label(self.FrameMenu, text="GESCOM_SCIAM")
		self.Nom.place(x=80, y=80)


		#Tableau de Bord
		
		self.logoImage =Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\dashboard-icon.png")
		photo = ImageTk.PhotoImage(self.logoImage)
		self.dashboard=Label(self.FrameMenu, image=photo, bg="#ffffff")
		self.dashboard.image=photo
		self.dashboard.place(x=35, y=200)

		self.dashboard_text = Button(self.root, text="Tableau de bord", bg= "white", font=("time new roman", 13, "bold"), bd = 0, fg = "black", cursor="hand2", activebackground = "#808080" )
		self.dashboard_text.place(x=80, y = 200)






			#Gestion 
		self.logoImage =Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\manage-icon.png")
		photo = ImageTk.PhotoImage(self.logoImage)
		self.gestion=Label(self.FrameMenu, image=photo, bg="#ffffff")
		self.gestion.image=photo
		self.gestion.place(x=35, y =240)

		self.gestion_text = Button(self.root, text="Gestion", bg= "white", font=("time new roman", 13, "bold"), bd = 0, fg = "black", cursor="hand2", activebackground = "#808080" )
		self.gestion_text.place(x=80, y = 240)





			#Gestion 
		self.logoImage =Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\settings-icon.png")
		photo = ImageTk.PhotoImage(self.logoImage)
		self.parametre=Label(self.FrameMenu, image=photo, bg="#ffffff")
		self.parametre.image=photo
		self.parametre.place(x=35, y =280)

		self.parametre_text = Button(self.root, text="Parametre", bg= "white", font=("time new roman", 13, "bold"), bd = 0, fg = "black", cursor="hand2", activebackground = "#808080" )
		self.parametre_text.place(x=80, y = 280)





		self.logoImage =Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\exit-icon.png")
		photo = ImageTk.PhotoImage(self.logoImage)
		self.quitter=Label(self.FrameMenu, image=photo, bg="#ffffff")
		self.quitter.image=photo
		self.quitter.place(x=30, y =320)

		self.quitter_text = Button(self.root, text="Quitter", bg= "white", font=("time new roman", 13, "bold"), bd = 0, fg = "black", cursor="hand2", activebackground = "#808080" )
		self.quitter_text.place(x=80, y = 332)





		# corps


		self.titre = Label(self.root, text="tableau de bord", font=("time new roman", 13, "bold"), fg="#0064d3", bg="#eff5f6")

		self.titre.place(x=325, y=70)


		#corps 1 

		self.corps1=Frame(self.root, bg="#ffffff").place(x=3280, y =110, heigh = 350, width = 1040 )

		donnee = pd.read_excel(r"C:\Users\USER\Desktop\sciam_btp\classeur.xlsx")

		sunlundi = sum(donnee["lundi"])
		sunmardi = sum(donnee["mardi"])
		sunmercredi = sum(donnee["mercredi"])
		sunjeudi = sum(donnee["jeudi"])
		sunvendredi = sum(donnee["vendredi"])
		sunsamedi = sum(donnee["samedi"])


		fig = plt.figure(figsize=(5,5), dpi=100)
		fig.set_size_inches(5, 3.5)

		labels="lunid", "mardi", "mercredi", "jeudi", "vendredi", "samedi"
		sizes =	[sunlundi, sunmardi, sunmercredi, sunjeudi, sunvendredi, sunsamedi]
		colors=	["yellowgreen", "gold", "lightcoral", "lightskyblue", "cyan", "red"]
		explode=(0.2, 0, 0, 0, 0, 0)

		plt.pie(sizes, explode=explode, labels=labels, colors = colors, autopct='%1.1f%%', shadow=True, startangle=140)
		plt.axis("equal")
		#plt.show()
		canvasbar = FigureCanvasTkAgg(fig, master=self.root)
		canvasbar.draw()
		canvasbar.get_tk_widget().place(x=1120, y=235, anchor=CENTER)


			#diagramme en barre

		#fig=plt.figure(figsize=(5, 3.5), dpi=100)
		#labels="lunid", "mardi", "mercredi", "jeudi", "vendredi", "samedi"
		#labelpos=np.arange(len(labels))
		#seminesum=[sunlundi, sunmardi, sunmercredi, sunjeudi, sunvendredi, sunsamedi]
		#plt.bar(labelpos, seminesum, align='center', alpha=1.0)
		#plt.xticks(labelpos, labels)
		#plt.ylabel("prix")
		#plt.xlabel("semaine")
		#plt.tight_layout(pad=2.2, w_pad=0.5, h_pad=0.1)
		#plt.title("Vente de la semaine")
		#plt.xticks(rotation=30, horizontalalignment="center")
#ya une errerur la..... a revoir demain .... Obido la tcheta 
#je suis vraiment epuisé don a demain ... tchiao

		#for index, dtatapoint in enumerate(seminesum):
		#	plt.text(x=index, y=dtatapoint+0.3, s=f"(dtatapoint)", fondict=dict(fontsize=10), has="center", yah="bottom")
		#canvasbar=FigureCanvasTkAgg(fig, master=self.root)
		#canvasbar.draw()
		#canvasbar.get_tk_widget().place(x=1120, y=285, anchor="center")
		#self.root.protocol("VM_DELETE_WINDOW", self.Exit)

				#corps 2 

		self.corp2 =Frame(self.root, bg="#009aa5").place(x=328, y = 405, width=310, height =220)

		self.totalclientImage = Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\left-icon.png")

		photo = ImageTk.PhotoImage(self.totalclientImage)
		self.totalclient=Label(self.corp2, image=photo, bg="#009aa5")
		self.totalclient.image= photo
		self.totalclient.place(x=555, y=405)

		self.ntotalclient_text = Button(self.root, text="300", bg= "#009aa5", font=("time new roman", 25, "bold"), bd = 0, fg = "white", cursor="hand2", activebackground = "#009aa5" )
		self.ntotalclient_text.place(x=450, y = 540)

		self.ttotalclient_text = Button(self.root, text="Total client", bg= "#009aa5", font=("time new roman", 20, "bold"), bd = 0, fg = "white", cursor="hand2", activebackground = "#009aa5" )
		self.ttotalclient_text.place(x=330, y = 405)

		


		#Corps 3

		self.corp3 =Frame(self.root, bg="red").place(x=700, y = 405, width=310, height =220)

		self.totaldepenseImage = Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\left-icon.png")

		photo = ImageTk.PhotoImage(self.totaldepenseImage)
		self.totaldepense=Label(self.corp3, image=photo, bg="red")
		self.totaldepense.image= photo
		self.totaldepense.place(x=935 , y=405)

		self.ntotaldepense_text = Button(self.root, text="80", bg= "red", font=("time new roman", 25, "bold"), bd = 0, fg = "white", cursor="hand2", activebackground = "#009aa5" )
		self.ntotaldepense_text.place(x=800, y = 550)

		self.ttotaldepense_text = Button(self.root, text="Total depense", bg= "red", font=("time new roman", 20, "bold"), bd = 0, fg = "white", cursor="hand2", activebackground = "#009aa5" )
		self.ttotaldepense_text.place(x=700, y = 405)


 		#Corps 4 #a revoir 

		self.corp4 =Frame(self.root, bg="#009aa5").place(x=1040, y = 405, width=310, height =220)

		self.totaventeImage = Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\left-icon.png")

		photo = ImageTk.PhotoImage(self.totaventeImage)
		self.vente=Label(self.corp4, image=photo, bg="#009aa5")
		self.vente.place(x=1500, y=405)

		self.vente_text = Button(self.root, text="20", bg= "red", font=("time new roman", 25, "bold"), bd = 0, fg = "white", cursor="hand2", activebackground = "#009aa5" )
		self.vente_text.place(x=1500, y = 1000)

		self.ventee_text = Button(self.root, text="Total Vente", bg= "red", font=("time new roman", 20, "bold"), bd = 0, fg = "white", cursor="hand2", activebackground = "#009aa5" )
		self.vente_text.place(x=1200, y = 405)
		#a revoir demain




		#heure



		self.heureImage = Image.open(r"C:\Users\USER\Desktop\sciam_btp\image\left-icon.png")

		photo = ImageTk.PhotoImage(self.totaventeImage)
		self.heure=Label(self.corp4, image=photo, bg="#009aa5")
		self.heure.place(x=1500, y=405)

		self.heure_text=Label(self.FrameMenu).place(x=115, y=15)
		#self.afficher_heure()

		def afficher_heure(self):
			self.time = time.strftime("%H:%M:%S")
			self.date=time.strftime("%d/%M/%Y")
			resultat = f"{self.time}\n{self.date}"
			self.heure_text.config(text=resultat, bd=0, font=("time new roman", 13, "bold"), bg="#ffffff")
			self.heure_text.after(100, self.afficher_heure)



		def Exit(self):
			self.root


if __name__=="__main__":
	root=Tk()
	Dashboard(root)
	root.mainloop()



