
# Phase 2

# CONSTANTS
units = ['cups', 'tablespoons', '', 'cups', 'teaspoons', 'teaspoons', 'slices', '', '', '']
ingredients = ['flour', 'sugar', 'eggs', 'milk', 'cinnamon', 'baking powder', 'bread', 'bananas', 'apples', 'peaches']

pantry = []

banana_pancake_recipe = [1, 2, 1, 1, 3, 2, 0, 2, 0, 0]
peach_crepe_recipe = [1, 0, 1, 1, 2, 0, 0, 0, 0, 3]
apple_pie_recipe = [2, 4, 2, 0.5, 1, 1, 0, 0, 5, 0]
french_toast_recipe = [0.5, 3, 3, 0.5, 2, 0, 8, 0, 0, 0]
scrambled_eggs = [0, 0, 4, 0.5, 0, 0, 2, 0, 0.5, 1]

menu = [banana_pancake_recipe, peach_crepe_recipe, apple_pie_recipe, french_toast_recipe, scrambled_eggs]
menu_list = ["banana pancake", "peach crepe", "apple pie", "french toast", "scrambled eggs with toast and fruits"]


def pantry_ingredients(units, ingredients):
    for i in range(len(units)):
        unit = units[i]
        if unit:
            unit += ' of '
        ingredient = ingredients[i]
        item = input(f'How many {unit}{ingredient} do you have? ')
        pantry.append(int(item))


# ADD INGREDIENTS WHEN THERE AREN'T SUFFICIENT
def add_ingredients(units, ingredients):
    for i in range(len(units)):
        unit = units[i]
        if unit:
            unit += ' of '
        ingredient = ingredients[i]
        pantry[i] += int(input(f'How many {unit}{ingredient} do you want to add?: '))


def show_pantry():
    for realNumber in range(len(pantry)):
        unit = units[realNumber]
        if unit:
            unit += ' of '
        ingredient = ingredients[realNumber]
        print(f'{pantry[realNumber]} {unit}{ingredient}')


def recipe_menu():
    print("What would you like to cook? Here's the recipe book:")
    for i in range(len(menu_list)):
        print("   ", i + 1, ". ", menu_list[i], sep="")

    print("   ", i + 2, ". Nevermind, I don't want to cook anything (Exit).", sep="")
    print(" ")
    option = int(input("Select an option by typing its number here: "))
    return option


def valid_option(option):
    while option not in range(1, 7):
        print("Invalid. Please enter a valid option.")
        option = recipe_menu()
    if option > 0 or option < 6:
        print("Yay! You selected a valid number.")
    if option == 6:
        return option
    else:
        return menu[option - 1]


# The pantry can be replaced with a new pantry
def pantry_update(recipe):
    for i in range(len(pantry)):
        if pantry[i] < recipe[i]:
            print("You don't have enough ingredients for this recipe")
            addmore = input("Do you want to add? (yes/no): ")
            if addmore == "yes":
                add_ingredients(units, ingredients)

                return

    for i in range(len(pantry)):
        pantry[i] -= recipe[i]


def start():
    pantry_ingredients(units, ingredients)
    cook = True
    while cook:
        option = recipe_menu()
        print(f'You selected option {option}')
        recipe = valid_option(option)
        if recipe == 6:
            print("Thank you for your visit. Hope to see you soon!")
            break
        pantry_update(recipe)

        print("Here's what's left in the pantry: ")
        show_pantry()


start()