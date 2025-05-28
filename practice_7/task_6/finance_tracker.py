transactions = []

def add_transaction(transactions, amount, trans_type, category):
    trans = {
        "amount": amount,
        "trans_type": trans_type,
        "category": category
    }
    transactions.append(trans)

add_transaction(transactions, 10000, "дохід", "зарплата")
add_transaction(transactions, 2500, "витрата", "їжа")
add_transaction(transactions, 1500, "витрата", "транспорт")

print(transactions)


def get_balance(transactions):
    total = 0
    for trans in transactions:
        if trans["trans_type"] == "дохід":
            total += trans["amount"]
        else:
            total -= trans["amount"]
    return total

print(get_balance(transactions))