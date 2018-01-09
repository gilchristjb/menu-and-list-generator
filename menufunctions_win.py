def newmeal():
    """This function checks to see if there is a directory called 'recipe_book
    in the cwd, and creates one if it's not present. It then allows a user to
    input a new meal by listing the number of ingredients and their amounts.
    Then a file is written with the title, number of servings and the ingredient
    list and amounts.
    """
    import os

    # check for and/or creation of the recipe_book directory
    filepath = str(os.getcwd() + '\\recipe_book')
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    # this is also the code for changemeal()
    # setting title, number of ingredients and amount with unit
    title = input('What is the meal name? ').title()
    number = int(input('How many ingredients? '))
    no_ing = list(range(0,number)) # number of ingredients
    ing_am = list(range(0,number)) # amount of each ingredient
    am_unit = list(range(0,number)) # unit of the amount
    for i in no_ing:
        no_ing[i] = input('What is an ingredient? ').title() # always titled
        ing_am[i] = int(input('What is the amount? '))
        am_unit[i] = input('What is the unit? ').lower() # always lowercase

    # set number of days meal will be for, one or two days only
    pWsAJjrHwk = 0
    while pWsAJjrHwk == 0:
        jyrmwemjfe = input('How many days will it be for? ')
        try:
            iUfGEqhuPW = int(jyrmwemjfe)
            pWsAJjrHwk = 1
        except ValueError:
            print('')
            print("That's not an number!")

    # if it is a two day meal, set if it can be halved easily
    if iUfGEqhuPW == 2:
        oWHYGDTejp = 0
        while oWHYGDTejp == 0:
            cCUYyfWkIk = (input('Can this also be for one day? (y/n) ')).lower()
            if cCUYyfWkIk == 'y':
                iUfGEqhuPW = 3
                servings_list = list(range(1,iUfGEqhuPW))
                oWHYGDTejp = 1
            elif cCUYyfWkIk == 'n':
                iUfGEqhuPW = 2
                servings_list = [iUfGEqhuPW]
                oWHYGDTejp = 1
            else:
                 print('Please enter if this can this also be for one day "y" or "n"')
    else:
        servings_list = [iUfGEqhuPW]

    # set if this is a pie meal
    EUZTXhpFnA = 0
    while EUZTXhpFnA == 0:
        pie_check = (input('Is meal a pie, (y/n)? ')).lower()
        if pie_check == 'y':
            pie = '1'
            EUZTXhpFnA = 1
        elif pie_check == 'n':
            pie = '0'
            EUZTXhpFnA = 1
        else:
             print('Please enter if this is a pie meal "y" or "n" ')

    # set if this is a faffy meal
    EMPxeBgRMx = 0
    while EMPxeBgRMx == 0:
        faff_check = (input('Is this a faffy meal, (y/n)? ')).lower()
        if faff_check == 'y':
            faff = '1'
            EMPxeBgRMx = 1
        elif faff_check == 'n':
            faff = '0'
            EMPxeBgRMx = 1
        else:
             print('Please enter if this is a faffy meal "y" or "n" ')

    # set the main carbohydrate type
    hIgMHfWSlz = ['Pasta','Rice','Bread','Couscous','Potato']
    fwjdJsQJwc = 0
    while fwjdJsQJwc == 0:
        carb_type = input('What is the main carbohydrate (pasta, rice, bread, couscous, potato)? ').title()
        if carb_type in hIgMHfWSlz:
            fwjdJsQJwc = 1
        else:
            print('That does not make sense.')

    # set the meal type (vegetarian, fish or meat)
    aAPokUoGVJ = 0
    while aAPokUoGVJ == 0:
        vegetarian_check = input('Is this a vegetarian meal? (y/n) ').title()
        if vegetarian_check == 'Y' or vegetarian_check == 'Yes':
            meal_type = 'Vegetarian'
            aAPokUoGVJ = 1
        else:
            fish_check = input('Is this a fish meal? (y/n) ').title()
            if fish_check == 'Y' or fish_check == 'Yes':
                meal_type = 'Fish'
                aAPokUoGVJ = 1
            else:
                meal_type = 'Meat'
                aAPokUoGVJ = 1

    # if it's a meat meal, set meat type
    if meal_type == 'Meat':
        ecNTnjBrfA = ['Poultry','Beef','Pork','Game']
        JKcYzRDWZz = 0
        while JKcYzRDWZz == 0:
            meat_type = input('What kind of meat is it (poultry, beef, pork, game)? ').title()
            if meat_type in ecNTnjBrfA:
                JKcYzRDWZz = 1
            else:
                print('That does not make sense.')
    else:
        meat_type = 'N/A'

    check_EnqO = 0
    while check_EnqO != 1:

        additional_item_check = input('Are there any additional items that are needed in this meal (e.g. herbs and spices, condiments)? ').lower()

        if additional_item_check == 'yes' or additional_item_check == 'y':
            check_gDgC = 0
            additional_items = []

            while check_gDgC != 1:
                current_additional = input('What additional items do you want to add (type "end" to quit)? ').lower()
                if current_additional == 'end':
                    check_gDgC = 1
                else:
                    additional_items.append(current_additional)
            check_EnqO = 1
        elif additional_item_check == 'no' or additional_item_check == 'n':
            additional_items = ['N/A']
            check_EnqO = 1
        else:
            print('That does not make sense')

    # creation of the meal file txt file with all the parameters set previously
    filename = str(filepath + '\\' + title + '.txt')
    ingredients = str(no_ing)
    amounts = str(ing_am)
    units = str(am_unit)
    servings_string = str(servings_list)
    additional_items_string = str(additional_items)
    file = open(filename, 'w')
    file.write(title)
    file.write('\n\n')
    file.write(servings_string)
    file.write('\n\n')
    file.write(faff)
    file.write('\n\n')
    file.write(pie)
    file.write('\n\n')
    file.write(carb_type)
    file.write('\n\n')
    file.write(meal_type)
    file.write('\n\n')
    file.write(meat_type)
    file.write('\n\n')
    file.write(ingredients)
    file.write('\n\n')
    file.write(amounts)
    file.write('\n\n')
    file.write(units)
    file.write('\n\n')
    file.write(additional_items_string)
    file.close()

    # end process
    beg_greet = 'New meal "'
    end_greet = '" created!'
    print(beg_greet + title + end_greet)

