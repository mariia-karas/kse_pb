#2
nums = [4, 7, 2, 4, 8, 9, 2, 10, 3, 8]
unique_nums = list(set(nums)) 

odd_nums = [num for num in unique_nums if num % 2 !=  0]

print(odd_nums[::-1])
