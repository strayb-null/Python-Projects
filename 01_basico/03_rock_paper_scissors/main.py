from tkinter import *
import random


#Paleta
bg_color = "#FFFFFF"

#janela principal
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title("Pedra, Papel, Tesoura")
root.config(bg = bg_color)

# Label Título
Label(
    root, 
    text="Pedra, Papel, Tesoura", 
    font=("Roboto", 15), 
    bg=bg_color 
).pack(pady=10)



if __name__ == "__main__":
    root.mainloop()