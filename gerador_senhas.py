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

        self.historico = []
        self.minusculo = tk.IntVar()
        self.maisculo = tk.IntVar()
        self.numero = tk.IntVar()
        self.simbolo = tk.IntVar()
        
        self.config_janela()


    def config_janela(self):
        
        boas_vindas = tk.Label(self.tela, text="Bem-vindo ao Gerador de Senhas", bg="#008B8B", fg="#FFFFFF", font=("Helvetica", 16, "bold"))
        boas_vindas.grid(column=0, row=0, columnspan=2, pady=10)


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

        # Opções de senha
        tk.Checkbutton(self.tela, text="Letras minúsculas", variable=self.minusculo, 
                       bg="#3CB371", fg="#FFFFFF", selectcolor="#008000", activebackground="#006400").grid(column=0, row=3, sticky="w")
        tk.Checkbutton(self.tela, text="Letras maiúsculas", variable=self.maisculo, 
                       bg="#3CB371", fg="#FFFFFF", selectcolor="#008000", activebackground="#006400").grid(column=1, row=3, sticky="e")
        tk.Checkbutton(self.tela, text="Números", variable=self.numero, 
                       bg="#3CB371", fg="#FFFFFF", selectcolor="#008000", activebackground="#006400").grid(column=0, row=4, sticky="w")
        tk.Checkbutton(self.tela, text="Símbolos", variable=self.simbolo, 
                       bg="#3CB371", fg="#FFFFFF", selectcolor="#008000", activebackground="#006400").grid(column=1, row=4, sticky="e")
        
        self.botao_copiar = tk.Button(self.tela, text="Copiar", command=self.copiar, bg="#1E90FF", fg="#FFFFFF", font=("Arial", 10, "bold"))
        self.botao_resetar = tk.Button(self.tela, text="Resetar", command=self.reset, bg="#FF4500", fg="#FFFFFF", font=("Arial", 10, "bold"))
        
        # Botão de gerar senha
        self.titulo_senha = tk.Label(self.tela, text="Sua senha:", bg="#2E2E2E", fg="#FFFFFF")
        tk.Button(self.tela, text="Gerar Senha", command=self.gerar_senha, bg="#00CED1", fg="#000000", font=("Arial", 10, "bold"), activebackground="#008B8B" , width=15, relief="groove").grid(column=0, row=5, columnspan=2, pady=20)
        self.tela.bind("<Return>", self.gerar_senha)
        tk.Button(self.tela,text="Limpar Histórico", command=self.limpar_historico, bg="#FF8C00", font=("Arial", 10, "bold"), activebackground="#FF4500").grid(column=0, row=11, sticky="ew",pady=4)
        self.lista_historico = tk.Listbox(self.tela, height=10, width=30, bg="#2E2E2E", fg="#FFD700", font=("Courier", 12, "bold"), activestyle="dotbox")
        self.lista_historico.grid(column=0, row=10)
        self.mostrar_senha = tk.Label(self.tela, text="", bg="#2E2E2E", fg="#FFD700", font=("Courier", 12, "bold"))
        
        scroll = tk.Scrollbar(self.tela, orient="vertical", command=self.lista_historico.yview)
        scroll.grid(column=0, row=10, sticky="nse")
        self.lista_historico.config(yscrollcommand=scroll.set)
        
    def gerar_senha(self, event):
        
        #validações da senha.
        if not self.senha_comprimento.get().isnumeric() or int(self.senha_comprimento.get()) < 8 or int(self.senha_comprimento.get()) > 20:
            messagebox.showinfo("AVISO", "Insira números entre 8 e 20.")
            return
        if not (self.minusculo.get() or self.maisculo.get() or self.numero.get() or self.simbolo.get()):
            messagebox.showinfo("AVISO", "Selecione pelo menos uma opção.")
            return
        
        else:
            comprimento = int(self.senha_comprimento.get())
            caracters = ''
        
            # Exibir senha gerada
            
            self.titulo_senha.grid(column=0, row=6, sticky="w")
            
            self.mostrar_senha.grid(column=1, row=6)  
            
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
            self.historico.append(senha)
            self.lista_historico.insert(tk.END, senha)
            
            #botões copiar e resetar
            self.botao_copiar.grid(column=1, row=8, pady=5, sticky="e")
            self.botao_resetar.grid(column=0, row=8, pady=5, sticky="w")

    def limpar_historico(self):
        self.historico.clear()
        self.lista_historico.delete(0, tk.END)
    
    
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
        
        self.botao_copiar.grid_remove()
        self.botao_resetar.grid_remove()
        self.titulo_senha.grid_remove()


    def rodar(self):
        self.tela.mainloop()


#Tela de login
class LoginApp:
    
    #cores
    letras =  "#DCDCDC"
    cor_fundo = "#1C1C1C"
    botoes = "#00BFFF"
    
    
    def __init__(self):
    
        self.telalogin = tk.Tk()
        self.telalogin.configure(pady=3, padx=10, bg=self.cor_fundo)
        self.telalogin.resizable(False, False)
        self.telalogin.title("Gerador de senhas")
        self.telalogin.geometry("300x200+600+250")
        self.janela_login()
        
        #login se senha autorizada a utilizar
        self.login = "leonardo"
        self.senha = "12345"
        
        
    def janela_login(self):
            
        tk.Label(self.telalogin, text="Gerador de senhas", font=("arial", 20, "bold"), bg="#2E2E2E", fg= self.letras).grid(column=0,columnspan=2, row=0, pady=20, padx=20)
        tk.Label(self.telalogin,text="Login: ", bg="#2E2E2E", fg=self.letras).grid(column=0, row=1, padx=20, pady=10)
        self.entrar_login = tk.Entry(self.telalogin)
        self.entrar_login.grid(column=1, row=1 ,sticky="n",pady=10)
        tk.Label(self.telalogin,text="Senha:", bg="#2E2E2E", fg=self.letras).grid(column=0, row=2, padx=20,pady=10)
        self.entrar_senha = tk.Entry(self.telalogin)
        self.entrar_senha.grid(column=1, row=2,pady=10)
        self.logar = tk.Button(self.telalogin, text="Entrar", command=self.entrar, bg=self.botoes)
        self.logar.grid(column=1, row=3, sticky="e", pady=2, padx=22)
        self.telalogin.bind("<Return>", self.entrar)
    
    
    def entrar(self, event=None):
        if self.entrar_login.get() == self.login and self.entrar_senha.get() == self.senha:
            self.telalogin.destroy()
            GeradorSenhas().rodar()
            #from gerador_senhas import GeradorSenhas
            #GeradorSenhas().rodar()
            
        else:
            messagebox.showwarning("AVISO", "Login ou senha estão incorretos")
    
    
    def rodar_login(self):
        self.telalogin.mainloop()


if __name__ == "__main__":
    lg = LoginApp()
    lg.rodar_login() 
