import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=1):
        assert price >= 0, f'Price {price} must be greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} must be greater than or equal to zero'

        # como é um atributo com @property o _ serve para instanciar um valor inicial. Tipo um Setter
        # com __ o atributo fica privado à classe.
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        Item.all.append(self)  # adiciona a instância à lista toda a vez que for instanciado.

    # Encapsulamento: utilizamos esse decorador para deixar os atributos privados, isto é, instanciáveis somente
    # no objeto, e não podendo ser alterado novamente. Então fica somente leitura.
    # @ Property = Read-Only Atributo
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    # esse decorador serve para definir um novo valor para o atributo
    @name.setter
    def name(self, value):
        print('passou pelo setter')
        self.__name = value

    def calculate_total_price(self):
        return self.__price * self.__quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @classmethod
    def instantiate_from_csv(cls):
        with open('../items.csv', 'r') as arquivo:
            reader = csv.DictReader(arquivo)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # self.__class__.__name__ é um método que identifica qual classe está executando:

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __connect(self, smtp_server):  # __ torna o método privado à classe.
        pass

    def __send(self):
        pass

    def __prepare_body(self):
        return f'Hello. We have {self.name} {self.quantity} times. Regards. '

    def send_email(self):   # método publico que acessa os métodos privados.
        self.__connect('')
        self.__prepare_body()
        self.__send()


    #@property
    #def read_only_name(self):
        #return "AAA"
