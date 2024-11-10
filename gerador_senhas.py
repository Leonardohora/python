#importação das bibliotecas usadas
import tkinter as tk
import random as rd
import string as str
from tkinter import messagebox

class GeradorSenhas:
    def __init__(self):
        #tela e titulo
        self.tela = tk.Tk()
        self.tela.title("Gerador de Senhas")
        
        self.minusculo = tk.IntVar()
        self.maisculo = tk.IntVar()
        self.numero = tk.IntVar()
        self.simbolo = tk.IntVar()
        self.config_janela()
    
    
    def config_janela(self):
        
        boas_vindas = tk.Label(self.tela, text="Bem vindo ao gerador de senhas",fg="blue", font="Arial" )
        boas_vindas.grid(column=0, row=0, padx=5)

        quantidades_caracters = tk.Label(self.tela, text="Quantos caracters terá sua senha?")
        quantidades_caracters.grid()
        
        self.senha_comprimento = tk.Entry(self.tela)
        self.senha_comprimento.grid()
        
        tk.Checkbutton(self.tela,text="Conter Letras minusculas", variable=self.minusculo).grid()
        tk.Checkbutton(self.tela,text="Conter Letras maiúsculas", variable=self.maisculo).grid()
        tk.Checkbutton(self.tela, text="Conter Números", variable= self.numero).grid()
        tk.Checkbutton(self.tela, text="Conter Símbolos", variable=self.simbolo).grid()
        
        tk.Button(self.tela,text="Gerar senha", command=self.gerar_senha).grid()
        self.mostrar_senha = tk.Label(self.tela, text="")
        tk.Label(self.tela,text="Sua senha é:").grid()
        self.mostrar_senha.grid()
        
        tk.Button(self.tela, text="Copiar", command=self.copiar).grid()
        tk.Button(self.tela, text="Reset",command=self.reset).grid()
        
        
    def gerar_senha(self):
        
        if not self.senha_comprimento.get().isnumeric() or int(self.senha_comprimento.get()) < 8 or int(self.senha_comprimento.get()) > 20 :
            messagebox.showinfo("AVISO", "Insira apenas números de 8 a 20 Caracteres.")
            return
        
        if not (self.minusculo.get() or self.maisculo.get() or self.numero.get() or self.simbolo.get()):
            messagebox.showinfo("AVISO", "Marque pelo menos uma das opções")
            return        
        

        comprimento = int(self.senha_comprimento.get())
        caracters = ''
        
        if self.minusculo.get():
            caracters += str.ascii_lowercase
        
        if self.maisculo.get():
            caracters += str.ascii_uppercase

        if self.numero.get():
            caracters += str.digits
         
        if self.simbolo.get():
            caracters += str.punctuation
        
        senha = ''.join(rd.choice(caracters) for _ in range(comprimento))
        self.mostrar_senha.config(text=f'{senha}')
    
    
    def copiar(self):
        self.tela.clipboard_clear()
        self.tela.clipboard_append(self.mostrar_senha["text"])
        
    
    def reset(self):
        self.senha_comprimento.delete(0, tk.END)
        self.maisculo.set(0)
        self.minusculo.set(0)
        self.numero.set(0)
        self.simbolo.set(0)
        self.mostrar_senha.config(text="")
        
        
    def rodar(self):
        self.tela.mainloop()
        

 #Caso o programa seja importado como um módulo, ele não executará automaticamente.
if __name__ == "__main":
    app = GeradorSenhas()
    app.rodar()