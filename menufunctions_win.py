def meallist():
    """Function to check if there is a directory called 'recipe_book'
    in the cwd, and creates one if it is not present. It then creates and returns a list of
    all the meals present in the recipe_book directory.
    """
    import os

    #checks for and creation of the recipe_book directory
    recipe_book_path = str(os.getcwd() + '\\recipe_book')
    if not os.path.exists(recipe_book_path):
        os.makedirs(recipe_book_path)

    #lists all the files in the recipe_book
    recipe_book_list = os.listdir(recipe_book_path)

    #makes a list with no .txt extention
    meal_list = [recipe_book_list[i].strip('.txt') for i in range(len(recipe_book_list))]
    return(meal_list)

def newmeal():
    """Function checks to see if there is a directory called 'recipe_book
    in the cwd, and creates one if it's not present. It then allows a user to
    input a new meal by listing the number of ingredients and their amounts.
    Then a file is written with the title, number of servings and the ingredient
    list and amounts. Testing.
    Testing.
    """
    import os
    from menufunctions_win import meallist

    meal_list = meallist()
    while True:
        title = input('What is the meal name? ').title()
        if title in meal_list:
            print('That is already a meal, please choose another meal name')
            continue
        else:
            ingredients = []
            amounts = []
            units = []
            while True:
                current_ing = input('Name an ingredient or enter "end" to exit ').title()
                if current_ing == 'End':
                    break
                else:
                    ing_am = int(input('How much of this ingredient? '))
                    ing_unit = input('what is the unit? ').lower()
                    ingredients.append(current_ing)
                    amounts.append(ing_am)
                    units.append(ing_unit)
        break

    #set number of days meal will be for, one or two days only
    while True:
        servQuest = input('How many days will it be for (one or two days only)? ')
        if servQuest == '1':
            servings = 'One day'
            break
        elif servQuest == '2':
            while True:
                dayQuest = input('Can this also be for one day? (y/n) ').lower()
                if dayQuest == 'y' or dayQuest == 'yes':
                    servings = 'One or two days'
                    break
                elif dayQuest == 'n' or dayQuest == 'no':
                    servings = 'Two days'
                    break
                else:
                    print('That does not make sense')
            break
        else:
            print('That does not make sense')

    #set if this is a pie meal
    while True:
        pieQuest = (input('Is meal a pie, (y/n)? ')).lower()
        if pieQuest == 'y' or pieQuest == 'yes':
            pie = 'Pie'
            break
        elif pieQuest == 'n' or pieQuest == 'no':
            pie = 'Not pie'
            break
        else:
             print('Please enter if this is a pie meal "y" or "n"')

    #set if this is a faffy meal
    while True:
        faffQuest = (input('Is this a faffy meal, (y/n)? ')).lower()
        if faffQuest == 'y' or faffQuest == 'yes':
            faff = 'Faffy'
            break
        elif faffQuest == 'n' or faffQuest == 'no':
            faff = 'Not faffy'
            break
        else:
             print('Please enter if this is a faffy meal "y" or "n" ')

    #set the main carbohydrate type
    carbList = ['Pasta','Rice','Bread','Couscous','Potato']
    while True:
        carbQuest = input('What is the main carbohydrate (pasta, rice, bread, couscous, potato)? ').title()
        if carbQuest in carbList:
            break
        else:
            print('That does not make sense')

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

    #making a list of any potential additional items that might be needed
    additional_items = []
    while True:
        current_additional = input('What additional items might be needed (type "end" to quit)? ').title()
        if current_additional == 'End':
            break
        else:
            additional_items.append(current_additional)

    # creation of the meal file txt file with all the parameters set previously
    filename = str(os.getcwd() + '\\recipe_book' + '\\' + title + '.txt')
    ingredients = str(ingredients)
    amounts = str(amounts)
    units = str(units)
    additional_items_string = str(additional_items)
    file = open(filename, 'w')
    file.write(title)
    file.write('\n\n')
    file.write(servings)
    file.write('\n\n')
    file.write(faff)
    file.write('\n\n')
    file.write(pie)
    file.write('\n\n')
    file.write(carbQuest)
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

