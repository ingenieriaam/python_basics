####################################################
# Recipe book administration
####################################################

from pathlib import Path
from os import system
import os
####################################################
## Functions
def dict_recipes_creation(rpath,recipes):
    for txt in Path(rpath).glob('**/*.txt'):
        category = Path(txt).parent.name
        recipe = Path(txt).stem
        if category not in recipes: recipes[category]={}
        recipes[category][recipe]=txt
    return recipes   

def select_category(recipes):
    for key in recipes.keys():
        print(f'{key}')

    cat = input('Enter a category (textual): \n>>> ')
    while cat not in recipes.keys():
        cat = input('Enter a category (textual): \n>>> ')
    return cat
def select_recipe(recipes,cat):
    for key in recipes[cat].keys():
        print(f'{key}')

    recipe = input('Enter a recipe (textual): \n>>> ')
    while recipe not in recipes[cat].keys():
        recipe = input('Enter a recipe (textual): \n>>> ')
    return recipe

def Read_a_recipe(recipes):
    cat = select_category(recipes)
    recipe = select_recipe(recipes,cat)

    print(f'\nRecipe file: {recipes[cat][recipe]}\n')
    file = open(recipes[cat][recipe])
    print(file.read() + '\n')
    file.close()
    
def Create_a_recipe(recipes,rpath):
    cat = select_category(recipes)
    recipe = input('Enter a new recipe name: \n>>> ')

    newpath= Path(rpath,cat,f'{recipe}.txt') 

    while newpath.exists():
        recipe = input('\nRecipe already exists. Select a different name.\n>>> ')
        newpath= Path(rpath,cat,f'{recipe}.txt')

    recipes[cat][recipe]=newpath

    file = open(newpath,'a')
    text = input('Enter the recipe text: \n>>> ')
    print(file.write(text))
    file.close()
    print('You have created a new recipe file!\n')
    
def Create_category(recipes):
    cat = input('Enter a new Category name: \n>>> ')

    newpath= Path(rpath,cat) 

    while newpath.exists():
        for key in recipes.keys():
            print(f'{key}')
        cat = input('\nRecipe already exists. Select a different name.\n>>> ')
        newpath= Path(rpath,cat)

    path = os.makedirs(newpath)
    recipes[cat]=newpath
    print('You have created a new category directory!\n')

def Delete_a_recipe(recipes):
    cat = select_category(recipes)
    recipe = select_recipe(recipes,cat)
    while not os.path.exists(recipes[cat][recipe]):
        print('File does not exist!\n')
        cat = select_category(recipes)
        recipe = select_recipe(recipes,cat)

    os.remove(recipes[cat][recipe])
    print('You have deleted the recipe!\n')
def Delete_category(recipes):
    cat = select_category(recipes)
    folder = Path(rpath,cat)
    while not folder.exists():
        print('Category does not exist!\n')
        cat = select_category(recipes)
    
    os.rmdir(folder)
    print('You have deleted the category directory!\n')
    
def case6_func():
    pass
####################################################
## Welcome message
print('Welcome to the Recipe book administration')

rpath = Path(os.getcwd(),'Recetas')
print(f'The recipe book path is: {rpath}')

rcount = 0
for txt in Path(rpath).glob('**/*.txt'):
    rcount += 1
print(f'This book contains {rcount} recipes')
recipes = {}

####################################################
## Main loop
recipes=dict_recipes_creation(rpath,recipes)
op = 0
op_dic = {
    1: 'Read a recipe'   ,
    2: 'Create a recipe' ,
    3: 'Create category' ,
    4: 'Delete a recipe' ,
    5: 'Delete category' ,
    6: 'Exit the program'
}
while op != '6':
    if "posix" in os.name:
        system(f"clear")
    else:
        system(f"cls")
    for key, value in op_dic.items():
        print(f'{key}: {value}')
    op = input('What do you want to do? \n>>> ')
    match op:
        case '1':
            Read_a_recipe(recipes)
        case '2':
            Create_a_recipe(recipes,rpath)
        case '3':
            Create_category(recipes)
        case '4':
            Delete_a_recipe(recipes)
        case '5':
            Delete_category(recipes)
        case '6':
            print('See you next time')
            break
    input('\nPress any key to continue...')