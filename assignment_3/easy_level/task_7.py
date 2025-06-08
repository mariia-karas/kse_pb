prefix = input("За яким префіксом ви шукаєте? ")
my_list = ["прибігати", "прекрасно", "припікати"]
for i in my_list:
    if i.startswith(prefix):
        print(i)