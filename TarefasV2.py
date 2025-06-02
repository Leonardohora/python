import sqlite3

class ListaTarefas:
    
    def __init__(self, tarefas):
        try:
            self.conn = sqlite3.connect(tarefas)
            self.cursor = self.conn.cursor()
            print("Conexão feita")
        except sqlite3.Error:
            print("Erro com a conexão com o banco de dados")
            self.conn = None
    
    def criar_lista(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lista TEXT NOT NULL
            )
        ''')
        self.conn.commit()
        return "Lista criada/verificada com sucesso"
    
    def inserir(self, lista):
        try:
            self.cursor.execute('INSERT INTO tarefas (lista) VALUES (?)', (lista,))
            self.conn.commit()
            return "Tarefa incluída na lista com sucesso."
        except sqlite3.Error as e:
            return f"Erro na conexão do banco de dados: {e}"
    
    def mostrar(self):
        try:
            listas = self.cursor.execute('SELECT * FROM tarefas').fetchall()
            if not listas:
                return "A lista de tarefas está vazia"
            else:
                return listas
        except sqlite3.Error as e:
            return f"Erro na conexão com o banco de dados: {e}"
    
    def atualizar(self, nova_lista, id):
        try:
            self.cursor.execute('UPDATE tarefas SET lista = ? WHERE id = ?', (nova_lista, id))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                return f"Nenhuma tarefa com o ID {id} foi encontrada"
            return f"A lista do ID {id} foi atualizada com sucesso!"
        except sqlite3.Error as e:
            return f"Erro na conexão com o banco de dados: {e}"
    
    def excluir(self, id_selecionado):
        try:
            self.cursor.execute('DELETE FROM tarefas WHERE id = ?', (id_selecionado,))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                return f"Lista não encontrada ou inexistente. O ID selecionado foi: {id_selecionado}"
            return "Lista excluída com sucesso!"
        except sqlite3.Error as e:
            return f"Erro no banco de dados: {e}"
    
    def veri_id(self, id):
        try:
            self.cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id,))
            return self.cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            return False
    
    def fechar(self):
        if self.conn:
            self.conn.close()

def main():
    banco = ListaTarefas("MinhasTarefas.db")
    print(banco.criar_lista())
    
    menu = """
    ========================================
    Esse é o menu da lista de tarefas:
    1 - Fazer uma nova lista
    2 - Mostrar lista
    3 - Atualizar uma lista
    4 - Excluir uma lista
    0 - Sair
    ========================================
    """
    
    while True:
        print(menu)
        try:
            escolha = int(input("Escolha uma opção: "))
            
            if escolha == 1:
                minhalista = input("Digite a nova tarefa: ")
                print(banco.inserir(minhalista))
            
            elif escolha == 2:
                resultado = banco.mostrar()
                if isinstance(resultado, list):
                    for item in resultado:
                        print(item)
                else:
                    print(resultado)
            
            elif escolha == 3:
                resultado = banco.mostrar()
                if isinstance(resultado, list):
                    for item in resultado:
                        print(item)
                else:
                    print(resultado)
                
                try:
                    id_atualizar = int(input("Digite o ID da tarefa para atualizar: "))
                    if banco.veri_id(id_atualizar):
                        nova_lista = input("Digite a nova tarefa: ")
                        print(banco.atualizar(nova_lista, id_atualizar))
                    else:
                        print("ID não encontrado.")
                except ValueError:
                    print("ID inválido.")
            
            elif escolha == 4:
                resultado = banco.mostrar()
                if isinstance(resultado, list):
                    for item in resultado:
                        print(item)
                else:
                    print(resultado)
                
                try:
                    id_excluir = int(input("Digite o ID da tarefa para excluir: "))
                    print(banco.excluir(id_excluir))
                except ValueError:
                    print("ID inválido.")
            
            elif escolha == 0:
                print("Encerrando o programa. Até a próxima!")
                banco.fechar()
                break
            
            else:
                print("Escolha inválida. Digite um número entre 0 e 4.")
        
        except ValueError:
            print("Entrada inválida. Digite um número.")

if __name__ == "__main__":
    main()
