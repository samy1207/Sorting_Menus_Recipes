import unittest

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RestaurantApp:
    def __init__(self):
        self.menus = {}  # A dictionary to store menus, where keys are menu names and values are lists of recipes.

    def add_menu(self, menu_name):
        if menu_name not in self.menus:
            self.menus[menu_name] = []

    def remove_menu(self, menu_name):
        if menu_name in self.menus:
            del self.menus[menu_name]

    def add_recipe_to_menu(self, menu_name, recipe):
        if menu_name in self.menus:
            self.menus[menu_name].append(recipe)

    def update_recipe_in_menu(self, menu_name, old_recipe_name, new_recipe):
        if menu_name in self.menus:
            for recipe in self.menus[menu_name]:
                if recipe.name == old_recipe_name:
                    recipe.name = new_recipe.name
                    recipe.ingredients = new_recipe.ingredients
                    recipe.instructions = new_recipe.instructions
                    break

    def remove_recipe_from_menu(self, menu_name, recipe_name):
        if menu_name in self.menus:
            self.menus[menu_name] = [recipe for recipe in self.menus[menu_name] if recipe.name != recipe_name]

class TestRestaurantApp(unittest.TestCase):
    def setUp(self):
        self.restaurant = RestaurantApp()
        self.recipe1 = Recipe("Pasta Carbonara", ["pasta", "bacon", "eggs", "cheese"], "Instructions for making Pasta Carbonara.")
        self.recipe2 = Recipe("Chicken Curry", ["chicken", "curry paste", "coconut milk"], "Instructions for making Chicken Curry.")
        self.recipe3 = Recipe("Salad", ["lettuce", "tomatoes", "cucumbers"], "Instructions for making Salad.")

    def test_add_menu(self):
        self.restaurant.add_menu("Main Menu")
        self.assertIn("Main Menu", self.restaurant.menus)

    def test_remove_menu(self):
        self.restaurant.add_menu("Main Menu")
        self.restaurant.remove_menu("Main Menu")
        self.assertNotIn("Main Menu", self.restaurant.menus)

    def test_add_recipe_to_menu(self):
        self.restaurant.add_menu("Main Menu")
        self.restaurant.add_recipe_to_menu("Main Menu", self.recipe1)
        self.assertIn(self.recipe1, self.restaurant.menus["Main Menu"])

    def test_update_recipe_in_menu(self):
        self.restaurant.add_menu("Main Menu")
        self.restaurant.add_recipe_to_menu("Main Menu", self.recipe1)
        updated_recipe = Recipe("Updated Pasta Carbonara", ["pasta", "bacon", "eggs", "cheese", "pepper"], "Updated instructions for making Pasta Carbonara.")
        self.restaurant.update_recipe_in_menu("Main Menu", "Pasta Carbonara", updated_recipe)
        self.assertIn(updated_recipe, self.restaurant.menus["Main Menu"])
        self.assertNotIn(self.recipe1, self.restaurant.menus["Main Menu"])

    def test_remove_recipe_from_menu(self):
        self.restaurant.add_menu("Main Menu")
        self.restaurant.add_recipe_to_menu("Main Menu", self.recipe1)
        self.restaurant.add_recipe_to_menu("Main Menu", self.recipe2)
        self.restaurant.remove_recipe_from_menu("Main Menu", "Pasta Carbonara")
        self.assertNotIn(self.recipe1, self.restaurant.menus["Main Menu"])
        self.assertIn(self.recipe2, self.restaurant.menus["Main Menu"])

if __name__ == "__main__":
    unittest.main()
