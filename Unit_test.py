import unittest

from app import Recipe, RestaurantApp

class RestaurantAppTests(unittest.TestCase):
    def setUp(self):
        self.restaurant_app = RestaurantApp()

    def test_add_menu(self):
        self.restaurant_app.add_menu("Breakfast")
        self.assertTrue("Breakfast" in self.restaurant_app.menus)

    def test_add_duplicate_menu(self):
        self.restaurant_app.add_menu("Lunch")
        self.restaurant_app.add_menu("Lunch")
        self.assertEqual(len(self.restaurant_app.menus), 1)

    def test_add_recipe_to_existing_menu(self):
        recipe = Recipe("Pasta Carbonara", ["pasta", "bacon", "eggs", "cheese"], "Instructions for making Pasta Carbonara.")
        self.restaurant_app.add_menu("Dinner")
        self.restaurant_app.add_recipe_to_menu("Dinner", recipe)
        menu = self.restaurant_app.menus["Dinner"]
        self.assertEqual(len(menu.recipes), 1)
        self.assertEqual(menu.recipes[0].name, "Pasta Carbonara")

    def test_add_recipe_to_non_existing_menu(self):
        recipe = Recipe("Chicken Curry", ["chicken", "curry paste", "coconut milk"], "Instructions for making Chicken Curry.")
        self.restaurant_app.add_recipe_to_menu("Lunch", recipe)
        self.assertFalse("Lunch" in self.restaurant_app.menus)

    def test_sort_menu_by_recipe_name(self):
        recipe1 = Recipe("Pasta Carbonara", ["pasta", "bacon", "eggs", "cheese"], "Instructions for making Pasta Carbonara.")
        recipe2 = Recipe("Chicken Curry", ["chicken", "curry paste", "coconut milk"], "Instructions for making Chicken Curry.")
        self.restaurant_app.add_menu("Dinner")
        self.restaurant_app.add_recipe_to_menu("Dinner", recipe2)
        self.restaurant_app.add_recipe_to_menu("Dinner", recipe1)
        self.restaurant_app.sort_menu_by_recipe_name("Dinner")
        menu = self.restaurant_app.menus["Dinner"]
        self.assertEqual(menu.recipes[0].name, "Chicken Curry")
        self.assertEqual(menu.recipes[1].name, "Pasta Carbonara")

    def test_display_menu(self):
        recipe = Recipe("Salad", ["lettuce", "tomatoes", "cucumbers"], "Instructions for making Salad.")
        self.restaurant_app.add_menu("Lunch")
        self.restaurant_app.add_recipe_to_menu("Lunch", recipe)
        with self.assertLogs() as logs:
            self.restaurant_app.display_menu("Lunch")
            self.assertIn("Menu: Lunch", logs.output)
            self.assertIn("Recipe: Salad", logs.output)
            self.assertIn("Ingredients: ['lettuce', 'tomatoes', 'cucumbers']", logs.output)
            self.assertIn("Instructions: Instructions for making Salad.", logs.output)

if __name__ == '__main__':
    unittest.main()

