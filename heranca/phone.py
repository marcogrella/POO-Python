from heranca.item import Item


# classe herdeira recebe a classe Mãe dentro do parâmetro.

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=1, broken_phones=0):
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f'Broken Phones {broken_phones} must be greater than or equal to zero'

        self.broken_phones = broken_phones


