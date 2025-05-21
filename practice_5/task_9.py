def analyze_prices(prices):
  dic = {}
  min_price = min(prices)
  max_price = max(prices)
  mean_price = sum(prices)/len(prices)

  count = 0
  for i in prices:
    if i < mean_price:
      count += 1
  dic["мінімальна_ціна"] = min_price
  dic["максимальна_ціна"] = max_price
  dic["середня_ціна"] = mean_price
  dic["кількість товарів дешевших за середнє"] = count
  print(dic)
  
  return analyze_prices(prices)