def mealchange():
    """This function allows the replacement of an existing meal file. It is
    essentially the same as the newmeal function, but it will overwrite the
    old meal file with the new meal characteristics."""

    import os

    # check for and/or creation of the recipe_book directory
    recipe_book_path = str(os.getcwd() + '\\recipe_book')
    if not os.path.exists(recipe_book_path):
        os.makedirs(recipe_book_path)

    # lists all the files in the recipe_book
    recipe_book_list = os.listdir(recipe_book_path)

    # makes a list with no .txt extention
    meal_list = [recipe_book_list[i].strip('.txt') for i in range(len(recipe_book_list))]

    # runs a meallist function and finds what meal file is to be change
    for i in meal_list:
        print(i)
    change_meal = input('What meal do you want to change?').title()

    # checks if the meal file actually exists (by title)
    while change_meal not in meal_list:
        print('That is not a listed meal, try again.')
        change_meal = input('What meal do you want to change?').title()
    # check and/or creation of recipe book
    filepath = str(os.getcwd() + '\\recipe_book')
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    # setting title, number of ingredients and amount with unit
    title = change_meal
    number = int(input('How many ingredients? '))
    no_ing = list(range(0,number)) # number of ingredients
    ing_am = list(range(0,number)) # amount of each ingredient
    am_unit = list(range(0,number)) # unit of the amount
    for i in no_ing:
        no_ing[i] = input('What is an ingredient? ').title() # always titled
        ing_am[i] = int(input('What is the amount? '))
        am_unit[i] = input('What is the unit? ').lower() # always lowercase

    # set number of days meal will be for, one or two days only
    pWsAJjrHwk = 0
    while pWsAJjrHwk == 0:
        jyrmwemjfe = input('How many days will it be for? ')
        try:
            iUfGEqhuPW = int(jyrmwemjfe)
            pWsAJjrHwk = 1
        except ValueError:
            print('')
            print("That's not an number!")

    # if it is a two day meal, set if it can be halved easily
    if iUfGEqhuPW == 2:
        oWHYGDTejp = 0
        while oWHYGDTejp == 0:
            cCUYyfWkIk = (input('Can this also be for one day? (y/n) ')).lower()
            if cCUYyfWkIk == 'y':
                iUfGEqhuPW = 3
                servings_list = list(range(1,iUfGEqhuPW))
                oWHYGDTejp = 1
            elif cCUYyfWkIk == 'n':
                iUfGEqhuPW = 2
                servings_list = [iUfGEqhuPW]
                oWHYGDTejp = 1
            else:
                 print('Please enter if this can this also be for one day "y" or "n"')
    else:
        servings_list = [iUfGEqhuPW]

    # set if this is a pie meal
    EUZTXhpFnA = 0
    while EUZTXhpFnA == 0:
        pie_check = (input('Is meal a pie, (y/n)? ')).lower()
        if pie_check == 'y':
            pie = '1'
            EUZTXhpFnA = 1
        elif pie_check == 'n':
            pie = '0'
            EUZTXhpFnA = 1
        else:
             print('Please enter if this is a pie meal "y" or "n" ')

    # set if this is a faffy meal
    EMPxeBgRMx = 0
    while EMPxeBgRMx == 0:
        faff_check = (input('Is this a faffy meal, (y/n)? ')).lower()
        if faff_check == 'y':
            faff = '1'
            EMPxeBgRMx = 1
        elif faff_check == 'n':
            faff = '0'
            EMPxeBgRMx = 1
        else:
             print('Please enter if this is a faffy meal "y" or "n" ')

    # set the main carbohydrate type
    hIgMHfWSlz = ['Pasta','Rice','Bread','Couscous','Potato']
    fwjdJsQJwc = 0
    while fwjdJsQJwc == 0:
        carb_type = input('What is the main carbohydrate (pasta, rice, bread, couscous, potato)? ').title()
        if carb_type in hIgMHfWSlz:
            fwjdJsQJwc = 1
        else:
            print('That does not make sense.')

    # set the meal type (vegetarian, fish or meat)
    aAPokUoGVJ = 0
    while aAPokUoGVJ == 0:
        vegetarian_check = input('Is this a vegetarian meal? (y/n) ').title()
        if vegetarian_check == 'Y' or vegetarian_check == 'Yes':
            meal_type = 'Vegetarian'
            aAPokUoGVJ = 1
        else:
            fish_check = input('Is this a fish meal? (y/n) ').title()
            if fish_check == 'Y' or fish_check == 'Yes':
                meal_type = 'Fish'
                aAPokUoGVJ = 1
            else:
                meal_type = 'Meat'
                aAPokUoGVJ = 1

    # if it's a meat meal, set meat type
    if meal_type == 'Meat':
        ecNTnjBrfA = ['Poultry','Beef','Pork','Game']
        JKcYzRDWZz = 0
        while JKcYzRDWZz == 0:
            meat_type = input('What kind of meat is it (poultry, beef, pork, game)? ').title()
            if meat_type in ecNTnjBrfA:
                JKcYzRDWZz = 1
            else:
                print('That does not make sense.')
    else:
        meat_type = 'N/A'

    check_EnqO = 0
    while check_EnqO != 1:

        additional_item_check = input('Are there any additional items that are needed in this meal (e.g. herbs and spices, condiments)? ').lower()

        if additional_item_check == 'yes' or additional_item_check == 'y':
            check_gDgC = 0
            additional_items = []

            while check_gDgC != 1:
                current_additional = input('What additional items do you want to add (type "end" to quit)? ').lower()
                if current_additional == 'end':
                    check_gDgC = 1
                else:
                    additional_items.append(current_additional)
            check_EnqO = 1
        elif additional_item_check == 'no' or additional_item_check == 'n':
            additional_items = ['N/A']
            check_EnqO = 1
        else:
            print('That does not make sense')

    # creation of the meal file txt file with all the parameters set previously
    filename = str(filepath + '\\' + title + '.txt')
    ingredients = str(no_ing)
    amounts = str(ing_am)
    units = str(am_unit)
    servings_string = str(servings_list)
    additional_items_string = str(additional_items)
    file = open(filename, 'w')
    file.write(title)
    file.write('\n\n')
    file.write(servings_string)
    file.write('\n\n')
    file.write(faff)
    file.write('\n\n')
    file.write(pie)
    file.write('\n\n')
    file.write(carb_type)
    file.write('\n\n')
    file.write(meal_type)
    file.write('\n\n')
    file.write(meat_type)
    file.write('\n\n')
    file.write(ingredients)
    file.write('\n\n')
    file.write(amounts)
    file.write('\n\n')
    file.write(units)
    file.write('\n\n')
    file.write(additional_items_string)
    file.close()

    # end process
    beg_greet = '"'
    end_greet = '" changed!'
    print(beg_greet + title + end_greet)

