from bun import Bun
from ingredient import Ingredient


class Burger:
    def __init__(self):
        self.bun = None
        self.ingredients = []

    def set_buns(self, bun):
        self.bun = bun

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index):
        del self.ingredients[index]

    def move_ingredient(self, old_index, new_index):
        self.ingredients.insert(new_index, self.ingredients.pop(old_index))

    def get_price(self):
        price = 0
        if self.bun:
            price += self.bun.get_price() * 2
        for ingredient in self.ingredients:
            price += ingredient.get_price()
        return price

    def get_ingredient_count(self):
        return len(self.ingredients)

    def get_receipt(self):
        receipt = f"(==== {self.bun.get_name()} ====)\n"
        for ingredient in self.ingredients:
            receipt += f"= {ingredient.get_type()} {ingredient.get_name()} =\n"
        receipt += f"(==== {self.bun.get_name()} ====)\n"
        receipt += f"\nPrice: {self.get_price()}"
        return receipt