#5
people = {
    "Anna": "Kyiv",
    "Bohdan": "Lviv",
    "Oksana": "Kyiv",
    "Dmytro": "Odesa"
}

unique_citys = list(set(people.values()))
print(unique_citys)
names = list(people.keys())
print(names)

mista = {}
for i in unique_citys:
  mista[i] = []
for key, value in people.items():
  mista[value].append(key)
print(mista)
