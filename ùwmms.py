import tkinter  as tk 
from tkcalendar import DateEntry # pip install tkcalendar 
my_w = tk.Tk()
my_w.geometry("400x420") # width and height of window   
font1=['Times',56,'normal'] # font style to display output 

l1=tk.Label(my_w,text='data',bg='yellow',font=font1)  # display difference 
l1.grid(row=0,column=0,padx=10,pady=20,columnspan=3,sticky='ew')

cal1=DateEntry(my_w,selectmode='day')
cal1.grid(row=1,column=0,padx=20,pady=30)
cal2=DateEntry(my_w,selectmode='day')
cal2.grid(row=1,column=1,padx=20,pady=30)

b1=tk.Button(my_w,text='Diff in Days', bg='lightgreen',
        font=20,command=lambda:my_upd())
b1.grid(row=1,column=2)
def my_upd(): # triggered on Button Click
    diff_days=(cal2.get_date()-cal1.get_date()).days # difference in days 
    #print(diff_days)
    l1.config(text=str(diff_days)+' days') # read and display date

my_w.mainloop()



#le petit frer de combobox
from tkinter import *

gui = Tk()

liste = Listbox(gui)
liste.insert(1, "Blue")
liste.insert(2, "Red")
liste.insert(3, "Green")
liste.insert(4, "Yellow")
liste.insert(5, "Orange")
liste.insert(6, "Black")

liste.pack()



#WayToLearnX » Python » Interfaces graphiques » Toplevel Tkinter | Python 3

Toplevel Tkinter - Python 3
Interfaces graphiques 
DJI Mini 3 Pro: Waypoint Hyperlapse...

Replay

Unmute
Remaining Time -0:00


Fullscreen
DJI Mini 3 Pro: Waypoint Hyperlapse using only two points
Toplevel Tkinter | Python 3
juillet 1, 2020 Aucun commentaire
Le widget Toplevel fonctionne à peu près comme Frame, mais il est affiché dans une fenêtre différente de niveau supérieur. Ces fenêtres ont généralement des barres de titre, des bordures et d’autres « décorations ».
from tkinter import *

gui = Tk()
w = Toplevel()
w.mainloop()



import tkinter as tk

gui = tk.Tk()
gui.geometry("200x100")

texte = tk.Entry(gui)
texte.insert(0, "Valeur par défaut")
texte.pack(pady=20)

gui.mainloop()

#AfICHHER OU MASQUER

import tkinter as tk

root = tk.Tk()
root.geometry('200x150')  

btn1 = tk.Button(root, text='Afficher', command=lambda: label.pack())       
btn1.pack(pady=20)

btn2 = tk.Button(root, text='Masquer', command=lambda: label.pack_forget())
btn2.pack()

label = tk.Label(root, text = "Welcome to WayToLearnX!")
label.pack()

root.mainloop()





import time
from threading import Thread

def sleeper(i):
    print("Le thread %d est en veille pendant 5 secondes" % i)
    time.sleep(5)
    print("Le thread %d s'est réveillé" % i) 

for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()



#envoie de message

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.connect("smtp.example.com",465)

#Ensuite, connectez-vous au serveur Gmail
server.login("your-email@mail.com", "password")

#Le message à envoyer
msg = "Hello!" 

#Envoyez le mail
server.sendmail("your-email@mail.com", "destination@mail.com", msg)

server.quit()




#recuper la valeur d un bouton radion 


from tkinter import *
 
fenetre=Tk()
  
var_type_trajectoire = IntVar()
 
def afficher():
    valeur_traj = var_type_trajectoire.get()
    print(valeur_traj)
     
choix_lent = Radiobutton(fenetre,text="lent",
                         variable=var_type_trajectoire,value=0,
                         command=afficher)
choix_normal = Radiobutton(fenetre,text="normal",
                           variable=var_type_trajectoire,value=1,
                           command=afficher)
choix_rapide = Radiobutton(fenetre,text="rapide",
                           variable=var_type_trajectoire,value=2,
                           command=afficher)
 
 
choix_lent.place(x=300,y=30)
choix_normal.place(x=300,y=150)
choix_rapide.place(x=300,y=266)
  
fenetre.mainloop()


