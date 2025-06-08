my_list = ["дім", "святковий", "тут", "бестія"]
x = int(input("Введіть довжину для перевірки: "))

count = 0
for i in my_list:
    if len(i)>x:
        count+=1
print(count)