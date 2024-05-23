class animal():
    def __init__(self, nome, idade, alimentacao):
        self.nome = nome
        self.idade = idade
        self.alimentacao = alimentacao

    def som(self):
        pass
    
    
    def info(self):
        return f"O nome do animal é: {self.nome}\nele tem {self.idade} anos de idade,\nele é {self.alimentacao}"
    

class mamifero(animal):
    def __init__(self, nome, idade, alimentacao, tempo_gestacao):
        super().__init__(nome, idade, alimentacao)
        self.tempo_gestacao = tempo_gestacao
        
        
    def som(self):
        return 'sons de mamifero'


class ave(animal):
    def __init__(self, nome, idade, alimentacao, capacidade_voo):
        super().__init__(nome, idade, alimentacao)
        self.capacidade_voo = capacidade_voo
        
    def som(self):
        return 'sons de ave'
        
        
        
class reptil(animal):
    def __init__(self, nome, idade, alimentacao, veneno):
        super().__init__(nome, idade, alimentacao)
        self.veneno = veneno
        
    def som(self):
        return 'shhhhh'
            
#canivoro        
leao = mamifero("leao", 5, "Carnivoro", 3)
elefante = mamifero("elefante", 15, "Herbívoro",22)

#ave
galinha = ave("galinha", 3, "Herbívoro", False)
picapau = ave("Pica-pau", 2,"herbivoro", True)

#reptil
jacare = reptil("Jacare", 5, "Carnivoro", "Não")
cobra = reptil("Cobra", 2, "Carnívoro", "Sim")

animais = [leao, elefante, picapau, galinha, jacare, cobra]

for animal in animais:
    print(animal.info())
    print(f"Emitiu o som - {animal.som()}")
    print(*'')