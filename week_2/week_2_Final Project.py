# -*- coding: utf-8 -*-

product1_name, product1_price = "Books", 49.95
product2_name, product2_price = "Computer", 579.99
product3_name, product3_price = "Monitor", 124.89

company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"


message = "Thanks for shopping with us today!"

print("*" * 50)
print( f"\t\t{company_name.title()}")
print( f"\t\t{company_address}")
print( f"\t\t{company_city}")

print("=" * 50)

print("\tProduct Name \t\t Product Price\n")
print( f"\t{product1_name}\t\t\t$ {product1_price}")
print( f"\t{product2_name}\t\t$ {product2_price}")
print( f"\t{product3_name}\t\t\t$ {product3_price}")


print("=" * 50)

print("\t\t\tTotal")

total = product1_price + product2_price + product3_price
print(f"\t\t\t${total}")


print("=" * 50)

print("\t" + message)

print("*" * 50)





