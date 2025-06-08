my_list = [1, 2, 3, 4, 5]

final = []

for i in my_list:
    if i % 2 == 0:
        final.append("парне")
    else:
        final.append(i)

print(final)
