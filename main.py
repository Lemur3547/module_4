from units.classes import Product
from units.read_json import read_json

products_list = read_json()

products_list[1].add_product(Product.add_product({"name": "Советский", "description": "Может быть работает", "price": 1500.0, "quantity": 2}, products_list))
products_list[1].add_product(Product.add_product({"name": "Советский", "description": "Может быть работает", "price": 2000.0, "quantity": 1}, products_list))
print(products_list[1].get_products)

print(products_list[0]._products[1].price)
products_list[0]._products[1].price = float(input("Введите новую цену "))
print(products_list[0]._products[1].price)