# A abstração é um dos princípios fundamentais da Programação Orientada a Objetos (POO) e refere-se ao processo de modelar objetos do mundo real como entidades simplificadas em código.
# Em outras palavras, abstração envolve identificar e representar apenas as características mais relevantes de um objeto, ignorando detalhes menos importantes.
# A abstração é um dos princípios fundamentais da Programação Orientada a Objetos (POO) e refere-se ao processo de modelar objetos do mundo real como entidades simplificadas em código. Em outras palavras, abstração envolve identificar e representar apenas as características mais relevantes de um objeto, ignorando detalhes menos importantes.
# Na prática, ao criar classes e objetos em Python, estamos aplicando o conceito de abstração.
# Por exemplo, ao modelar um carro em um programa, podemos criar uma classe Carro com atributos como marca, modelo e cor, e métodos como acelerar, frear e virar. Aqui, estamos abstraindo as características essenciais de um carro e representando-as em código.
# A abstração permite simplificar a complexidade do mundo real, tornando mais fácil entender e trabalhar com objetos em um sistema de software.
# Ela também promove a reutilização de código, uma vez que objetos abstraídos podem ser reutilizados em diferentes contextos e situações.
# Além disso, a abstração facilita a manutenção do código, pois torna mais claro o propósito e o comportamento dos objetos.

# Exemplos:

# Classe animal
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        pass  # Método abstrato

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

cachorro = Cachorro("Rex", 3)
print(cachorro.emitir_som())  # Saída: Au Au!

#Classe forma geometrica
class FormaGeometrica:
    def calcular_area(self):
        pass  # Método abstrato

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

retangulo = Retangulo(5, 3)
print("Área do retângulo:", retangulo.calcular_area())  # Saída: Área do retângulo: 15

circulo = Circulo(4)
print("Área do círculo:", circulo.calcular_area())  # Saída: Área do círculo: 50.24

# classe conta bancaria
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

class ContaPoupanca(ContaBancaria):
    def calcular_juros(self):
        return self.saldo * 0.05  # Taxa de juros de 5%

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo, limite):
        super().__init__(saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Limite de saque excedido.")

conta_poupanca = ContaPoupanca(1000)
conta_poupanca.depositar(500)
print("Saldo da poupança:", conta_poupanca.saldo)  # Saída: Saldo da poupança: 1500
print("Juros da poupança:", conta_poupanca.calcular_juros())  # Saída: Juros da poupança: 75.0

