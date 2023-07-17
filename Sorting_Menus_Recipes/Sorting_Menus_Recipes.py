class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.image = None 

    def add_image(self, image_url):
        self.image = image_url
class Menu:
    def __init__(self, name):
        self.name = name
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe_name):
        self.recipes = [recipe for recipe in self.recipes if recipe.name != recipe_name]

class RestaurantApp:
    def __init__(self):
        self.menus = {}
        self.recipes_hash = {}

    def add_menu(self, menu_name):
        if menu_name not in self.menus:
            self.menus[menu_name] = []

    def remove_menu(self, menu_name):
        if menu_name in self.menus:
            del self.menus[menu_name]

    def add_recipe_to_menu(self, menu_name, recipe):
        if menu_name in self.menus:
            self.menus[menu_name].append(recipe)
            self.recipes_hash[recipe.name] = recipe

    def update_recipe_in_menu(self, menu_name, old_recipe_name, new_recipe):
        if menu_name in self.menus:
            for i, recipe in enumerate(self.menus[menu_name]):
                if recipe.name == old_recipe_name:
                    recipe.name = new_recipe.name
                    recipe.ingredients = new_recipe.ingredients
                    recipe.instructions = new_recipe.instructions
                    recipe.image = new_recipe.image
                    self.menus[menu_name][i] = new_recipe
                    self.recipes_hash[new_recipe.name] = new_recipe
                    
                    break

    def remove_recipe_from_menu(self, menu_name, recipe_name):
        if menu_name in self.menus:
            self.menus[menu_name] = [recipe for recipe in self.menus[menu_name] if recipe.name != recipe_name]
            
            if recipe_name in self.recipes_hash:
                del self.recipes_hash[recipe_name]

                def get_recipe_by_name(self, recipe_name):
                    return self.recipes_hash.get(recipe_name, None)

class RestaurantView:
    @staticmethod
    def display_menus_and_recipes(app):
        print("\nMenus and Recipes:")
        for menu_name, recipes in app.menus.items():
            print(f"\nMenu: {menu_name}")
            for recipe in recipes:
                print(f"Recipe: {recipe.name}")
                print(f"Ingredients: {', '.join(recipe.ingredients)}")
                print(f"Instructions: {recipe.instructions}")
                print(f"Image URL: {recipe.image}" if recipe.image else "No image available")
                print()


def main():
    restaurant = RestaurantApp()

    while True:
        print("\n1. Add Menu")
        print("2. Remove Menu")
        print("3. Add Recipe to Menu")
        print("4. Update Recipe in Menu")
        print("5. Remove Recipe from Menu")
        print("6. View Menus and Recipes")
        print("7. Exit")

        choice = new_func()

        if choice == 1:
            menu_name = input("Enter the name of the menu: ")
            restaurant.add_menu(menu_name)
            print(f"Menu '{menu_name}' added successfully!")

        elif choice == 2:
            menu_name = input("Enter the name of the menu: ")
            restaurant.remove_menu(menu_name)
            print(f"Menu '{menu_name}' removed successfully!")

        elif choice == 3:
            menu_name = input("Enter the name of the menu: ")
            recipe_name = input("Enter the name of the recipe: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            instructions = input("Enter the recipe instructions: ")
            image_url = input("Enter the image URL for the recipe (leave blank if none): ")
            recipe = Recipe(recipe_name, ingredients, instructions)
            if image_url:
                recipe.add_image(image_url)
            restaurant.add_recipe_to_menu(menu_name, recipe)
            print(f"Recipe '{recipe_name}' added to menu '{menu_name}' successfully!")

        elif choice == 4:
            menu_name = input("Enter the name of the menu: ")
            old_recipe_name = input("Enter the name of the recipe to update: ")
            ingredients = input("Enter new ingredients (comma-separated): ").split(",")
            instructions = input("Enter the new recipe instructions: ")
            image_url = input("Enter the new image URL for the recipe (leave blank if none): ")
            new_recipe = Recipe(old_recipe_name, ingredients, instructions)
            if image_url:
                new_recipe.add_image(image_url)
            restaurant.update_recipe_in_menu(menu_name, old_recipe_name, new_recipe)
            print(f"Recipe '{old_recipe_name}' updated in menu '{menu_name}' successfully!")

        elif choice == 5:
            menu_name = input("Enter the name of the menu: ")
            recipe_name = input("Enter the name of the recipe to remove: ")
            restaurant.remove_recipe_from_menu(menu_name, recipe_name)
            print(f"Recipe '{recipe_name}' removed from menu '{menu_name}' successfully!")

        elif choice == 6:
            RestaurantView.display_menus_and_recipes(restaurant)

        elif choice == 7:
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

def new_func():
    choice = int(input("Enter your choice: "))
    return choice

if __name__ == "__main__":
    main()
