# O encapsulamento é um conceito importante na Programação Orientada a Objetos (POO) que se refere à ideia de agrupar dados (atributos) e operações (métodos) relacionados em uma única unidade (classe) e controlar o acesso a esses membros.
# Em Python, o encapsulamento é mais uma convenção do que uma regra rígida devido à natureza da linguagem, mas ainda assim é possível aplicar os princípios de encapsulamento para garantir a integridade dos dados e a segurança do código.
# Existem três níveis de acesso em Python:

# 1. Public: Atributos e métodos públicos podem ser acessados de fora da classe. Em Python, todos os membros de uma classe são públicos por padrão, a menos que sejam explicitamente definidos como privados ou protegidos.
# 2. Protected: Atributos e métodos protegidos têm um único sublinhado (_) como prefixo. Embora seja possível acessar esses membros de fora da classe, é uma convenção indicar que eles não devem ser acessados diretamente.
# 3. Private: Atributos e métodos privados têm dois sublinhados (__) como prefixo. Em Python, esses membros são "manglados", o que significa que o interpretador Python os renomeia adicionando o nome da classe como prefixo para evitar colisões de nomes em subclasses.

# abaixo alguns exemplos:

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca         # Público
        self.__modelo = modelo     # Privado

    def obter_modelo(self):       # Método público para acessar o atributo privado
        return self.__modelo

    def __acelerar(self):         # Método privado
        print("Acelerando...")

    def dirigir(self):            # Método público que chama um método privado
        self.__acelerar()
        print("Dirigindo...")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla")

# Acessando atributos e métodos públicos
print("Marca do carro:", meu_carro.marca)           # Saída: Toyota
print("Modelo do carro:", meu_carro.obter_modelo())  # Saída: Corolla

# Tentativa de acessar um atributo privado (Isso vai gerar um erro)
#print("Modelo do carro:", meu_carro.__modelo)       # Comentar esta linha para evitar erro, para ver o erro basta descomentar a linha.

# Chamando um método público que acessa um método privado
meu_carro.dirigir()  # Saída: Acelerando... \n Dirigindo...

