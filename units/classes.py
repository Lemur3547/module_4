class Category:
    name: str
    description: str
    _products: list
    categories: int
    quantity_unique_products: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = products
        self.quantity_unique_products = len(products)

    # @property
    def add_product(self, product):
        self._products.append(product)
        return self._products

    @property
    def get_products(self):
        products_list = []
        for product in self._products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return products_list


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def add_product(cls, product, products):
        for i in products:
            if product["name"] == i.name or product["description"] == i.description:
                cls.quantity += i["quantity"]
                if product["price"] > cls.price:
                    cls.price = product["price"]
                return
            return Product(product["name"], product["description"], product["price"], product["quantity"])

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price >= self._price:
                self._price = new_price
                print("Успешно")
            elif new_price < self._price and input("Вы хотите понизить цену? y/n") == 'y':
                self._price = new_price
                print("Цена понижена")
            else:
                print("Отмена")
        else:
            print("Введена некорректная цена")
