class Forma():
    
    def area(self):
        pass
    
class Quadrado(Forma):
    
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return self.lado ** 2 
    
class Triangulo(Forma):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura / 2 
    
quadrado = Quadrado(2)
area_quadrado = quadrado.area()
print(area_quadrado)

triangulo = Triangulo(3,5)
area_triangulo = triangulo.area()
print(area_triangulo)