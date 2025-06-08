list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]

final = []

print(list(zip(list_1, list_2)))

for x, y in zip(list_1, list_2):
    final.append(x)
    final.append(y)
print(final)