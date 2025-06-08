from collections import Counter

my_list = [3, 4, 4, 4, 5, 1, 2, 2]
my_list_за_спаданням = sorted(my_list, reverse = True)

freq = Counter(my_list_за_спаданням)

final_list = []

for num, times in freq.most_common():
    for i in range(times):
        final_list.append(num)


print(my_list_за_спаданням)
print(final_list)



