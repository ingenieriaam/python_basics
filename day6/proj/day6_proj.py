####################################################
# Recipe book administration
####################################################

from pathlib import Path
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

def case1_func(recipes):
    cat = select_category(recipes)
    recipe = select_recipe(recipes,cat)

    print(f'\nRecipe file: {recipes[cat][recipe]}\n')
    file = open(recipes[cat][recipe])
    print(file.read() + '\n')
    file.close()
    
def case2_func(recipes,rpath):
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
    print('You have created a new recipe file!')
    
def case3_func(recipes):
    cat = input('Enter a new Category name: \n>>> ')

    newpath= Path(rpath,cat) 

    while newpath.exists():
        for key in recipes.keys():
            print(f'{key}')
        cat = input('\nRecipe already exists. Select a different name.\n>>> ')
        newpath= Path(rpath,cat)

    path = os.makedirs(newpath)
    recipes[cat]=newpath
    print('You have created a new category directory!')

def case4_func(recipes):
    pass
def case5_func(recipes):
    pass
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
    for key, value in op_dic.items():
        print(f'{key}: {value}')
    op = input('What do you want to do? \n>>> ')
    match op:
        case '1':
            case1_func(recipes)
        case '2':
            case2_func(recipes,rpath)
        case '3':
            case3_func(recipes)
        case '4':
            case4_func(recipes)
        case '5':
            case5_func(recipes)
        case '6':
            print('See you next time')
            break