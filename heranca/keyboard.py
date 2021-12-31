from heranca.item import Item


# classe herdeira recebe a classe Mãe dentro do parâmetro.

class Keyboard(Item):
    # essa taxa foi alterada somente nessa classe. Logo quando for calcular o desconto, irá utilizar
    # essa taxa e não a taxa da classe principal. Polimorfismo
    pay_rate = 0.50


    def __init__(self, name: str, price: float, quantity=0):
        super().__init__(
            name, price, quantity
        )
