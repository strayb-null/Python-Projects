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

#Título
Label(root, text="Pedra, Papel, Tesoura", font="Roboto 15", bg=bg_color).pack(pady=10)

# Instrução e campo do usuário
Label(root, text='escolha: pedra, papel ou tesoura', font='arial 15 bold', bg=bg_color).place(x=30, y=70)
user_take = StringVar()
Entry(root, font='arial 15', textvariable=user_take, bg=bg_color).place(x=90, y=130)


#Variável do resultado
resultado = StringVar()

def jogar():
    escolha_pc = random.randint(1, 3)
    if escolha_pc == 1:
        escolha_pc = "pedra"      # = não ==
    elif escolha_pc == 2:
        escolha_pc = "papel"
    else:
        escolha_pc = "tesoura"

    escolha_usuario = user_take.get()

    if escolha_usuario == escolha_pc:
        resultado.set("Empate")
    elif escolha_usuario == 'pedra' and escolha_pc == 'tesoura':
        resultado.set(f"Você ganhou, o pc escolheu {escolha_pc}")
    elif escolha_usuario == 'pedra' and escolha_pc == 'papel':
        resultado.set(f"Você perdeu, o pc escolheu {escolha_pc}")
    elif escolha_usuario == 'papel' and escolha_pc == 'pedra':
        resultado.set(f"Você ganhou, o pc escolheu {escolha_pc}")
    elif escolha_usuario == 'papel' and escolha_pc == 'tesoura':
        resultado.set(f"Você perdeu, o pc escolheu {escolha_pc}")
    elif escolha_usuario == 'tesoura' and escolha_pc == 'papel':
        resultado.set(f"Você ganhou, o pc escolheu {escolha_pc}")
    elif escolha_usuario == 'tesoura' and escolha_pc == 'pedra':
        resultado.set(f"Você perdeu, o pc escolheu {escolha_pc}")
    else:
        resultado.set("Inválido: escolha pedra, papel ou tesoura")

def resetar():
    resultado.set("")
    user_take.set("")

def sair():
    root.destroy()


# Campo de resultado e botões
Entry(root, font='arial 10 bold', textvariable=resultado, bg=bg_color, width=50).place(x=25, y=250)
Button(root, font='arial 13 bold', text='JOGAR',  padx=5, bg=bg_color, command=jogar).place(x=150, y=190)
Button(root, font='arial 13 bold', text='RESETAR', padx=5, bg=bg_color, command=resetar).place(x=70, y=310)
Button(root, font='arial 13 bold', text='SAIR',  padx=5, bg=bg_color, command=sair).place(x=230, y=310)


root.mainloop()