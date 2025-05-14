sum1 = 0
while True:
  profit = float(input("Введіть ваш місячний дохід або 0 для виходу: "))
  if profit == 0:
    break 
  elif profit < 0:
    print("Дохід не може бути від'ємним")
    continue
  else:
    print("Ваш дохід збережено")
    sum1 += profit
    print (f"Ваш дохід дорівнює {sum1}")