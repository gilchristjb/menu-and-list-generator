def lineprint_m1():
    """ This function randomly chooses a meal file for meal 1 and asigns the characheristics
    of that meal file to a list which can then be sliced returning the desired
    characteristic.
    """

    import os
    import ast
    import random
    from meallist_win import meallist

    # randomly chooses a meal from meallist and finds the file path
    meal_list = meallist()
    meal_choice_m1 = str(random.choice(meal_list))
    meal_choice_path = str(os.getcwd() + '\\recipe_book\\' + meal_choice_m1 + '.txt')

    # reads all the files from a mealfile and removes quotes
    with open(meal_choice_path,"r") as rcGifEWQPI:
        ZiOcMoczPu = rcGifEWQPI.readlines()
    ZiOcMoczPu = [NisnKjEEVb.strip() for NisnKjEEVb in ZiOcMoczPu]

    # asigns the appropriate characteristics to reasonable local variables
    # interprets the lists given in the meal file as actual lists
    faff_check_m1 = int(ZiOcMoczPu[4])
    pie_check_m1 = ZiOcMoczPu[6]
    main_carb_m1 = ZiOcMoczPu[8]
    meal_type_m1 = ZiOcMoczPu[10]
    meat_type_m1 = ZiOcMoczPu[12]
    ingredients_m1 = ast.literal_eval(ZiOcMoczPu[14])
    amounts_m1 = ast.literal_eval(ZiOcMoczPu[16])
    units_m1 = ast.literal_eval(ZiOcMoczPu[18])
    servings_m1 = ast.literal_eval(ZiOcMoczPu[2])
    additional_items_m1 = ast.literal_eval(ZiOcMoczPu[20])

    # lists the important characteristics of the randomly selected meal file
    return [meal_choice_m1, ingredients_m1, amounts_m1, units_m1, servings_m1, faff_check_m1, pie_check_m1, main_carb_m1, meal_type_m1, meat_type_m1, additional_items_m1]

def lineprint_m2():
    """ This function randomly chooses a meal file for meal 2 and asigns the characheristics
    of that meal file to a list which can then be sliced returning the desired
    characteristic.
    """

    import os
    import ast
    import random
    from meallist_win import meallist

    # randomly chooses a meal from meallist and finds the file path
    meal_list = meallist()
    meal_choice_m2 = str(random.choice(meal_list))
    meal_choice_path = str(os.getcwd() + '\\recipe_book\\' + meal_choice_m2 + '.txt')

    # reads all the files from a mealfile and removes quotes
    with open(meal_choice_path,"r") as rcGifEWQPI:
        ZiOcMoczPu = rcGifEWQPI.readlines()
    ZiOcMoczPu = [NisnKjEEVb.strip() for NisnKjEEVb in ZiOcMoczPu]

    # asigns the appropriate characteristics to reasonable local variables
    # interprets the lists given in the meal file as actual lists
    faff_check_m2 = int(ZiOcMoczPu[4])
    pie_check_m2 = ZiOcMoczPu[6]
    main_carb_m2 = ZiOcMoczPu[8]
    meal_type_m2 = ZiOcMoczPu[10]
    meat_type_m2 = ZiOcMoczPu[12]
    ingredients_m2 = ast.literal_eval(ZiOcMoczPu[14])
    amounts_m2 = ast.literal_eval(ZiOcMoczPu[16])
    units_m2 = ast.literal_eval(ZiOcMoczPu[18])
    servings_m2 = ast.literal_eval(ZiOcMoczPu[2])
    additional_items_m2 = ast.literal_eval(ZiOcMoczPu[20])

    # lists the important characteristics of the randomly selected meal file
    return [meal_choice_m2, ingredients_m2, amounts_m2, units_m2, servings_m2, faff_check_m2, pie_check_m2, main_carb_m2, meal_type_m2, meat_type_m2, additional_items_m2]

def lineprint_m3():
    """ This function randomly chooses a meal file for meal 3 and asigns the characheristics
    of that meal file to a list which can then be sliced returning the desired
    characteristic.
    """
    import os
    import ast
    import random
    from meallist_win import meallist

    # randomly chooses a meal from meallist and finds the file path
    meal_list = meallist()
    meal_choice_m3 = str(random.choice(meal_list))
    meal_choice_path = str(os.getcwd() + '\\recipe_book\\' + meal_choice_m3 + '.txt')

    # reads all the files from a mealfile and removes quotes
    with open(meal_choice_path,"r") as rcGifEWQPI:
        ZiOcMoczPu = rcGifEWQPI.readlines()
    ZiOcMoczPu = [NisnKjEEVb.strip() for NisnKjEEVb in ZiOcMoczPu]

    # asigns the appropriate characteristics to reasonable local variables
    # interprets the lists given in the meal file as actual lists
    faff_check_m3 = int(ZiOcMoczPu[4])
    pie_check_m3 = ZiOcMoczPu[6]
    main_carb_m3 = ZiOcMoczPu[8]
    meal_type_m3 = ZiOcMoczPu[10]
    meat_type_m3 = ZiOcMoczPu[12]
    ingredients_m3 = ast.literal_eval(ZiOcMoczPu[14])
    amounts_m3 = ast.literal_eval(ZiOcMoczPu[16])
    units_m3 = ast.literal_eval(ZiOcMoczPu[18])
    servings_m3 = ast.literal_eval(ZiOcMoczPu[2])
    additional_items_m3 = ast.literal_eval(ZiOcMoczPu[20])

    # lists the important characteristics of the randomly selected meal file
    return [meal_choice_m3, ingredients_m3, amounts_m3, units_m3, servings_m3, faff_check_m3, pie_check_m3, main_carb_m3, meal_type_m3, meat_type_m3, additional_items_m3]

def lineprint_m4():
    """ This function randomly chooses a meal file for meal 4 and asigns the characheristics
    of that meal file to a list which can then be sliced returning the desired
    characteristic.
    """

    import os
    import ast
    import random
    from meallist_win import meallist

    # randomly chooses a meal from meallist and finds the file path
    meal_list = meallist()
    meal_choice_m4 = str(random.choice(meal_list))
    meal_choice_path = str(os.getcwd() + '\\recipe_book\\' + meal_choice_m4 + '.txt')

    # reads all the files from a mealfile and removes quotes
    with open(meal_choice_path,"r") as rcGifEWQPI:
        ZiOcMoczPu = rcGifEWQPI.readlines()
    ZiOcMoczPu = [NisnKjEEVb.strip() for NisnKjEEVb in ZiOcMoczPu]

    # asigns the appropriate characteristics to reasonable local variables
    # interprets the lists given in the meal file as actual lists
    faff_check_m4 = int(ZiOcMoczPu[4])
    pie_check_m4 = ZiOcMoczPu[6]
    main_carb_m4 = ZiOcMoczPu[8]
    meal_type_m4 = ZiOcMoczPu[10]
    meat_type_m4 = ZiOcMoczPu[12]
    ingredients_m4 = ast.literal_eval(ZiOcMoczPu[14])
    amounts_m4 = ast.literal_eval(ZiOcMoczPu[16])
    units_m4 = ast.literal_eval(ZiOcMoczPu[18])
    servings_m4 = ast.literal_eval(ZiOcMoczPu[2])
    additional_items_m4 = ast.literal_eval(ZiOcMoczPu[20])

    # lists the important characteristics of the randomly selected meal file
    return [meal_choice_m4, ingredients_m4, amounts_m4, units_m4, servings_m4, faff_check_m4, pie_check_m4, main_carb_m4, meal_type_m4, meat_type_m4, additional_items_m4]
