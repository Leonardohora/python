import tkinter as tk
import random as rd
import string as str
from tkinter import messagebox
from time import sleep

letras =  "#DCDCDC"
cor_fundo = "#1C1C1C"
botoes = "#00BFFF"


class GeradorSenhas:
    def __init__(self):
        # Tela e título
        self.tela = tk.Tk()
        self.tela.configure(pady=5, padx=10, bg="#2E2E2E")
        self.tela.resizable(False, False)
        self.tela.title("Gerador de Senhas")
        self.tela.geometry("445x570+500+250")
        
        # Configurar pesos para linhas e colunas
        for i in range(12):  # 12 linhas no total
            self.tela.grid_rowconfigure(i, weight=1)
        for j in range(2):  # 2 colunas no total
            self.tela.grid_columnconfigure(j, weight=1)

        self.historico = []
        self.minusculo = tk.IntVar()
        self.maisculo = tk.IntVar()
        self.numero = tk.IntVar()
        self.simbolo = tk.IntVar()
        
        self.config_janela()

    def config_janela(self):
        # Cabeçalho
        boas_vindas = tk.Label(
            self.tela, text="Bem-vindo ao Gerador de Senhas",
            bg="#008B8B", fg="#FFFFFF", font=("Helvetica", 16, "bold")
        )
        boas_vindas.grid(column=0, row=0, columnspan=2, pady=10, sticky="nsew")

        # Instruções
        instrucoes = tk.Label(
            self.tela, text=(
                "Instruções:\n"
                "- Insira um número entre 8 e 20 caracteres.\n"
                "- Escolha pelo menos uma opção abaixo."
            ),
            fg="#FFD700", bg="#2E2E2E", font=("Arial", 10)
        )
        instrucoes.grid(column=0, row=1, columnspan=2, pady=5, sticky="nsew")

        # Comprimento da senha
        tk.Label(self.tela, text="Quantidade de caracteres:", bg="#2E2E2E", fg="#FFFFFF").grid(column=0, row=2, sticky="w")
        self.senha_comprimento = tk.Entry(self.tela)
        self.senha_comprimento.grid(column=1, row=2, sticky="e", pady=5)

        # Opções de senha
        tk.Checkbutton(
            self.tela, text="Letras minúsculas", variable=self.minusculo,
            bg="#3CB371", fg="#FFFFFF", selectcolor="#008000", activebackground="#006400"
        ).grid(column=0, row=3, sticky="w")
        tk.Checkbutton(
            self.tela, text="Letras maiúsculas", variable=self.maisculo,
            bg="#3CB371", fg="#FFFFFF", selectcolor="#008000", activebackground="#006400"
        ).grid(column=1, row=3, sticky="e")
        tk.Checkbutton(
            self.tela, text="Números", variable=self.numero,
            bg="#3CB371", fg="#FFFFFF", selectcolor="#008000", activebackground="#006400"
        ).grid(column=0, row=4, sticky="w")
        tk.Checkbutton(
            self.tela, text="Símbolos", variable=self.simbolo,
            bg="#3CB371", fg="#FFFFFF", selectcolor="#008000", activebackground="#006400"
        ).grid(column=1, row=4, sticky="e")

        # Botão de gerar senha
        tk.Button(
            self.tela, text="Gerar Senha", command=self.gerar_senha,
            bg="#00CED1", fg="#000000", font=("Arial", 10, "bold"),
            activebackground="#008B8B", width=15, relief="groove"
        ).grid(column=0, row=5, columnspan=2, pady=20, sticky="nsew")

        # Exibir senha gerada
        self.titulo_senha = tk.Label(self.tela, text="Sua senha:", bg="#2E2E2E", fg="#FFFFFF")
        self.mostrar_senha = tk.Label(self.tela, text="", bg="#2E2E2E", fg="#FFD700", font=("Courier", 12, "bold"))

        # Lista de histórico com barra de rolagem
        self.lista_historico = tk.Listbox(self.tela, bg="#2E2E2E", fg="#FFD700", font=("Courier", 12, "bold"), activestyle="dotbox")
        self.lista_historico.grid(column=0, row=10, columnspan=2, sticky="nsew", pady=5)
        scroll = tk.Scrollbar(self.tela, orient="vertical", command=self.lista_historico.yview)
        scroll.grid(column=1, row=10, sticky="nse")
        self.lista_historico.config(yscrollcommand=scroll.set)

        # Botões adicionais
        self.botao_copiar = tk.Button(self.tela, text="Copiar", command=self.copiar, bg="#1E90FF", fg="#FFFFFF", font=("Arial", 10, "bold"))
        self.botao_resetar = tk.Button(self.tela, text="Resetar", command=self.reset, bg="#FF4500", fg="#FFFFFF", font=("Arial", 10, "bold"))
        tk.Button(self.tela, text="Limpar Histórico", command=self.limpar_historico, bg="#FF8C00", font=("Arial", 10, "bold"), activebackground="#FF4500").grid(column=0, row=11, sticky="ew", pady=4)
        self.logout = tk.Button(self.tela, text="Fazer logout", command=self.mudar_para_login, bg="red")
        self.logout.grid(column=1, row=11, sticky="e")

    def gerar_senha(self, event=None):
        
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
            self.mostrar_senha.grid(columnspan=2, row=6, sticky="e")  
            
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

    def mudar_para_login(self):
        self.tela.destroy()
        LoginApp().rodar_login()

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
        

