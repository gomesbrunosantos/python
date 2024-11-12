class Produto:
    def _init_(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Padaria:
    def _init_(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado à padaria.")

    def listar_produtos(self):
        print(f"Produtos disponíveis na padaria '{self.nome}':")
        for produto in self.produtos:
            print(f"Nome: {produto.nome} - Preço: R${produto.preco} - Quantidade: {produto.quantidade}")

    def vender_produto(self, nome_produto, quantidade):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                    print(f"{quantidade} unidades de '{produto.nome}' vendidas.")
                else:
                    print(f"Desculpe, não há {quantidade} unidades de '{produto.nome}' disponíveis para venda.")
                return
        print(f"Desculpe, '{nome_produto}' não está disponível na padaria.")

# Exemplo de uso:
if _name_ == "_main_":
    padaria = Padaria("Minha Padaria")

    pao_frances = Produto("Pão Francês", 0.50, 100)
    padaria.adicionar_produto(pao_frances)

    bolo_chocolate = Produto("Bolo de Chocolate", 20.00, 10)
    padaria.adicionar_produto(bolo_chocolate)

    padaria.listar_produtos()

    padaria.vender_produto("Pão Francês", 10)
    padaria.vender_produto("Bolo de Chocolate", 5)

    padaria.listar_produtos()