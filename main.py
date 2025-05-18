import tkinter as tk
from src.ui.window import WaTor

if __name__ == "__main__":
    #crée la fenêtre principale de l’interface graphique avec Tkinter.
    root = tk.Tk()
    # connecte l'application à la fenêtre principale.
    app = WaTor(root)
    # lance la boucle principale de l’interface graphique.
    root.mainloop()
