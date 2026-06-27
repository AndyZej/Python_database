price = Price23Vat(123)

print(price.get_pretax())  # 123
print(price.get_tax())     # 23
print(price.get_net())     # 100

price.set_tax(69)

print(price.get_pretax())  # 369
print(price.get_tax())     # 69
print(price.get_net())     # 300