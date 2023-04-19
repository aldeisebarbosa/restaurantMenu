# Importando pedidos.py
from pedidos import Pedido

class Conta:
    def __init__(self):
        self.pedido = Pedido()

    def fazer_pedido(self):
        while True:
            self.pedido.menu.exibir_menu()
            codigo = input("\nDigite o código do item que deseja adicionar (ou '0' para finalizar o pedido): ")
            if codigo == "0":
                break
            self.pedido.adicionar_item(codigo)
            print("\nPedido atual:")
            self.pedido.exibir_pedido_atual()
            print("")

    def exibir_conta(self):
        print("\n\nConta:")
        self.pedido.exibir_pedido_atual()