class LoginApp:
        
    letras =  "#DCDCDC"
    cor_fundo = "#1C1C1C"    
    
    def __init__(self):
        
        self.mudar = CriarUsuario.rodar_criacao    
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
        self.entrar_senha = tk.Entry(self.telalogin, show="*")
        self.entrar_senha.grid(column=1, row=2,pady=10)
        self.logar = tk.Button(self.telalogin, text="Entrar", command=self.entrar, bg=botoes)
        self.logar.grid(column=1, row=3, sticky="e", pady=5, padx=22)
        self.telalogin.bind("<Return>", self.entrar)
        self.criar_usuario = tk.Button(self.telalogin, text="Criar usuario", command=self.mudar_para_criacao)
        self.criar_usuario.grid(column=0, row=3, pady=5)
    
    
    def mudar_para_criacao(self):
        self.telalogin.destroy()
        CriarUsuario().rodar_criacao()
    
    
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

#Criação de um usuário
class CriarUsuario:
    
     #cores
    letras =  "#DCDCDC"
    cor_fundo = "#1C1C1C"
    
    def __init__(self):
        self.tela_criar = tk.Tk()
        self.tela_criar.configure(pady=3, padx=10, bg=cor_fundo)
        self.tela_criar.resizable(False, False)
        self.tela_criar.title("Gerador de senhas")
        self.tela_criar.geometry("300x200+600+250")
        self.criar_usuario()
        
    
    def mudar_para_login(self):
        self.tela_criar.destroy()
        LoginApp().rodar_login()
        
        
    def criar_usuario(self):
        tk.Label(self.tela_criar, text="Crie um usuario", font=("arial", 20, "bold"), bg="#2E2E2E", fg= self.letras).grid(column=0,columnspan=2, row=0, pady=20, padx=20)
        tk.Label(self.tela_criar,text="Usuário: ", bg="#2E2E2E", fg=self.letras).grid(column=0, row=1, padx=20, pady=10)
        self.criar_login = tk.Entry(self.tela_criar)
        self.criar_login.grid(column=1, row=1 ,sticky="n",pady=10)
        tk.Label(self.tela_criar,text="Senha:", bg="#2E2E2E", fg=self.letras).grid(column=0, row=2, padx=20,pady=10)
        self.criar_senha = tk.Entry(self.tela_criar, show="*")
        self.criar_senha.grid(column=1, row=2,pady=10)
        self.criar = tk.Button(self.tela_criar, text="Criar Usuario", command=self.verificar_criacao, bg=botoes)
        self.criar.grid(column=1, row=3, sticky="e", pady=5, padx=10)
        self.voltar_login = tk.Button(self.tela_criar, text="Voltar para tela de login", command=self.mudar_para_login)
        self.voltar_login.grid(column=0, row=3, sticky="e", pady=5, padx=10)

    
    def verificar_criacao(self):
        login = self.criar_login.get()
        senha = self.criar_senha.get()
                
        if  not login.isalpha():
            messagebox.showinfo("Aviso", "O login deve conter apenas Letras!")
            return
        
        elif len(senha) < 8:
            messagebox.showinfo("Aviso", "Sua senha deve conter acima de 8 Caraceters")
            return
        
        self.tela_criar.destroy()
        self.popup_adm()
        
            
    def popup_adm(self):
        
        self.adm = tk.Tk()
        self.adm.title("Verificação")
        self.adm.geometry("280x90+601+400")
        self.adm.configure(padx=2, pady=10 ,bg="red")
        self.adm.resizable(False, False)
        
        tk.Label(self.adm, text="Senha do Administrador:").grid(column=0, row=0, padx=5, pady=10)
        self.senhadm = tk.Entry(self.adm, show="*")
        self.senhadm.grid(column=1, row=0, padx=5, pady=10)
        self.botao_autorizar = tk.Button(self.adm, text="AUTORIZAR", command= self.adm.bind("<Return>", self.autorizar), bg=botoes)
        self.botao_autorizar.grid(column=1, row=1, pady=3, padx=5, sticky="e")
    
        self.adm.mainloop()
        
                       
    def autorizar(self, event=None):
        
        if self.senhadm.get() == "12345":
            self.adm.configure(padx=5, pady=10 ,bg="green")
            messagebox.showinfo("Aviso", "Login criado")
            self.adm.destroy()
            sleep(1)
            LoginApp().rodar_login()
        
        else:
            messagebox.showwarning("Aviso", "Senha do ADM incorreta!")
    
    def rodar_criacao(self):
        self.tela_criar.mainloop()

    
if __name__ == "__main__":
    lg = LoginApp()
    lg.rodar_login()