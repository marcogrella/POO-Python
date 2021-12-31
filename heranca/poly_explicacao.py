# explicação do polimorfismo:

from phone import Phone
from keyboard import Keyboard


item1 = Phone("iphone", 1000, 3)
item1.apply_discount() # herda da classe mãe e utiliza o desconto em Item
print(item1.price)


keyb1 = Keyboard("Keyboard", 150, 1)
# herda da classe mãe, mas a taxa de desconto utiliza o que está na classe Keybord que é 0.50
# Logo, o método é o mesmo, mas é executado com base no polimorfismo, a taxa é calculada de acordo com a classe
keyb1.apply_discount()
print(keyb1.price)