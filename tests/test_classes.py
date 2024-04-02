import pytest

from units.classes import Category, Product, ProductIteration, Smartphone, Grass, Order


@pytest.fixture()
def category_technics():
    return Category("Техника",
                    "Техника всякая разная",
                    [Product("Телевизор", "Фоновая подсветка", 123000.0, 7),
                     Product("Компьютер", "Компьютер мощный", 999000.0, 3)])


def test_category_init(category_technics):
    assert category_technics.name == "Техника"
    assert category_technics.description == "Техника всякая разная"
    assert category_technics.quantity_unique_products == 2

    assert category_technics.get_products == ['Телевизор, 123000.0 руб. Остаток: 7 шт.',
                                              'Компьютер, 999000.0 руб. Остаток: 3 шт.']
    assert len(category_technics) == 10
    assert str(category_technics) == 'Техника, количество продуктов: 10 шт.'


def test_category_add(category_technics):
    with pytest.raises(ValueError):
        category_technics.add_product("что то")

    assert category_technics.get_products == ['Телевизор, 123000.0 руб. Остаток: 7 шт.',
                                              'Компьютер, 999000.0 руб. Остаток: 3 шт.']

    category_technics.add_product(Product("Продукт", "какой то", 1234.0, 2))
    assert category_technics.get_products == ['Телевизор, 123000.0 руб. Остаток: 7 шт.',
                                              'Компьютер, 999000.0 руб. Остаток: 3 шт.',
                                              'Продукт, 1234.0 руб. Остаток: 2 шт.']

    category_technics.add_product(Smartphone("Смартфон", "Сусный", 45000.0,
                                             4, 3.3, "193JCX", 16, "Black"))
    assert category_technics.get_products == ['Телевизор, 123000.0 руб. Остаток: 7 шт.',
                                              'Компьютер, 999000.0 руб. Остаток: 3 шт.',
                                              'Продукт, 1234.0 руб. Остаток: 2 шт.',
                                              'Смартфон, 45000.0 руб. Остаток: 4 шт.']

    with pytest.raises(ValueError):
        category_technics.add_product("что то")

    assert category_technics.get_products == ['Телевизор, 123000.0 руб. Остаток: 7 шт.',
                                              'Компьютер, 999000.0 руб. Остаток: 3 шт.',
                                              'Продукт, 1234.0 руб. Остаток: 2 шт.',
                                              'Смартфон, 45000.0 руб. Остаток: 4 шт.']

    category_technics.add_product(Grass("Трава газонная", "Мягкая", 1499.99, 5,
                                        "Poland", "1 мес.", "Зеленая", ))

    assert category_technics.get_products == ['Телевизор, 123000.0 руб. Остаток: 7 шт.',
                                              'Компьютер, 999000.0 руб. Остаток: 3 шт.',
                                              'Продукт, 1234.0 руб. Остаток: 2 шт.',
                                              'Смартфон, 45000.0 руб. Остаток: 4 шт.',
                                              'Трава газонная, 1499.99 руб. Остаток: 5 шт.']

    assert repr(category_technics._products[2]) == ("Создан объект Product(name='Продукт', description='какой то', "
                                                    "_price=1234.0, quantity=2)")
    assert repr(category_technics._products[3]) == ("Создан объект Smartphone(name='Смартфон', description='Сусный', "
                                                    "_price=45000.0, quantity=4, productivity=3.3, model='193JCX', "
                                                    "storage=16, color='Black')")
    assert repr(category_technics._products[4]) == ("Создан объект Grass(name='Трава газонная', description='Мягкая', "
                                                    "_price=1499.99, quantity=5, country_of_production='Poland', "
                                                    "germination_time='1 мес.', color='Зеленая')")


def test_avg_price():
    category = Category("sus", "atata", [])
    assert category.avg_price() == 0


@pytest.fixture()
def product():
    return Product("Компьютер", "Игровой пк без видеокарты", 48990.0, 3)


def test_product_init(product):
    assert product.name == "Компьютер"
    assert product.description == "Игровой пк без видеокарты"
    assert product.price == 48990
    assert product.quantity == 3


def test_product_price_setter(product):
    product.price = 50000
    assert product.price == 50000

    product.price = -123
    assert product.price == 50000


def test_product_add_product(product):
    new_product = product.add_product({"name": "Наушники", "description": "Норм звук", "price": 1500.0, "quantity": 2})
    product.add_product({"name": "Наушники", "description": "Норм звук", "price": 1600.0, "quantity": 4})
    assert new_product.name == "Наушники"
    assert new_product.description == "Норм звук"
    assert new_product.price == 1600.0
    assert new_product.quantity == 6

    with pytest.raises(ValueError):
        product.add_product({"name": "Наушники", "description": "Норм звук", "price": 1600.0, "quantity": -4})


def test_order(product):
    my_order = Order(product, 3)
    assert my_order.product == product
    assert my_order.quantity == 3
    assert my_order.final_price == 146970.00


def test_product_add(product):
    product2 = Product("Телевизор", "Цветной", 15990.0, 5)
    assert product + product2 == 226920.0

    product3 = Smartphone("Телефон", "Работает", 15990.0, 5, 3.3, "19H-43J", 64, "Blue")
    with pytest.raises(ValueError):
        product + product3


@pytest.fixture()
def product_iteration():
    return ProductIteration(["Телефон", "Наушники", "Компьютер"])


def test_iteration_init(product_iteration):
    assert product_iteration.category == ["Телефон", "Наушники", "Компьютер"]
    product_list = [i for i in product_iteration]
    assert product_list == ["Телефон", "Наушники", "Компьютер"]
