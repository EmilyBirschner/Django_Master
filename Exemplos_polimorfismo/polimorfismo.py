class Animal:
    def emitir_som(self):
        print('Qualquer som...')
        
class Cachorro(Animal):
    def emitir_som(self):
        print('Au au!')

class Gato(Animal):
    def emitir_som(self):
        print('Miau!')

#Esse é o polimorfismo de Classe, mas pode subescrever propriedade tbm                
cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()