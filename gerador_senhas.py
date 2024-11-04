import tkinter as tk
import random as rd
import string as str


tela = tk.Tk()
tela.geometry("600x480")
tela.title("Gerador de senhas")

bvindas = tk.Label(tela, text="Boas vindas ao Gerador de senhas.", bg="gray")
bvindas.place(x=20, y=10)

opcao1 = tk.IntVar()
opcao2 = tk.IntVar()
opcao3 = tk.IntVar()

def gerar_senha():
    comprimento = int(senha_comprimento.get())    
    letras = ''
    
    if opcao1.get() == 1:
        letras += str.punctuation
        
    if opcao2.get() == 1:
        letras += str.digits
        
    if opcao3.get() == 1:
        letras += str.ascii_uppercase
        
    letras += str.ascii_lowercase
    
    senha = ''.join(rd.choice(letras) for l in range(comprimento))
    mostrar_senha.config(text=senha)
        
    return gerar_senha


def copiar():
    tela.clipboard_clear()
    tela.clipboard_append(mostrar_senha["text"])
    
    
texto_comprimento = tk.Label(tela, text="Quantos Caracters será a senha?")
texto_comprimento.grid()

senha_comprimento = tk.Entry(tela)
senha_comprimento.grid()

chk_simbolo1 = tk.Checkbutton(tela, text="Símbolos", variable=opcao1, command=opcao1)
chk_simbolo1.grid(padx=300, pady=5)

chk_simbolo2 = tk.Checkbutton(tela, text="Números", variable=opcao2, command=opcao2)
chk_simbolo2.grid(pady=1)

chk_simbolo3 = tk.Checkbutton(tela, text="Letras maisculas", variable=opcao3,command=opcao3)
chk_simbolo3.grid(pady=1)

gerar = tk.Button(tela, text="clique aqui", command=lambda: gerar_senha())
gerar.place(x=20, y=60)

mostrar_senha = tk.Label(tela, text="")
mostrar_senha.place(x=20,y=90)

copiar_senha = tk.Button(tela, text="Copiar senha", command=lambda:copiar())
copiar_senha.place(x=15, y=120)


tela.mainloop()