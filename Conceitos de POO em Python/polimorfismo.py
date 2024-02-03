# O polimorfismo é um conceito fundamental da Programação Orientada a Objetos (POO) que se refere à capacidade de objetos de diferentes classes responderem ao mesmo método de maneira diferente.
# Em outras palavras, o polimorfismo permite que um método tenha diferentes implementações em classes diferentes, mas com a mesma interface, o que facilita a reutilização de código e torna o sistema mais flexível e extensível.
# Existem duas formas principais de implementar o polimorfismo em Python: sobrescrita de métodos (métodos em classes filhas substituem métodos em classes pai) e o uso de interfaces (classes abstratas ou interfaces definem um conjunto de métodos que devem ser implementados por suas subclasses).

# Vamos ver um exemplo simples de sobrescrita de método em Python:


class Animal:
    def falar(self):
        raise NotImplementedError("Subclasse deve implementar o método 'falar'")

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Vaca(Animal):
    def falar(self):
        return "Muuu!"

def fazer_barulho(animal):
    print(animal.falar())

cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

fazer_barulho(cachorro)  # Saída: Au Au!
fazer_barulho(gato)      # Saída: Miau!
fazer_barulho(vaca)      # Saída: Muuu!
