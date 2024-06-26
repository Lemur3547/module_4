from abc import ABC, abstractmethod


class AbstractCategory(ABC):
    @abstractmethod
    def __init__(self):
        pass


class Category(AbstractCategory):
    """Класс для категорий"""
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
        """
        Метод для добавления нового товара в список товаров категории
        :param product: Добавляемый товар
        :return: Список товаров включающий новый товар
        """
        try:
            if isinstance(product, Product):
                if product not in self._products:
                    self._products.append(product)
                return self._products
            raise ValueError("Добавляемое значение не является экземпляром класса Product или его наследником")
        except ValueError as e:
            print(e)
            return self._products

    @property
    def get_products(self):
        """
        Метод для представления списка товаров в виде "<Товар>, <Цена> руб. Остаток: <Остаток> шт."
        :return: список товаров
        """
        products_list = []
        for product in self._products:
            if product not in products_list:
                products_list.append(str(product))
        return products_list

    def avg_price(self):
        try:
            avg_price = round(sum([i._price for i in self._products]) / len(self._products), 2)
            return avg_price
        except ZeroDivisionError:
            return 0


class Order(AbstractCategory):
    def __init__(self, product, quantity):
        try:
            if quantity > 0:
                self.product = product
                self.quantity = quantity
                self.final_price = product._price * quantity
            else:
                raise ZeroProductQuantity
        except ZeroProductQuantity as e:
            print(e)
        else:
            print("Товар добавлен")
        finally:
            print("Обработка товара завершена")



class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    def add_product(cls, product):
        pass


class MixinLog:
    """Класс миксинов"""

    def __repr__(self):
        attributes = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"Создан объект {self.__class__.__name__}({', '.join(attributes)})"


class Product(AbstractProduct, MixinLog):
    """Класс для товаров"""
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
        if self.__class__.__name__ == "Product":
            print(repr(self))

    def __str__(self):
        return f'{self.name}, {self._price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(self) == type(other):
            return (self._price * self.quantity) + (other._price * other.quantity)
        raise ValueError("Нельзя складывать товары из разных категорий")

    @classmethod
    def add_product(cls, product):
        pr = cls(**product)
        try:
            if pr.quantity > 0:
                for i in cls.__products:
                    if i.name == pr.name:
                        i.quantity += pr.quantity
                        i._price = max(i._price, pr._price)
                        return i
                cls.__products.append(pr)
                return pr
            raise ZeroProductQuantity()
        except ZeroProductQuantity as e:
            print(e)
        else:
            print("Товар добавлен")
        finally:
            print("Обработка товара завершена")

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


class Smartphone(Product, MixinLog):
    """Класс для смартфонов"""

    def __init__(self, name, description, price, quantity, productivity, model, storage, color):
        super().__init__(name, description, price, quantity)
        self.productivity = productivity
        self.model = model
        self.storage = storage
        self.color = color
        print(repr(self))


class Grass(Product, MixinLog):
    """Класс для травы"""

    def __init__(self, name, description, price, quantity, country_of_production, germination_time, color):
        super().__init__(name, description, price, quantity)
        self.country_of_production = country_of_production
        self.germination_time = germination_time
        self.color = color
        print(repr(self))


class ZeroProductQuantity(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Количество товара не может быть менее 1"

    def __str__(self):
        return self.message


class ProductIteration:
    """Класс для итерации по списку продуктов"""
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
