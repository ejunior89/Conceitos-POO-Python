# Embora Python não tenha suporte direto para interfaces como em outras linguagens, é possível usar classes abstratas ou protocolos para definir contratos que classes devem implementar. Aqui está um exemplo usando uma classe abstrata:

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

# Criando objetos das classes
retangulo = Retangulo(5, 3)
circulo = Circulo(4)

# Chamando método para calcular área
print("Área do retângulo:", retangulo.calcular_area())  # Saída: Área do retângulo: 15
print("Área do círculo:", circulo.calcular_area())      # Saída: Área do círculo: 50.24
