import customtkinter as ctk
from tkinter import Tk, Menu
from tkinter import PhotoImage, messagebox

# Fonction pour traiter les informations du formulaire
def submit_form():
    identifiant = id_entry.get()
    mot_de_passe = password_entry.get()
    
    # Par exemple, afficher une boîte de message avec les informations saisies
    if identifiant and mot_de_passe:
        messagebox.showinfo("Informations soumises", f"Identifiant: {identifiant}\nMot de passe: {mot_de_passe}")
    else:
        messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")

# Créer la fenêtre principale
window = ctk.CTk()
window.title("Faro")
window.geometry("720x420")
window.iconbitmap("Karmine_Corp_logo.svg.ico")
window.config(bg="#fefffb")

# Créer la frame principale (cette frame va se redimensionner et occuper tout l'espace)
frame = ctk.CTkFrame(window, fg_color="#fefffb")
frame.pack(expand=True)  # Rempli tout l'espace disponible et s'agrandit

# Création de l'image
width = 300
height = 300
image = PhotoImage(file="image login.png").zoom(25).subsample(25)
canvas = ctk.CTkCanvas(frame, width=width, height=height, bg="#fefffb", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, padx=20, pady=20, sticky="n")

# Créer une sous-boîte (right_frame) pour le formulaire
right_frame = ctk.CTkFrame(frame, fg_color="#fefffb")
right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n", columnspan=2)  # Centrer la frame

# Créer un titre = Identifiant
label_title_id = ctk.CTkLabel(right_frame, text="Identifiant", font=("Helvetica", 20), text_color="black")
label_title_id.pack(pady=10)

# Créer un champ de saisie pour l'Identifiant
id_entry = ctk.CTkEntry(right_frame, font=("Helvetica", 20), placeholder_text="Entrer votre identifiant")
id_entry.pack(pady=10)

# Créer un titre = Mot de passe
label_title_password = ctk.CTkLabel(right_frame, text="Mot de passe", font=("Helvetica", 20), text_color="black")
label_title_password.pack(pady=10)

# Créer un champ de saisie pour le Mot de passe
password_entry = ctk.CTkEntry(right_frame, font=("Helvetica", 20), show="*", placeholder_text="Entrer votre mot de passe")
password_entry.pack(pady=10)


# Créer un bouton "Soumettre"
submit_button = ctk.CTkButton(right_frame, text="Soumettre", font=("Helvetica", 16), fg_color="#4CAF50", text_color="white", hover_color="#45a049", command=submit_form)
submit_button.pack(pady=20)

# Créer un bouton "Mot de passe perdu"
generate_password_button = ctk.CTkButton(right_frame, text="Mot de passe perdu ?", font=("Helvetica", 12), fg_color="#fefffb", text_color="black", hover_color="#f1f1f1")
generate_password_button.pack(pady=20)



# Créer une barre de menu (avec tkinter)
menu_bar = Menu(window)

# Créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Créer un compte")
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Configurer la fenêtre pour ajouter la barre de menu
window.config(menu=menu_bar)

# Afficher la fenêtre
window.mainloop()
