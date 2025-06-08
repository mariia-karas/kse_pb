x = int(input("Введіть число, на яке має ділитися: "))
y = int(input("Введіть число, на яке не має ділитися: "))

my_list = [1, 2, 3, 4, 5]
filtered = []

for i in my_list:
    if i % x == 0 and i % y != 0:
        filtered.append(i)

print(filtered)