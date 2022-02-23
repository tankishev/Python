# Create a class called PizzaDelivery. Upon initialization, it should receive a name (string), a price (float),
# and ingredients (dictionary). The class should also have an instance attribute ordered set to False by default.
# You should also create 3 additional instance methods:
# -	add_extra(ingredient: str, quantity: int, price_per_quantity: float):
# o	If we already have this ingredient in our pizza, increase the ingredient quantity with the given one and update
# the pizza price by adding the ingredient price for the given quantity
# o	If we do not have this ingredient in our pizza, we should add it and update the pizza price
# -	remove_ingredient(ingredient: str, quantity: int, price_per_quantity: float):
# o	If we do not have this ingredient in our pizza, we should return the following message "Wrong ingredient selected!
# We do not use {ingredient} in {pizza_name}!"
# o	If we have the ingredient, but we try to remove more than we have available, we should return the following message
# "Please check again the desired quantity of {ingredient}!"
# o	Otherwise, remove the given quantity of the ingredient and update the pizza price by removing the ingredient price
# for the given quantity
#
# -	make_order()
# o	Set the attribute ordered to True and return the following message
# "You've ordered pizza {pizza_name} prepared with {ingredient: quantity} and the price will be {price}lv.".
# The ingredients should be separated by a comma and a space ", "
# o	Keep in mind that once the pizza is ordered, no further changes are allowed. We should return the following message
# if the customer tries to change it: "Pizza {name} already prepared, and we can't make any changes!"


class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients  # {name: quantity}
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> str:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        else:
            self.price += quantity * price_per_quantity
            if ingredient in self.ingredients.keys():
                self.ingredients[ingredient] += quantity
            else:
                self.ingredients.update({ingredient: quantity})

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> str:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        else:
            current_qty = self.ingredients.get(ingredient)
            if not current_qty:
                return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
            elif current_qty < quantity:
                return f'Please check again the desired quantity of {ingredient}!'
            else:
                self.price -= quantity * price_per_quantity
                self.ingredients[ingredient] -= quantity

    def make_order(self) -> str:
        self.ordered = True
        print_ingredients = ', '.join([f'{k}: {v}' for k, v in self.ingredients.items()])
        return f"You've ordered pizza {self.name} prepared with {print_ingredients} " \
               f"and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
