#3
grades = [
    [90, 85, 88],
    [75, 80, 79],
    [95, 92, 96],
    [88, 85, 84]
]

mid_grade_list = []

for i in grades:
  mid_grade = sum(i) / len(i)
  mid_grade_list.append(mid_grade)
print(mid_grade_list)
mean_value = max(mid_grade_list)

for index,value in enumerate(mid_grade_list):
  if value == mean_value:
    break

print(index)
print(round(mv,2))
