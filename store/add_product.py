
def add_product(inventory, product, quant):
    if product in inventory: 
        inventory[product]["quantity"] += quant
    else:
        price = int(input("What is your price? "))
        inventory[product] = {"price" : price, "quantity": quant}
    return inventory


