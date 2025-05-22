def  calculate_vat(amount):
  return amount * 0.2

def calculate_income_tax(amount):
  return (calculate_vat(amount) + amount) * 0.18