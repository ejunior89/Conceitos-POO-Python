# Herança é um dos conceitos fundamentais da Programação Orientada a Objetos (POO) e refere-se à capacidade de uma classe (subclasse ou classe derivada) herdar atributos e métodos de outra classe (superclasse ou classe base).
# Quando uma classe herda de outra, a subclasse pode acessar e reutilizar os atributos e métodos da superclasse, além de adicionar novos atributos e métodos próprios ou até mesmo sobrescrever os métodos existentes para personalizar seu comportamento.
# Vamos ver um exemplo simples de herança em Python:

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        return "O carro está acelerando."

    def frear(self):
        return "O carro está freando."

class CarroEsportivo(Carro):
    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo)
        self.potencia = potencia

    def acelerar(self):
        return "O carro esportivo está acelerando muito rápido!"

class CarroFamilia(Carro):
    def __init__(self, marca, modelo, capacidade):
        super().__init__(marca, modelo)
        self.capacidade = capacidade

    def acelerar(self):
        return "O carro da família está acelerando suavemente."

# Criando objetos das classes
carro_generico = Carro("Toyota", "Corolla")
carro_esportivo = CarroEsportivo("Ferrari", "458 Italia", "800 cv")
carro_familia = CarroFamilia("Honda", "Civic", 5)

# Chamando os métodos
print(carro_generico.acelerar())  # Saída: O carro está acelerando.
print(carro_esportivo.acelerar())  # Saída: O carro esportivo está acelerando muito rápido!
print(carro_familia.acelerar())    # Saída: O carro da família está acelerando suavemente.
