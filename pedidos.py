#Importando 
from menu import Menu

class Pedido:
    def __init__(self):
        self.menu = Menu()
        self.pedido_atual = {}

    def adicionar_item(self, codigo):
        if codigo in self.menu.items:
            if codigo in self.pedido_atual:
                self.pedido_atual[codigo]["quantidade"] += 1
            else:
                self.pedido_atual[codigo] = {"nome": self.menu.items[codigo]["nome"], "preco": self.menu.obter_preco(codigo), "quantidade": 1}

    def exibir_pedido_atual(self):
        total = 0
        for item in self.pedido_atual.values():
            total += item["preco"] * item["quantidade"]
            print(f"{item['quantidade']}x {item['nome']} - R${item['preco']:.2f}")
        print(f"Total: R${total:.2f}")
