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