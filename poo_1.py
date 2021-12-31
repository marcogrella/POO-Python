
 # métodos que possuem __str__ (por exemplo) são chamados de magic methods

class Item:
    # atributo de classe. Podemos alterá-lo no nível da instancia atribuindo um valor diretamente pelo objeto:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=1):   # quantity já especifica um tipo de forma automatica
        # validações aos argumentos recebidos:
        assert price >= 0, f'Price {price} must be greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} must be greater than or equal to zero'


        # define os valores aos objetos
        self.name = name
        self.price = price
        self.quantity = quantity

    ''' 
        self -> é gerado automaticamente porque em python é sempre necessário pelo menos um parâmetro em um método,
        por isso ele passa um objeto de sí (referência da classe). Quando fazemos a chamada do método:
        item1.calculate_total_price(item1.price, item1.quantity) no caso:
        self -> item1 , x -> item1.price, y-> item1.quantity
    '''


    def calculate_total_price(self):  # função dentro de classe é método
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

'''
item1 = Item("Phone", 100, 5)
print(Item.__dict__)  # __dict__ mostra os atributos no nível de classe em forma de dicionário
print(item1.__dict__)  # __dict__ mostra os atributos no nível de instância em forma de dicionário

item2 = Item("Laptop", 1500, 5)
print(item1.price)  # 100
item1.apply_discount()  # .80
print(item1.price) # 80

print(item2.price)   # 1500
item2.pay_rate = 0.7      # alteramos no nível da instância
item2.apply_discount()   # 1050
print(item2.price)

'''

item1 = Item("Phone", 100, 5)
item2 = Item("laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
