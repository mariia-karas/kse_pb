my_dict = [{'yellow': 1}, {'blue': 2}, {'yellow': 3}, {'blue': 4}, {'red': 1}]

final = {}

for i in my_dict:
    for color in i:
        if color in final:
            final[color] += i[color]
        else:
            final[color] = i[color]
print(final)