import sys

import pytest

from units.classes import Category, Product


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


@pytest.fixture()
def product():
    return Product("Компьютер", "Игровой пк без видеокарты", 48990, 3)


def test_product_init(product):
    assert product.name == "Компьютер"
    assert product.description == "Игровой пк без видеокарты"
    assert product.price == 48990
    assert product.quantity == 3

    product.price = 50000
    assert product.price == 50000

    product.price = -123
    assert product.price == 50000

    assert product.add_product(
        {"name": "Наушники", "description": "Норм звук", "price": 1500.0, "quantity": 2}).name == "Наушники"
    assert product.add_product(
        {"name": "Наушники", "description": "Норм звук", "price": 1500.0, "quantity": 3}).description == "Норм звук"
    assert product.add_product(
        {"name": "Наушники", "description": "Норм звук", "price": 1500.0, "quantity": 4}).price == 1500.0
    assert product.add_product(
        {"name": "Наушники", "description": "Норм звук", "price": 1500.0, "quantity": 2}).quantity == 11
