#Criando a class Menu
class Menu:
    def __init__(self):
        self.items = {
            "1": {"nome": "Hamburguer", "preco": 10.00},
            "2": {"nome": "Batata-Frita", "preco": 7.00},
            "3": {"nome": "Refrigerante", "preco": 5.00},
        
        }

    print("-----------------------------\nRestaurante do José Henrique\n-----------------------------")
    print("------------MENU-------------")

    def exibir_menu(self):
        for key, value in self.items.items():
            print(f"{key}. {value['nome']} - R${value['preco']}")

    def obter_preco(self, codigo):
        return self.items[codigo]["preco"]
