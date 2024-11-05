#importação das bibliotecas usadas
import tkinter as tk
import random as rd
import string as str

#configuração da janela
tela = tk.Tk()
tela.geometry("600x480+500+200") #"+500+200 é para definir a posição inicial da janela na tela."
tela.title("Gerador de senhas")


bvindas = tk.Label(tela, text="Boas vindas ao Gerador de senhas.", bg="gray")
bvindas.place(x=20, y=10)

#variaveís de controle, serve para saber se as opções estão marcadas ou não. 1 = sim/0 == não
opcao1 = tk.IntVar()
opcao2 = tk.IntVar()
opcao3 = tk.IntVar()


#função para gerar senha.
def gerar_senha():
    
    if not senha_comprimento.get().isnumeric():
        campo_vazio.config(text="digite um numero válido")
        
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
                
            letras += str.ascii_lowercase
            
            senha = ''.join(rd.choice(letras) for l in range(comprimento))
            mostrar_senha.config(text=senha)
            
        else:
            erro.config(text="Sua senha deverá que ter entre 8 a 20 caracters.")

#função para copiar a senha
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

campo_vazio = tk.Label(tela, text="")
campo_vazio.place(x=410, y=25)

erro = tk.Label(tela,text="")
erro.place(x=20, y=40)

botao_gerar = tk.Button(tela, text="clique aqui", command=lambda: gerar_senha())
botao_gerar.place(x=20, y=60)

mostrar_senha = tk.Label(tela, text="")
mostrar_senha.place(x=20,y=90)

botao_copiar_senha = tk.Button(tela, text="Copiar senha", command=lambda:copiar())
botao_copiar_senha.place(x=15, y=120)


tela.mainloop()