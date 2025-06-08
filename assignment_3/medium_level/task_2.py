my_list = [[1, "first"], [3, "fourth"], [5]]

joined_list = []

for i in my_list:
    for j in i:
        joined_list.append(j)
print(joined_list)