my_list = [-2, -1, 1, 2, 3, 4]
positive_nums = []
for i in my_list:
    if i > 0:
        positive_nums.append(i)

mean_positive_num = sum(positive_nums)/len(positive_nums)
print(mean_positive_num)