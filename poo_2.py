import csv

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=1):
        assert price >= 0, f'Price {price} must be greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} must be greater than or equal to zero'

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)  # adiciona a instância à lista toda a vez que for instanciado.

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # decorador que transforma o método para um método de classe. cls deve ser passado como referência, no momento
    # de invocar esse método é necessário utilizar o nome da classe antes: Item.instantiate_from_csv()
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as arquivo:
            reader = csv.DictReader(arquivo)
            items = list(reader)

        for item in items:
            # para cada item instancia um objeto e põe na lista all
            Item(
                name=item.get('name'),
                price=float(item.get('price')),  # necessário converter para float (caso houver valores quebrados)
                quantity=int(item.get('quantity')) # necessário converter para inteiro
            )

    # decorador que transforma um método para estático. O met estático não recebe self (nenhuma referência da classe).
    # esse método irá contar os valores flutuantes que estão com .0. exemplo: 10.0 true, 15.0 true, 15.90 false, 7 true
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    #  Torna a representação mais legível e de acordo com a doc. Similar ao toString
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


'''
Quando utilizar métodos de classes e métodos estáticos?

Basicamente quando um método tem relação com a classe, mas usualmente são utilizados para manipular diferentes estruturas
de dados para instanciar objetos, assim como fizemos com o CSV. Então por isso há o método estático dentro da classe.

'''


#for instancia in Item.all:
    #print(instancia.name)

Item.instantiate_from_csv()
#print(Item.all)
#print(Item.is_integer(7.58))

phone1 = Item("jscPhonev10", 500, 5)
phone2 = Item("jscPhonev20", 700, 5)



