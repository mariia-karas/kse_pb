def is_valid_price(value): 
    if value > 0:
        return True
    else:
        return False
    
def is_valid_quantity(value):
    if value > 0:
        return True
    else:
        return False
    
def format_currency(amount):
    return f"{round(amount, 2)} грн"

   

