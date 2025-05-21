def calculate_wacc(equity, debt, cost_of_equity, cost_of_debt, tax_rate):
  return ((equity/(equity+debt)*cost_of_equity)+(debt)/(equity+debt)*cost_of_debt*(1-tax_rate))