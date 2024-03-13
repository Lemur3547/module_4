import pytest

from units.classes import Category, Product


@pytest.fixture()
def category_technics():
    return Category("Техника", "Техника всякая разная", ["Телевизор", "Компьютер", "Телефон", "Микроволновка"])


def test_category_init(category_technics):
    assert category_technics.name == "Техника"
    assert category_technics.description == "Техника всякая разная"
    assert category_technics.products == ["Телевизор", "Компьютер", "Телефон", "Микроволновка"]
    assert category_technics.quantity_unique_products == 4


@pytest.fixture()
def product():
    return Product("Компьютер", "Игровой пк без видеокарты", 48990, 3)


def test_product_init(product):
    assert product.name == "Компьютер"
    assert product.description == "Игровой пк без видеокарты"
    assert product.price == 48990
    assert product.quantity == 3
