n = int(input("Enter the number for verification: "))
my_list = [1, 2, 3, 4, 5]
verification = []


for i in my_list:
    condition = i % n == 0
    verification.append(condition)
    

print(verification)