from units.classes import Product
from units.read_json import read_json

products_list = read_json()


# prod1 = Product("Советский", "Может быть работает", 1500.0, 2)
# products_list[1].add_product(Product("Советский", "Может быть работает", 1500.0, 2))
# products_list[1].add_product(Product("Советский", "Может быть работает",2000.0, 1))

products_list[1].add_product(Product.add_product({"name": "Советский", "description": "Может быть работает",
                                                  "price": 1500.0, "quantity": 2}))
products_list[1].add_product(Product.add_product({"name": "новый", "description": "Может быть работает",
                                                  "price": 2000.0, "quantity": 1}))
products_list[1].add_product(Product.add_product({"name": "Советский", "description": "Может быть работает",
                                                  "price": 1100.0, "quantity": 3}))
products_list[1].add_product(Product.add_product({"name": "новый", "description": "Может быть работает",
                                                  "price": 1500.0, "quantity": 1}))
for i in products_list[1].get_products:
    print(i)


# products_list[0].add_product(Product.add_product({}, 12, 3))

# print(products_list[0]._products[1].price)
# products_list[0]._products[1].price = float(input("Введите новую цену "))
# print(products_list[0]._products[1].price)

print(products_list[1]._products[1]._price)

products_list[1]._products[1].price = 4000

print(products_list[1]._products[1]._price)



