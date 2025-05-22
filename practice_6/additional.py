import random
import matplotlib.pyplot as plt
balance = 10000
iteration = 0
history = []

while balance >= 100 and iteration <= 1000:
  
  iteration += 1

  result = random.random()
  if result <= 1/37:
        balance += 3600
  else:
        balance -= 100
  history.append(balance)

print(history)

plt.plot(history)
plt.show()