... ## Tout le code et les widgets..
 
## La boucle tkinter
fenetre.mainloop()
 
## On récupère la valeur, à la fin de la boucle
## Donc, lorsque la fenêtre est détruit.
valeur_traj = var_type_trajectoire.get()
print(valeur_traj)



#un autre exemple de radio
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module qui ce charge de crée la fenêtre récupère les valeur et les renvoie sous forme de graphique
"""
 
from tkinter import *
# from threading import Thread, RLock
import matplotlib.pyplot as plt
 
 
class Display(Frame):
 
 
    def __init__(self, window, **kwargs):
        """
        class en constructeur les widgets
 
        :param window:
        :param kwargs:
        """
 
        Frame.__init__(self, window, bg='yellow')
        self.nb_clic = {'but_in_left': 0, 'but_in_rigth': 0, 'match_win_left': 0, 'match_win_right': 0}
        self.grid(rowspan=14, columnspan=7)
 
        self.title = Label(self, text='PREDICTEUR FOOT', bg='green').grid(row=0, column=2)
 
        self.champ_text1 = StringVar()
        self.champ_text2 = StringVar()
 
        self.champ_team1 = Entry(self, textvariable=self.champ_text1, width=30, bg='white').grid(row=2, column=0)
        self.vs = Label(self, text='VS', bg='yellow').grid(row=2, column=2)
        self.champ_team2 = Entry(self, textvariable=self.champ_text2, width=30, bg='white').grid(row=2, column=5)
 
        self.goal_in_team1 = Label(self, text='Nombre de buts encaissés au cours des 5 derniers match:',
                                   bg='yellow').grid(row=3, column=0)
        self.in_goal_left = Label(self, text='0', bg='yellow').grid(row=5, column=0)
 
        self.goal_in_team2 = Label(self, text='Nombre de buts encaissés au cours des 5 derniers match:',
                                   bg='yellow').grid(row=3, column=5)
        self.in_goal_right = Label(self, text=self.nb_clic['but_in_rigth'], bg='yellow').grid(row=5, column=5)
 
        self.count_less_left = Button(self, text="-", command=self.less_left).grid(row=6, column=0)
        self.count_more_left = Button(self, text="+", command=self.more_left).grid(row=4, column=0)
 
        self.count_more_right = Button(self, text="+", command=self.more_right).grid(row=4, column=5)
        self.count_less_right = Button(self, text="-", command=self.less_right).grid(row=6, column=5)
 
        self.displ_team1 = Label(self, text='Equipe 1').grid(row=8, column=0)
        self.displ_team2 = Label(self, text='Equipe 2').grid(row=8, column=5)
 
    def more_left(self):
        """
        modifier la valeur des boutons
        :return:
        """
        self.nb_clic['but_in_left'] +=1
        self.in_goal_left = Label(self, text=self.nb_clic['but_in_left'], bg='yellow').grid(row=5, column=0)
 
    def more_right(self):
        """
               modifier la valeur des boutons
               :return:
        """
        self.nb_clic['but_in_rigth'] += 1
        print('{}'.format(self.nb_clic['but_in_rigth']))
        self.in_goal_right['text'] = '{}'.format(self.nb_clic['but_in_rigth'])
 
    def less_left(self):
        """
               modifier la valeur des boutons
               :return:
        """
        self.nb_clic['but_in_left'] -= 1
        self.in_goal_left = Label(self, text=self.nb_clic['but_in_left'], bg='yellow').grid(row=5, column=0)
 
    def less_right(self):
        """
            modifier la valeur des boutons
               :return:
        """
        self.nb_clic['but_in_rigth'] -= 1
        self.in_goal_left = Label(self, text=self.nb_clic['but_in_rigth'], bg='yellow').grid(row=5, column=5)
 
    def evidence(probability):
        """
        recupere la somme des resultat pour en sortir le graphique
        :return: le graphique
        """
        abs = list()
        ordn = list()
        nb_resul = 7
 
        for i in probability.keys():
            nb_resul -= 1
            abs.append(i)
            ordn.append(probability[i])
            if nb_resul == 0:
                break
        plt.pie(ordn, labels=abs, autopct=lambda x: str(round(x, 2)) + '%')
        plt.show()