#importation du module tkinter pour l'interface graphique
import tkinter as tk
from tkinter import messagebox

from datetime import datetime
#cette module importée nous permettra de bien manipuler la notion de date et aussi de prendre en compte les années bisextiles

#fonction de conversion
def convertir_date():
    
    #récuperer la date entree par l'utilisateur
    date_entree = entry_date.get()

    try:
        #Essayer de convertir la date en objet datetime
        date_obj = datetime.strptime(date_entree, "%Y-%m-%d")

        #Reformater la date en JJ/MM/AAA
        date_convertie = date_obj.strftime("%d/%m/%Y")

        #afficher le résultat
        label_resultat.config(text=f"Date convertie : {date_convertie}")
    
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une date au format AAAA-MM-JJ ou une date valide ! ")

#Création de la fenetre tkinter
root = tk.Tk()
root.title("Converson de date")

#Dimention de la fenetre
root.geometry("1000x500")


#ajout du champ d'entrée pour la date
label_instruction = tk.Label(root, text="Entrez la date au format AAAA-MM-JJ :", fg='white', bg='black')
label_instruction.pack()
#l'emplacement de l'instruction
label_instruction.place(x=350, y=200)

entry_date = tk.Entry(root)
entry_date.pack()
#l'emplacement du champ d'entree
entry_date.place(x=350, y=250)

#Bouton de conversion
buton_convertir = tk.Button(root, text="Convertir", fg='black', bg='blue', width=50, height=1, command=convertir_date)
buton_convertir.pack()
#l'emplacement du bouton
buton_convertir.place(x=350, y=300)


#afficher le résultat
label_resultat = tk.Label(root, text="", fg='white', bg='black')
label_resultat.pack()
#l'emplacement du resultat
label_resultat.place(x=350, y=350)

#Lancer l'interface graphique
root.mainloop()