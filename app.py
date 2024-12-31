import customtkinter as ctk
import webbrowser

def site():
    webbrowser.open_new("https://www.lipsp.fr/")

# Créer une fenêtre
window = ctk.CTk()

# Personnaliser la fenêtre
window.title("Faro")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("Karmine_Corp_logo.svg.ico")  # Assurez-vous que l'icône existe dans le répertoire
window.configure(fg_color="#ED7F10")  # Utilisez fg_color pour la couleur de fond de la fenêtre

# Créer un cadre pour placer les textes
frame = ctk.CTkFrame(window, fg_color="#ED7F10")  # Utilisation de fg_color pour la couleur de fond du cadre

# Ajouter le premier texte
label_title1 = ctk.CTkLabel(frame, text="Bienvenue sur Faro", font=("Roboto Serif", 75), text_color="white", fg_color="#ED7F10")  # Utilisation de la police Roboto
label_title1.pack(pady=20)

# Ajouter le deuxième texte
label_title2 = ctk.CTkLabel(frame, text="Projet solidaire dirigé par Haison, Antoine, Samuel, Sarra & Nina", font=("Roboto Serif", 20), text_color="white", fg_color="#ED7F10")  # Utilisation de la police Roboto
label_title2.pack(padx=5, pady=10)

# Ajouter le bouton
pst_button = ctk.CTkButton(frame, text="Présentation du Projet", font=("Roboto", 20), fg_color="white", text_color="#ED7F10", command=site)  # Utilisation de la police Roboto
pst_button.pack(pady=25, fill="x", padx=40)

# Ajouter le cadre à la fenêtre
frame.pack(expand=True, fill="both")

# Lancer la fenêtre
window.mainloop()