def deletemeal():
    """This function will give the option to delete a meal file in the
    recipe_book directory."""

    import os

    recipe_book_path = str(os.getcwd() + '\\recipe_book')
    if not os.path.exists(recipe_book_path):
        os.makedirs(recipe_book_path)

    # lists all the files in the recipe_book
    recipe_book_list = os.listdir(recipe_book_path)

    # makes a list with no .txt extention
    meal_list = [recipe_book_list[i].strip('.txt') for i in range(len(recipe_book_list))]

    # running and seeing the meal list so the user can choose the meal for deletion
    for i in meal_list:
        print(i)
    print('')

    # setting the file for deletion
    KUvlAvHnRO = 0
    uXXBdJeZrb = input('What meal do you want to remove? ').title()
    print('')
    while KUvlAvHnRO == 0: # while loop to find if it is in the meal list
        if uXXBdJeZrb not in meal_list:
            print('That is not a meal on the list!')
            print('')
            uXXBdJeZrb = input('What meal do you want to remove? ').title()
            print('')
        else:
            KUvlAvHnRO = 1

    # generation of the file path to file and deletion of meal file
    file_path_to_delete = str(os.getcwd() + '\\recipe_book' + '\\' + uXXBdJeZrb + '.txt')
    os.remove(file_path_to_delete)

    # end process and printing of the new meal_list
    print(uXXBdJeZrb + '.txt deleted!')
    print('')

    recipe_book_path = str(os.getcwd() + '\\recipe_book')
    if not os.path.exists(recipe_book_path):
        os.makedirs(recipe_book_path)

    # lists all the files in the recipe_book
    recipe_book_list = os.listdir(recipe_book_path)

    # makes a list with no .txt extention
    meal_list = [recipe_book_list[i].strip('.txt') for i in range(len(recipe_book_list))]

    for i in meal_list:
        print(i)
