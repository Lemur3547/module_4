import pytest

from units.classes import Category, Product, ProductIteration


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


def test_product_add(product):
    product2 = Product("Телефон", "Работает", 15990.0, 5)
    assert product + product2 == 226920.0


@pytest.fixture()
def product_iteration():
    return ProductIteration(["Телефон", "Наушники", "Компьютер"])


def test_iteration_init(product_iteration):
    assert product_iteration.category == ["Телефон", "Наушники", "Компьютер"]
    product_list = [i for i in product_iteration]
    assert product_list == ["Телефон", "Наушники", "Компьютер"]