def mealSelector():
    """ This function randomly chooses a meal file for meal 1 and asigns the characheristics
    of that meal file to a list which can then be sliced returning the desired
    characteristics.
    """
    import os
    import ast
    import random
    from menufunctions_win import meallist

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

def generate_menu_and_list():
    """The main function in the entire program. Using the lineprint function the
    meal choices are made and then if they all meet the desired menu characteristics.
    If they do, then one of the single meal files is halved (to get seven meals)
    and the list file is built and written to the cwd. Testing.
    Testing.
    """
    import os
    import datetime
    from menufunctions_win import mealSelector

    # running lineprint functions to get the meal files and the characteristics of that meal
    DLSDbqNGCK = 0 # while loop to check randomly selected meals fit the menu characteristics
    while DLSDbqNGCK == 0:
        meal_choice_m1 = mealSelector()
        meal_choice_m2 = mealSelector()
        meal_choice_m3 = mealSelector()
        meal_choice_m4 = mealSelector()
        if meal_choice_m1[5] + meal_choice_m2[5] + meal_choice_m3[5] + meal_choice_m4[5] == 1: # check for faff, later this will be the check for pie
            faff_check = 1
        else:
            faff_check = 0
        if len(set([meal_choice_m1[7], meal_choice_m2[7], meal_choice_m3[7], meal_choice_m4[7]])) == 4: # check for carb types
            carb_check = 1
        else:
            carb_check = 0
        if len(set([meal_choice_m1[8], meal_choice_m2[8], meal_choice_m3[8], meal_choice_m4[8]])) == 3: # check for meal type
            mealtype_check = 1
        else:
            mealtype_check = 0
        if [meal_choice_m1[8], meal_choice_m2[8], meal_choice_m3[8], meal_choice_m4[8]].count('Meat') == 2: # if two meat meals, check for meat type
            meat_list = list([meal_choice_m1[9], meal_choice_m2[9], meal_choice_m3[9], meal_choice_m4[9]]) # list all meats
            meat_list = [x for x in meat_list if x != 'N/A'] # removes 'N/A' from the list
            meat_set = set(meat_list)
            if len(meat_set) == 2:
                meat_check = 1
            else:
                meat_check = 0
        else:
            meat_list = list([meal_choice_m1[9], meal_choice_m2[9], meal_choice_m3[9], meal_choice_m4[9]])
            meat_list = [x for x in meat_list if x != 'N/A']
            meat_set = set(meat_list) # meat_set is used later and is necessary
            meat_check = 1
        if meal_choice_m1[4] == [1, 2] or meal_choice_m2[4] == [1, 2] or meal_choice_m3[4] == [1, 2] or meal_choice_m4[4] == [1, 2]:
            servings_check = 1 # check for a meal that can have multiple servings
        else:
            servings_check = 0
        if len(set([meal_choice_m1[0],meal_choice_m2[0],meal_choice_m3[0],meal_choice_m4[0]])) == 4: #checks if there are no duplicated meals
            name_check = 1
        else:
            name_check = 0
        if faff_check + carb_check + mealtype_check + meat_check + servings_check + name_check == 6: # if all checks are met, end loop
            DLSDbqNGCK = 1
        else:
            DLSDbqNGCK = 0

    # set suitable objects to meal ingredient amounts
    m1_ams = meal_choice_m1[2]
    m2_ams = meal_choice_m2[2]
    m3_ams = meal_choice_m3[2]
    m4_ams = meal_choice_m4[2]

    servings_change = 0 # while loop to halve the ingredient amounts for the meal with multiple servings
    while servings_change == 0:
        if meal_choice_m1[4] == [1, 2]:
            m1_ams = []
            for i in meal_choice_m1[2]:
                m1_ams.append(round(i/2))
                servings_change = 1
        elif meal_choice_m2[4] == [1, 2]:
            m2_ams = []
            for i in meal_choice_m2[2]:
                m2_ams.append(round(i/2))
                servings_change = 1
        elif meal_choice_m3[4] == [1, 2]:
            m3_ams = []
            for i in meal_choice_m3[2]:
                m3_ams.append(round(i/2))
                servings_change = 1
        elif meal_choice_m4[4] == [1, 2]:
            m4_ams = []
            for i in meal_choice_m4[2]:
                m4_ams.append(round(i/2))
                servings_change = 1
        else:
            print('THERE IS AN ERROR IN THE NUMBER OF SERVINGS') #this shoudn't be needed

    #for ease, the meal choices and the important characertistics are printed to decide if another menu should be generated
    print('\n')
    print('The meals are:')
    print(meal_choice_m1[0])
    print(meal_choice_m2[0])
    print(meal_choice_m3[0])
    print(meal_choice_m4[0])
    print('\n')
    print('The main carbohydrate in each meal is:')
    print(meal_choice_m1[7])
    print(meal_choice_m2[7])
    print(meal_choice_m3[7])
    print(meal_choice_m4[7])
    print('\n')
    print('The meal types are:')
    print(meal_choice_m1[8])
    print(meal_choice_m2[8])
    print(meal_choice_m3[8])
    print(meal_choice_m4[8])
    print('\n')
    print('The meat types are:')
    for i in list(meat_set):
        print(i)
    print('\n')

    # un-necessary change of object lable, but too lazy to change it
    lst1 = meal_choice_m1[1]
    lst2 = meal_choice_m1[2]
    lst2_5 = meal_choice_m1[3]
    lst3 = meal_choice_m2[1]
    lst4 = meal_choice_m2[2]
    lst4_5 = meal_choice_m2[3]
    lst5 = meal_choice_m3[1]
    lst6 = meal_choice_m3[2]
    lst6_5 = meal_choice_m3[3]
    lst7 = meal_choice_m4[1]
    lst8 = meal_choice_m4[2]
    lst8_5 = meal_choice_m4[3]

    list_all_ing = lst1 + lst3 + lst5 + lst7 # all ingredients (including duplicates) are listed

    list_all_ing_no_dup = [] # removing duplicated ingredients
    for i in list_all_ing:
        if i not in list_all_ing_no_dup:
            list_all_ing_no_dup.append(i)

    duplicate_ings = [] # creating of a list of duplicated ingredients
    for i in list_all_ing_no_dup:
        if list_all_ing.count(i) > 1:
            duplicate_ings.append(i)

    # while loop to find the amounts relating to the duplicated items then summing the relavent
    # amounts and putting it into a list with positions corresponding to the duplicated items list
    checkq = 0
    lst_of_dup_ams = []
    while checkq != len(duplicate_ings):
        curr_dup = duplicate_ings[checkq]

        ab1 = 0
        ab2 = 0
        ab3 = 0
        ab4 = 0

        try:
            ab1 = lst2[lst1.index(curr_dup)]
        except ValueError:
            pass
        try:
            ab2 = lst4[lst3.index(curr_dup)]
        except ValueError:
            pass
        try:
            ab3 = lst6[lst5.index(curr_dup)]
        except ValueError:
            pass
        try:
            ab4 = lst8[lst7.index(curr_dup)]
        except ValueError:
            pass

        am_of_curr_dup = ab1 + ab2 + ab3 + ab4
        lst_of_dup_ams.append(am_of_curr_dup)
        checkq += 1


    checkq = 0
    lst_of_dup_units = []

    # while loop to check that the units for duplicate ingredients match and puts the
    # units in a list with positions corresponding to the duplicated ingredients
    while checkq != len(duplicate_ings):
        curr_dup = duplicate_ings[checkq]

        uab1 = ''
        uab2 = ''
        uab3 = ''
        uab4 = ''

        try:
            uab1 = lst2_5[lst1.index(curr_dup)]
        except ValueError:
            pass
        try:
            uab2 = lst4_5[lst3.index(curr_dup)]
        except ValueError:
            pass
        try:
            uab3 = lst6_5[lst5.index(curr_dup)]
        except ValueError:
            pass
        try:
            uab4 = lst8_5[lst7.index(curr_dup)]
        except ValueError:
            pass

        unit_list = [uab1,uab2,uab3,uab4]
        try:
            unit_list.remove('')
            unit_list.remove('')
        except ValueError:
            pass
        unit_list = list(set(unit_list))

        if len(unit_list) != 1:
            print('THERE IS AN ERROR IN THE DUPLICATE INGREDIENT AMOUNT UNITS')
        unit = unit_list[0] # un-necessary
        lst_of_dup_units.append(unit)
        checkq += 1

    # concatenates the amount and unit for the duplicated ingredients
    no_of_dups = list(range(0,len(duplicate_ings)))
    dup_ams_and_units = []
    for i in no_of_dups:
        dup_ams_and_units.append(str(lst_of_dup_ams[i]) + ' ' + lst_of_dup_units[i])

    # generates a dictionary containing all ingredients as keys and the amounts and units as values
    lst_and_ams = {}
    for i in list_all_ing_no_dup:
        if i in duplicate_ings:
            lst_and_ams.update({i:dup_ams_and_units[duplicate_ings.index(i)]})
        else:
            try:
                lst_and_ams.update({i:str(lst2[lst1.index(i)]) + ' ' + lst2_5[lst1.index(i)]})
            except ValueError:
                pass
            try:
                lst_and_ams.update({i:str(lst4[lst3.index(i)]) + ' ' + lst4_5[lst3.index(i)]})
            except ValueError:
                pass
            try:
                lst_and_ams.update({i:str(lst6[lst5.index(i)]) + ' ' + lst6_5[lst5.index(i)]})
            except ValueError:
                pass
            try:
                lst_and_ams.update({i:str(lst8[lst7.index(i)]) + ' ' + lst8_5[lst7.index(i)]})
            except ValueError:
                pass

    # makes the list .txt file
    fmt = 'List made on %Y-%m-%d-%H-%M-%S' # time-stamp format
    list_file = open(str(os.getcwd() + '\\' + datetime.datetime.now().strftime(fmt) + '.txt'), 'w') #filename and timestamp

    # while loop to see which meal is the multiple servings one and changes the name for the list file
    meal_1 = meal_choice_m1[0]
    meal_2 = meal_choice_m2[0]
    meal_3 = meal_choice_m3[0]
    meal_4 = meal_choice_m4[0]
    servings_change = 0
    while servings_change == 0:
        if meal_choice_m1[4] == [1, 2]:
            meal_1 = str(meal_choice_m1[0] + ' (1)')
            servings_change = 1
        elif meal_choice_m2[4] == [1, 2]:
            meal_2 = str(meal_choice_m2[0] + ' (1)')
            servings_change = 1
        elif meal_choice_m3[4] == [1, 2]:
            meal_3 = str(meal_choice_m3[0] + ' (1)')
            servings_change = 1
        elif meal_choice_m4[4] == [1, 2]:
            meal_4 = str(meal_choice_m4[0] + ' (1)')
            servings_change = 1
        else:
            print('THERE IS AN ERROR IN THE NUMBER OF SERVINGS')

    # writes meal names to the listfile
    list_file.write('Meals:\n')
    list_file.write(meal_1 + '\n')
    list_file.write(meal_2 + '\n')
    list_file.write(meal_3 + '\n')
    list_file.write(meal_4 + '\n\n')

    # write the ingredients and amounts + units to the list file
    list_file.write('Ingredients:\n')
    for key in lst_and_ams:
        x = str(key + " - " + lst_and_ams[key])
        list_file.write(x + '\n')
    list_file.write('\n')

    # additional items for all the meal choices
    additional_items_total = meal_choice_m1[10] + meal_choice_m2[10] + meal_choice_m3[10] + meal_choice_m4[10]
    additional_items_no_dup = []

    for i in additional_items_total:
        if i not in additional_items_no_dup:
            additional_items_no_dup.append(i)

    additional_items_no_dup = [x for x in additional_items_no_dup if x != 'N/A']

    list_file.write('Additional items:\n')
    for i in additional_items_no_dup:
        list_file.write(i + '\n')
    list_file.close()
