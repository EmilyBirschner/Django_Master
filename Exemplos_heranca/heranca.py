class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5
    
    def acelerar(self):
        print('Acelerando...')
        
    def frear(self):
        print('Freando...')
        
    def buzinar(self):
        print('Buzinando...')
        
carro = Carro()
carro.acelerar()

#uno está herdando tudo da classe Carro
class Uno(Carro):
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992

uno = Uno()
uno.acelerar()
print(uno.numero_rodas)
print(uno.modelo)