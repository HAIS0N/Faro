from customtkinter import *
from PIL import Image

# Fonction pour ouvrir la fenêtre de création de compte
def open_signup_window():
    signup_window = CTkToplevel(main)
    signup_window.title("Créer un compte")
    signup_window.geometry("400x400")
    signup_window.config(bg="white")

    # Cadre principal
    frame_signup = CTkFrame(signup_window, fg_color="#D9D9D9", bg_color="white", height=350, width=300, corner_radius=20)
    frame_signup.pack(pady=20, padx=20, fill="both", expand=True)

    # Titre
    label_signup_title = CTkLabel(frame_signup, text="Créer un compte", text_color="black", font=("", 24, "bold"))
    label_signup_title.pack(pady=20)

    # Champ de saisie pour le nom d'utilisateur

    entry_signup_username = CTkEntry(frame_signup, fg_color="black", text_color="white", placeholder_text="Nom d'utilisateur", placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15, height=45)
    entry_signup_username.pack(pady=5)

    # Champ de saisie pour le mot de passe

    entry_signup_password = CTkEntry(frame_signup, fg_color="black", text_color="white", placeholder_text="Mot de passe", placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15, height=45, show="*")
    entry_signup_password.pack(pady=5)

    # Champ de saisie pour la confirmation du mot de passe

    entry_signup_confirm_password = CTkEntry(frame_signup, fg_color="black", text_color="white", placeholder_text="Confirmer le mot de passe", placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15, height=45, show="*")
    entry_signup_confirm_password.pack(pady=5, padx= 0)

    # Bouton de création de compte
    button_create_account = CTkButton(frame_signup, text="Créer un compte", font=("", 15, "bold"), height=40, width=60, fg_color="#0085FF", cursor="hand2", corner_radius=15)
    button_create_account.pack(pady=20)

# Configuration de la fenêtre principale
main = CTk()
main.title("Faro")
main.config(bg="white")
main.resizable(False, False)

bg_img = CTkImage(dark_image=Image.open("bg1.jpg"), size=(500, 500))

bg_lab = CTkLabel(main, image=bg_img, text="")
bg_lab.grid(row=0, column=0)

frame1 = CTkFrame(main, fg_color="#D9D9D9", bg_color="white", height=350, width=300, corner_radius=20)
frame1.grid(row=0, column=1, padx=40)

title = CTkLabel(frame1, text="Bienvenue sur Faro", text_color="black", font=("", 35, "bold"))
title.grid(row=0, column=0, sticky="nw", pady=30, padx=10)

usrname_entry = CTkEntry(frame1, text_color="white", placeholder_text="Identifiant", fg_color="black", placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15, height=45)
usrname_entry.grid(row=1, column=0, sticky="nwe", padx=30)

passwd_entry = CTkEntry(frame1, text_color="white", placeholder_text="Mot de passe", fg_color="black", placeholder_text_color="white", font=("", 16, "bold"), width=200, corner_radius=15, height=45, show="*")
passwd_entry.grid(row=2, column=0, sticky="nwe", padx=30, pady=20)

cr_acc = CTkLabel(frame1, text="Créer un compte", text_color="black", cursor="hand2", font=("", 15))
cr_acc.grid(row=3, column=0, sticky="w", pady=20, padx=25)
cr_acc.bind("<Button-1>", lambda e: open_signup_window())

l_btn = CTkButton(frame1, text="S'enregistrer", font=("", 15, "bold"), height=40, width=60, fg_color="#0085FF", cursor="hand2", corner_radius=15)
l_btn.grid(row=3, column=0, sticky="ne", pady=20, padx=35)

main.mainloop()
