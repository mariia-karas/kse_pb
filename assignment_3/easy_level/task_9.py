my_list = ["дім", "око", "тут", "сад" ]

palindroms = []

for i in my_list:
    if i == i[::-1]:
        palindroms.append(i)
print(palindroms)
