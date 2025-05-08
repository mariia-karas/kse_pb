import math

r1 = 30
area1 = math.pi * (r1) ** 2
print(area1)

r2 = 36.3
area2 = math.pi * (r2) ** 2
print(area2)

diff = ((area2 - area1) * 100) / area1
print(diff)

z = "{:.2f}".format(diff)
print(f"Друга піца більша за першу на {z} %")
