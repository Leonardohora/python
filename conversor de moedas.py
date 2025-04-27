import requests


class Conversor_moeda:
    def __init__(self, valor):
        self.valor = valor


    def converter_dolar(self):
        requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL')
        requisicao1 = requisicao.json()["USDBRL"]['bid']
        valor_convertido = self.valor * float(requisicao1)
        print(f"O valor Atual do Dolar está: {float(requisicao1):.2f}$")
        return f"R${valor_convertido:.2f}".replace('.', ',')
    

    def converter_euro(self):
        requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL')
        requisicao1 = requisicao.json()["EURBRL"]['bid']
        valor_convertido = self.valor * float(requisicao1)
        print(f"O valor Atual do Euro está: {float(requisicao1):.2f}€")
        return f"R${valor_convertido:.2f}".replace('.', ',')
    

valor = float(input('Digite o valor em reais: '))
conversor = Conversor_moeda(valor)
print('\n----------------------------------')
print(f'Convertendo Real em dolares é: {conversor.converter_dolar()}')
print('----------------------------------')
print('----------------------------------')
print(f'Convertendo Real em euros é: {conversor.converter_euro()}')