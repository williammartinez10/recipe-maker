
# Phase 1

# 1. Prompt user for input of ingredients available
# 2. ask user what they'd like to make (from options)
# 3a. If sufficient ingredients remain, subtract ingredients used, and present remaining amount. Go to step 2
# 3b. Otherwise, tell the user they don't have enough ingredients, go to step 2.

# THE FOLLOWING LIST CONTAINS THE UNITS OF THE INGREDIENTS
units = ['cups', 'tablespoons', '', 'cups', 'teaspoons', 'teaspoons', 'slices', '', '', '']

# THE FOLLOWING LIST CONTAINS THE NAMES OF THE INGREDIENTS
ingredients = ['flour', 'sugar', 'eggs', 'milk', 'cinnamon', 'baking powder', 'bread', 'bananas', 'apples', 'peaches']

# THE FOLLOWING LIST WILL BE USED TO SAVE THE INGREDIENTS
pantry = []


# THE FOLLOWING ARE EXAMPLES OF RECIPES - OBSERVE THE ORDER OF THE INGREDIENTS IS THE SAME AS THE ORDER OF THE PANTRY

# banana pancakes require 1 cup of flour, 2 tablespoons sugar, 1 egg, 1 cup of milk, 3 teaspoons cinnamon,
# 2 teaspoon baking powder, 0 bread, 2 bananas
banana_pancake_recipe = [1, 2, 1, 1, 3, 2, 0, 2, 0, 0]

# peach crepes require 1 cup of flour, 0 tablespoons sugar, 1 egg, 1 cup of milk, 2 teaspoons cinnamon,
# 0 teaspoon baking powder, 0 bread, 0 bananas, 0 apples, 3 peaches
peach_crepe_recipe = [1, 0, 1, 1, 2, 0, 0, 0, 0, 3]

# apple pie requires 2 cups of flour, 4 tablespoons sugar, 2 eggs, 0.5 cup milk, 1 teaspoon cinnamon,
# 1 teaspoon baking powder, 0 bread, 0 banana, 5 apples, 0 peaches
apple_pie_recipe = [2, 4, 2, 0.5, 1, 1, 0, 0, 5, 0]

# french_toast_recipe requires 0.5 cups of flour, 3 tablespoons sugar, 3 eggs, 0.5 cup milk, 2 teaspoon cinnamon,
# 0 teaspoon baking powder, 8 bread, 0 banana, 0 apples, 0 peaches
french_toast_recipe = [0.5, 3, 3, 0.5, 2, 0, 8, 0, 0, 0]

# scrambled_eggs requires 0 cups of flour, 0 tablespoons sugar, 4 eggs, 0.5 cup milk, 0 teaspoon cinnamon,
# 0 teaspoon baking powder, 2 bread, 0 banana, 0.5 apples, 1 peaches
scrambled_eggs = [0, 0, 4, 0.5, 0, 0, 2, 0, 0.5, 1]

menu = [banana_pancake_recipe, peach_crepe_recipe, apple_pie_recipe, french_toast_recipe, scrambled_eggs]
menu_list = ["banana pancake", "peach crepe", "apple pie", "french toast", "scrambled eggs with toast and fruits"]


# The following function allows to enter the ingredients
def pantry_ingredients(units, ingredients):
    for i in range(len(units)):
        unit = units[i]
        if unit:
            unit += ' of '
        ingredient = ingredients[i]
        item = input(f'How many {unit}{ingredient} do you have? ')
        pantry.append(int(item))


# Allows to print the content of the pantry
def show_pantry(): # Shows the ingredients of an existing pantry
    for realNumber in range(len(pantry)):
        unit = units[realNumber]
        if unit:
            unit += ' of '
        ingredient = ingredients[realNumber]
        print(f'{pantry[realNumber]} {unit}{ingredient}')



# This function does not need to be modified for Phase 1
def recipe_menu():
    global i
    print("What would you like to cook? Here's the recipe book:")
    for i in range(len(menu_list)):
        print("   ",i + 1, ". ", menu_list[i], sep="")

    print("   ", i + 2, ". Nevermind, I don't want to cook anything (Exit).", sep="")
    print(" ")
    option = int(input("Select an option by typing its number here: "))
    return option



# Verify if the option is valid. If it is, get the recipe from the list menu using the list index, and return the recipe
# If option is 6 terminate the program. If the option is not valid keep asking the user to enter a valid option while
# showing the recipe menu
def valid_option(option):
    while option not in range(1, 7):
        print("Sorry, your selection is invalid. Please enter a valid option (From 1 to 6).")
        option = recipe_menu()
    if option > 0 or option < 6:
        print("Congratulations, you have selected a valid number.")
    if option == 6:
        return option
    else:
        return menu[option - 1]



# Verify if there are enough ingredients in the pantry
# To cook the selected recipe, use subtraction of the pantry and recipe lists
# If there is not enough element show a message that indicate there are not enough ingredients
# If there is enough ingredients then show a happy message and update the pantry
# hint: you can replace the pantry with a new pantry

def pantry_update(recipe):
    x = False
    for i in range(len(pantry)):
        if pantry[i] < recipe[i]:
            x = True
            print("Sorry, you don't have enough ingredients for this recipe")
            break
    if x == False:
        print("You can cook this recipe!")
        for x in range(len(pantry)):
            pantry[x] -= recipe[x]
    return pantry




# 1. Prompt user for input of ingredients available
pantry_ingredients(units, ingredients)
cook = True
while cook:
    # 2. ask user what they'd like to make (from options)-COMMENT
    option = recipe_menu()
    print(f'You selected option {option}')
    # call the corresponding function to verify the selected option is valid-COMMENT
    recipe = valid_option(option)
    if recipe == 6:
        print("Thank you for your visit. Hope to see you soon!")
        break
    # if the option is valid and want to cook (different to 6)-COMMENT
    pantry_update(recipe)
    # 3a. If sufficient ingredients remain, subtract ingredients used, and present remaining amount. Go to step 2
    # ingredients = ['flour', 'sugar', 'eggs', 'milk', 'cinnamon', 'baking powder', 'bread', 'bananas', 'apples', 'peaches']
    print("Here's what's left in the pantry: ")
    show_pantry()