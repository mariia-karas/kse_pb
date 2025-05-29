def buy_product(inventory, transactions, product, quant, seller_id) :
    if product in inventory:
        amount_spent = inventory[product]["price"] * quant
        print(amount_spent)
        product_trans = {"product" : product, "price": inventory[product]["price"], "quantity": quant, "amount_spent": amount_spent}
        inventory[product]["quantity"] -= quant
        transactions.append(product_trans)
    else:
        print("Спробуй знову: ")
    return inventory
