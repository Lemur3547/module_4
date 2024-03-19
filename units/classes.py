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

    def __len__(self):
        """
        Функция для подсчета количества товара на складе в данной категории
        :return: Количество товара
        """
        count = 0
        for i in self._products:
            count += i.quantity
        return count

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    # @property
    def add_product(self, product):
        if product not in self._products:
            self._products.append(product)
        return self._products

    @property
    def get_products(self):
        products_list = []
        for product in self._products:
            if product not in products_list:
                products_list.append(str(product))
        return products_list


class Product:
    name: str
    description: str
    price: float
    quantity: int

    __products = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self._price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return (self._price * self.quantity) + (other._price * other.quantity)

    @classmethod
    def add_product(cls, product):
        pr = cls(product["name"], product["description"], product["price"], product["quantity"])

        for i in cls.__products:
            if i.name == pr.name:
                i.quantity += pr.quantity
                i._price = max(i._price, pr._price)
                return i
        cls.__products.append(pr)
        return pr

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


class ProductIteration:
    category: list

    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        self.current_value += 1
        if self.current_value < len(self.category):
            return self.category[self.current_value]
        else:
            raise StopIteration
