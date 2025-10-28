# format specifiers -> (value : flag)

price1 = 193.098
price2 = -12223.82

print(f"price1: ${price1 :.2f}")
print(f"price1: ${price1 :10}")
print(f"price1: ${price1 :010}")
print(f"price1: ${price1 :^10}")
print(f"price2: ${price2 :>10}")

print(f"price1: ${price1 :+}")
print(f"price2: ${price2 :+}")
print(f"price2: ${price2 :,}")


