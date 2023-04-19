#Importando as funções de menu, pedido e conta
from conta import Conta

def main():
    conta = Conta()
    conta.fazer_pedido()
    conta.exibir_conta()

if __name__ == "__main__":
    main()
