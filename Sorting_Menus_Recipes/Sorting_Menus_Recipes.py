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

def main():
    restaurant = RestaurantApp()

    while True:
        print("\n1. Add Menu")
        print("2. Remove Menu")
        print("3. Add Recipe to Menu")
        print("4. Update Recipe in Menu")
        print("5. Remove Recipe from Menu")
        print("6. Exit")
        new_varnew_var = choice = new_func()
        

        if choice == 1:
            menu_name = input("Enter the name of the menu: ")
            restaurant.add_menu(menu_name)
            print(f"Menu '{menu_name}' added successfully!")

        elif choice == 2:
            menu_name = input("Enter the name of the menu: ")
            restaurant.remove_menu(menu_name)
            print(f"Menu '{menu_name}' removed successfully!")

        elif choice == 3:
           
            recipe_name = input("Enter the name of the recipe: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            instructions = input("Enter the recipe instructions: ")
            recipe = Recipe(recipe_name, ingredients, instructions)
            restaurant.add_recipe_to_menu(menu_name, recipe)
            print(f"Recipe '{recipe_name}' added to menu '{menu_name}' successfully!")

        elif choice == 4:
            menu_name = input("Enter the name of the menu: ")
            old_recipe_name = input("Enter the name of the recipe to update: ")
            ingredients = input("Enter new ingredients (comma-separated): ").split(",")
            instructions = input("Enter the new recipe instructions: ")
            new_recipe = Recipe(old_recipe_name, ingredients, instructions)
            restaurant.update_recipe_in_menu(menu_name, old_recipe_name, new_recipe)
            print(f"Recipe '{old_recipe_name}' updated in menu '{menu_name}' successfully!")

        elif choice == 5:
            menu_name = input("Enter the name of the menu: ")
            recipe_name = input("Enter the name of the recipe to remove: ")
            restaurant.remove_recipe_from_menu(menu_name, recipe_name)
            print(f"Recipe '{recipe_name}' removed from menu '{menu_name}' successfully!")

        elif choice == 6:
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

def new_func():
    choice = int(input("Enter your choice: "))
    return choice

if __name__ == "__main__":
    main()
