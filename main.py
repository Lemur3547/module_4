from units.classes import Product, ProductIteration, Smartphone, Grass, Order, Category
from units.read_json import read_json

products_list = read_json()

# print(str(products_list[1]))
#
# products_list[1].add_product(Product.add_product({"name": "Советский", "description": "Может быть работает",
#                                                   "price": 1500.0, "quantity": -2}))
# products_list[1].add_product(Product.add_product({"name": "новый", "description": "Может быть работает",
#                                                   "price": 2000.0, "quantity": 1}))
# products_list[1].add_product(Product.add_product({"name": "Советский", "description": "Может быть работает",
#                                                   "price": 1100.0, "quantity": 3}))
# products_list[1].add_product(Product.add_product({"name": "новый", "description": "Может быть работает",
#                                                   "price": 1500.0, "quantity": 1}))
# # for i in products_list[1].get_products:
#     print(i)
# products_list.append(Category("sus", "atata", []))
# print(products_list[2].avg_price())
#
# print(len(products_list[1]))
#
# new = products_list[1]._products[1] + products_list[1]._products[2]
#
# print(new)

# tvs = ProductIteration(products_list[1]._products)
# print(list(tvs))
#
# for i in tvs:
#     print(i)
#
# print(str(products_list[1]))

# products_list[0].add_product(Product.add_product({}, 12, 3))
#
# print(products_list[0]._products[1].price)
# products_list[0]._products[1].price = float(input("Введите новую цену "))
# print(products_list[0]._products[1].price)
#
# print(products_list[1]._products[1]._price)
#
# products_list[1]._products[1].price = 4000
#
# print(products_list[1]._products[1]._price)


# new = Product("asas", "asasa", 12, 2)
# smartphone = Smartphone("AininyA", "SusakskiE", 39990.00, 7, 31, "12-931JK", 64, "green")
# grass = Grass("Трава", "Красивая", 1200.00, 12, "Румыния", "15 дней", "Зеленая")

# print(repr(new))
# print(repr(smartphone))
# print(repr(grass))

new_order = Order(products_list[0]._products[1], -2)

# print(new_order.product)
# print(new_order.quantity)
# print(new_order.final_price)
