from data import inventory, transactions
from add_product import add_product
from buy_product import buy_product


while True:
    action = int(input("Введіть бажану дію: "))
    if action == 1:
        product = input("Який товар додати? ")
        quant = int(input("Скільки одиниць ви хочете додати? "))
        inventory = add_product(inventory, product, quant)

    elif action == 2:
        product = input("Який товар бажаєте купити? ")
        quant = int(input("Скільки одиниць ви бажаєте купити? "))
        inventory = buy_product(inventory, transactions, product, quant, 1) 
        print(transactions)
    elif action == 3:
        print(3)
    
    elif action == 0:
        break