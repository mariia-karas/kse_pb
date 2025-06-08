list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]

condition_1 = sum(list_1)>9
condition_2 = len(list_2)<5

if condition_1 and condition_2:
    joined_list = list_1 + list_2
    print(joined_list)
else:
    print("Якась з умов не виконується")