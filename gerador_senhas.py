#importação das bibliotecas usadas
import tkinter as tk
import random as rd
import string as str
from tkinter import messagebox

class GeradorSenhas:
    def __init__(self):
        # tela e título
        self.tela = tk.Tk()
        self.tela.configure(pady=5, padx=10, bg="#2E2E2E")
        self.tela.resizable(False, False)
        self.tela.title("Gerador de Senhas")

        self.minusculo = tk.IntVar()
        self.maisculo = tk.IntVar()
        self.numero = tk.IntVar()
        self.simbolo = tk.IntVar()
        
        self.config_janela()

    def config_janela(self):
        
        # Boas-vindas
        boas_vindas = tk.Label(self.tela, text="Bem-vindo ao Gerador de Senhas", bg="#008B8B", fg="#FFFFFF", font=("Helvetica", 16, "bold"))
        boas_vindas.grid(column=0, row=0, columnspan=2, pady=10)

        # Instruções
        instrucoes = tk.Label(self.tela, text=(
            "Instruções:\n"
            "- Insira um número entre 8 e 20 caracteres.\n"
            "- Escolha pelo menos uma opção abaixo."
        ), fg="#FFD700", bg="#2E2E2E", font=("Arial", 10))
        instrucoes.grid(column=0, row=1, columnspan=2, pady=5)

        # Comprimento da senha
        tk.Label(self.tela, text="Quantidade de caracteres:", bg="#2E2E2E", fg="#FFFFFF").grid(column=0, row=2, sticky="w")
        self.senha_comprimento = tk.Entry(self.tela, width=10)
        self.senha_comprimento.grid(column=1, row=2, pady=5, sticky="e")

        # Opções de senha (Checkboxes)
        tk.Checkbutton(self.tela, text="Letras minúsculas", variable=self.minusculo, 
                       bg="#3CB371", fg="#FFFFFF", selectcolor="#008000").grid(column=0, row=3, sticky="w")
        tk.Checkbutton(self.tela, text="Letras maiúsculas", variable=self.maisculo, 
                       bg="#3CB371", fg="#FFFFFF", selectcolor="#008000").grid(column=1, row=3, sticky="e")
        tk.Checkbutton(self.tela, text="Números", variable=self.numero, 
                       bg="#3CB371", fg="#FFFFFF", selectcolor="#008000").grid(column=0, row=4, sticky="w")
        tk.Checkbutton(self.tela, text="Símbolos", variable=self.simbolo, 
                       bg="#3CB371", fg="#FFFFFF", selectcolor="#008000").grid(column=1, row=4, sticky="e")

        # Botão de gerar senha
        tk.Button(self.tela, text="Gerar Senha", command=self.gerar_senha, bg="#00CED1", fg="#000000", font=("Arial", 10, "bold"), width=15).grid(column=0, row=5, columnspan=2, pady=10)

        # Exibir senha gerada
        tk.Label(self.tela, text="Sua senha:", bg="#2E2E2E", fg="#FFFFFF").grid(column=0, row=6, sticky="w")
        self.mostrar_senha = tk.Label(self.tela, text="", bg="#2E2E2E", fg="#FFD700", font=("Courier", 12, "bold"))
        self.mostrar_senha.grid(column=1, row=6)

        # outros botões
        tk.Button(self.tela, text="Copiar", command=self.copiar, bg="#1E90FF", fg="#FFFFFF").grid(column=1, row=8, pady=5, sticky="e")
        tk.Button(self.tela, text="Resetar", command=self.reset, bg="#FF4500", fg="#FFFFFF").grid(column=0, row=8, pady=5, sticky="w")

    def gerar_senha(self):
        if not self.senha_comprimento.get().isnumeric() or int(self.senha_comprimento.get()) < 8 or int(self.senha_comprimento.get()) > 20:
            messagebox.showinfo("AVISO", "Insira apenas números entre 8 e 20.")
            return

        if not (self.minusculo.get() or self.maisculo.get() or self.numero.get() or self.simbolo.get()):
            messagebox.showinfo("AVISO", "Selecione pelo menos uma opção.")
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
        messagebox.showinfo("Informação", "Senha copiada para a área de transferência!")


    def reset(self):
        self.senha_comprimento.delete(0, tk.END)
        self.minusculo.set(0)
        self.maisculo.set(0)
        self.numero.set(0)
        self.simbolo.set(0)
        self.mostrar_senha.config(text="")


    def rodar(self):
        self.tela.mainloop()


if __name__ == "__main__":
    app = GeradorSenhas()
    app.rodar() 