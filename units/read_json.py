import json

from units.classes import Category, Product


def read_json():
    with open('products.json', 'rt', encoding='utf-8') as file:
        products = json.loads(file.read())
        categories = []
        for category in products:
            categories.append(Category(category["name"], category["description"], [
                Product(product["name"], product["description"], product["price"], product["quantity"]) for product in
                category['products']]))
    return categories
