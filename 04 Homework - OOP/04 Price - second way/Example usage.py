price = Price23Vat(123)

print(price.pretax)   # 123
print(price.tax)      # 23
print(price.net)      # 100

price.tax = 69

print(price.pretax)   # 369
print(price.tax)      # 69
print(price.net)      # 300