class Category:
    name: str
    description: str
    products: list
    categories: int
    quantity_unique_products: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.quantity_unique_products = len(products)


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
