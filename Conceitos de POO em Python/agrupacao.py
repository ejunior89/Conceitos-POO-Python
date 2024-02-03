# Agregação é uma forma especializada de associação em que um objeto contém outros objetos como parte de seu estado. Aqui está um exemplo de agregação em Python:

class CarrinhoCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Criando objetos das classes
produto1 = Produto("Camisa", 25)
produto2 = Produto("Calça", 50)

carrinho = CarrinhoCompras()
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)

# Iterando pelos produtos no carrinho
for produto in carrinho.produtos:
    print(f"Produto: {produto.nome}, Preço: R${produto.preco}")

# Saída:
# Produto: Camisa, Preço: R$25
# Produto: Calça, Preço: R$50
