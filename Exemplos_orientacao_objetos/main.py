class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'
    
    def fazer_ligacoes(self):
        print('Fazendo ligação...')
    
    def jogar_cobrinha(self):
        print('Jogando cobrinha...')
    
    def despertador(self):
        print('Despertando...')
    
    def calcular(self, valor_1, valor_2):
        return valor_1 + valor_2
        
        
celular = Celular()

print(celular.marca)

celular.fazer_ligacoes()

print(celular.calcular(2,3))
