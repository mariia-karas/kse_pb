def uah_to_usd(amount_uah, rate):
  return amount_uah*rate


def usd_to_uah(amount_usd, rate):
  return amount_usd/rate
print(usd_to_uah(1000, 39.5))