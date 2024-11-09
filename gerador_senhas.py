#importação das bibliotecas usadas
import tkinter as tk
import random as rd
import string as str
from tkinter import messagebox
#configuração da janela
tela = tk.Tk()
tela.title("Gerador de senhas")


bvindas = tk.Label(tela, text="Boas vindas ao Gerador de senhas.", bg="blue")
bvindas.grid()

#variaveís de controle, serve para saber se as opções estão marcadas ou não. 1 = sim/0 == não

opcao1 = tk.IntVar()
opcao2 = tk.IntVar()
opcao3 = tk.IntVar()
opcao4 = tk.IntVar()


#função para gerar senha.
def gerar_senha():
    
    if not senha_comprimento.get().isnumeric():
        messagebox.showinfo("Aviso", "Digite apenas Números.")
        
    else:
        comprimento = int(senha_comprimento.get())    
        letras = ''
        
        if comprimento >= 8 and comprimento <= 20:
            
            if opcao1.get() == 1:
                letras += str.punctuation
                
            if opcao2.get() == 1:
                letras += str.digits
                
            if opcao3.get() == 1:
                letras += str.ascii_uppercase
                
            if opcao4.get() == 1:
                letras+= str.ascii_lowercase
                
            if opcao1.get() == 0 and opcao2.get() == 0 and opcao3.get() == 0 and opcao4.get() == 0:
                messagebox.showinfo("Aviso", "Marque pelo menos uma das opções.")
                return
    
            
            senha = ''.join(rd.choice(letras) for _ in range(comprimento))
            mostrar_senha.config(text=f"A senha é: {senha}")
            
        else:
                messagebox.showinfo("Aviso", "Sua senha deverá entre 8 e 20 caracetrs")


#função para copiar a senha
def copiar():
    tela.clipboard_clear()
    tela.clipboard_append(mostrar_senha["text"])
    
    
texto_comprimento = tk.Label(tela, text="Quantos Caracters será a senha?")
texto_comprimento.grid()

senha_comprimento = tk.Entry(tela)
senha_comprimento.grid()

chk_simbolo1 = tk.Checkbutton(tela, text="Símbolos", variable=opcao1)
chk_simbolo1.grid()

chk_simbolo2 = tk.Checkbutton(tela, text="Números", variable=opcao2)
chk_simbolo2.grid()

chk_simbolo4 = tk.Checkbutton(tela, text="Letras minusculas", variable=opcao4)
chk_simbolo4.grid()

chk_simbolo3 = tk.Checkbutton(tela, text="Letras maisculas", variable=opcao3)
chk_simbolo3.grid()

botao_gerar = tk.Button(tela, text="Gerar senha", command=lambda: gerar_senha())
botao_gerar.grid()

mostrar_senha = tk.Label(tela, text="")
mostrar_senha.grid(pady=10)

botao_copiar_senha = tk.Button(tela, text="Copiar senha", command=lambda:copiar())
botao_copiar_senha.grid()

tela.mainloop()