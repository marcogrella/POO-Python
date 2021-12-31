from heranca.item import Item
from heranca.phone import Phone

item1 = Item("MyItem", 750)

phone1 = Phone("jscPhonev10", 500, 5, 1)
#print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)

#print(Item.all)
#print(Phone.all)

item1 = Item("MyItem", 750)
item1.name = "OtherItem"  # proibido definir um valor para o atributo com __. Como colocamos o @setter agora podemos alterar
# print(item1.read_only_name)  # leitura pode
# item1.read_only_name = "bbbb" # proibido
#print(item1.name)
print(item1.price)
item1.apply_increment(0.2)
print(item1.price)

item1.send_email()