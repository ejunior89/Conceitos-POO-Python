# Associação refere-se à relação entre objetos de diferentes classes. Aqui está um exemplo de associação em Python:

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}."

class Casa:
    def __init__(self, endereco, morador):
        self.endereco = endereco
        self.morador = morador

    def informar_morador(self):
        return f"A casa localizada em {self.endereco} pertence a {self.morador.nome}."

# Criando objetos das classes
pessoa = Pessoa("João")
casa = Casa("Rua ABC, 123", pessoa)

# Chamando métodos
print(pessoa.apresentar())        # Saída: Olá, meu nome é João.
print(casa.informar_morador())    # Saída: A casa localizada em Rua ABC, 123 pertence a João.
