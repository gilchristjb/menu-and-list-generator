def mealSelector():
    """ This function randomly chooses a meal file for meal 1 and asigns the characheristics
    of that meal file to a list which can then be sliced returning the desired
    characteristics.
    """
    import os
    import ast
    import random

    #randomly chooses a meal from meallist and finds the file path
    meal_choice = str(random.choice(meallist()))
    meal_choice_path = str(os.getcwd() + '\\recipe_book\\' + meal_choice + '.txt')

    # reads all the lines from a mealfile and removes quotes
    with open(meal_choice_path,"r") as temp_TfEa:
        ZiOcMoczPu = temp_TfEa.readlines()
    ZiOcMoczPu = [NisnKjEEVb.strip() for NisnKjEEVb in ZiOcMoczPu]

    # asigns the appropriate characteristics to reasonable local variables
    # interprets the lists given in the meal file as actual lists
    faff_check = int(ZiOcMoczPu[4])
    pie_check = int(ZiOcMoczPu[6])
    main_carb = ZiOcMoczPu[8]
    meal_type = ZiOcMoczPu[10]
    meat_type = ZiOcMoczPu[12]
    ingredients = ast.literal_eval(ZiOcMoczPu[14])
    amounts = ast.literal_eval(ZiOcMoczPu[16])
    units = ast.literal_eval(ZiOcMoczPu[18])
    servings = ast.literal_eval(ZiOcMoczPu[2])
    additional_items = ast.literal_eval(ZiOcMoczPu[20])

    # lists the important characteristics of the randomly selected meal file
    return [meal_choice, ingredients, amounts, units, servings, faff_check, pie_check, main_carb, meal_type, meat_type, additional_items]