x = int(input("Введіть задане число: "))
my_list = [1, 2, 3, 4, 5]

filtered = []

for i in my_list:
    if i > x:
        filtered.append(i)
print(len(filtered))