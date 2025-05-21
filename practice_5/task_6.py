prices = [1, 2, 3]
quantities = [1, 2, 3]



def weighted_average_price(prices, quantities):
  total = 0
  for i, num in enumerate(prices):
    step = prices[i]*quantities[i]
    total += step
  wap = total/sum(quantities)
  return wap


weighted_average_price([1, 2, 3], [1, 2, 3] )