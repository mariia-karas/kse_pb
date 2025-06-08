y = int(input("Введіть число, на яке має бути помножений список: "))
x = int(input("Введіть число, для перевірки: "))

my_list = [1, 2, 3, 4, 5]

for i in my_list:
    if i>x:
        i *= y
        print(i)
    else:
        print("Умова не виконується")