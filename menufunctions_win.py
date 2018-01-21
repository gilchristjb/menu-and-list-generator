def meallist():
    """Function to check if there is a directory called 'recipe_book'
    in the cwd, and creates one if it is not present. It then creates and returns a list of
    all the meals present in the recipe_book directory.
    """
    import os

    recipeFiles = os.listdir(str(os.getcwd() + '\\recipe_book'))
    mealList = [x.split('.')[0] for x in recipeFiles]

    return(mealList)

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

    #setting the title and ingredients, amounts and unit lists
    mealList = meallist()
    while True:
        title = input('What is the meal name? ').title()
        if title in mealList:
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
        if pie == 'Pie':
            faff = 'Faffy'
            break
        else:
            pass
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

    #set the meal type (vegetarian, fish or meat)
    while True:
        typeQuest = input('Is this meal vegetarian? (y/n) ').lower()
        if typeQuest == 'y' or typeQuest == 'yes':
            mealType = 'Vegetarian'
            break
        elif typeQuest == 'n' or typeQuest == 'no':
            while True:
                typeQuest = input('Is this a fish meal? (y/n) ').lower()
                if typeQuest == 'y' or typeQuest == 'yes':
                    mealType = 'Fish'
                    break
                elif typeQuest == 'n' or typeQuest == 'no':
                    mealType = 'Meat'
                    break
                else:
                    print('That does not make sense')
            break
        else:
            print('That does not make sense')

    #if it's a meat meal, set meat type
    if mealType == 'Meat':
        meatList = ['Poultry','Beef','Pork','Game','Lamb']
        while True:
            meatQuest = input('What kind of meat is it (poultry, beef, pork, game, lamb)? ').title()
            if meatQuest in meatList:
                break
            else:
                print('That does not make sense')
    else:
        meatQuest = 'No meat'

    #making a list of any potential additional items that might be needed
    additionalItems = []
    while True:
        current_additional = input('What additional items might be needed (type "end" to quit)? ').title()
        if current_additional == 'End':
            break
        else:
            additionalItems.append(current_additional)

    #creation of the meal file txt file with all the parameters set previously
    filename = str(os.getcwd() + '\\recipe_book' + '\\' + title + '.txt')
    ingredients = str(ingredients)
    amounts = str(amounts)
    units = str(units)
    additionalItems = str(additionalItems)
    file = open(filename, 'w')
    file.write(title + '\n\n')
    file.write(servings + '\n\n')
    file.write(faff + '\n\n')
    file.write(pie + '\n\n')
    file.write(carbQuest + '\n\n')
    file.write(mealType + '\n\n')
    file.write(meatQuest + '\n\n')
    file.write(ingredients + '\n\n')
    file.write(amounts + '\n\n')
    file.write(units + '\n\n')
    file.write(additionalItems + '\n\n')
    file.close()

    print('New meal "' + title + '" created!')

def mealchange():
    """This function allows the replacement of an existing meal file. It is
    essentially the same as the newmeal function, but it will overwrite the
    old meal file with the new meal characteristics."""

    import os
    import ast

    #runs meallist() to print all the available meals to change
    mealList = meallist()
    for i in mealList:
        print(i)
    print('')

    #choosing what meal is to be chnaged
    while True:
        changeMeal = input('What meal do you want to change?\n').title()
        if changeMeal not in mealList:
            print('That is not a listed meal.')
        else:
            break

    #generating the filepath to the .txt document
    #opening as read and extracting the meal characteristics into a list (mealChars) except for
    #ingredients, amounts, units and additional items which have their own variables
    changeFile = str(os.getcwd() + '\\recipe_book\\' + changeMeal + '.txt')

    with open(changeFile,"r") as tempChangeFile:

        mealChars = tempChangeFile.readlines()
        
        ingList = ast.literal_eval(mealChars[14])
        amList = ast.literal_eval(mealChars[16])
        unitList = ast.literal_eval(mealChars[18])
        addIngs = ast.literal_eval(mealChars[20])
    tempChangeFile.close()

    #creating a range of possible requests for the option of what to choose
    servResp = ['servings', 'serving', 'serv', 'serves', 'servs']
    pieResp = ['pie', 'not pie']
    faffResp = ['faff', 'faffy', 'fafy', 'faf']
    carbResp = ['main carbohydrate', 'main carb', 'carb', 'carbs', 'maincarbohydrate', 'maincarb']
    mealResp = ['meal type', 'meal', 'type', 'mealtype']
    meatResp = ['meat', 'meat type', 'meattype']
    ingResp = ['ingredients','ings', 'ing']
    amResp = ['amounts', 'ams', 'amount']
    unitResp = ['units', 'unit', 'uns']
    addResp = ['additional items','additional', 'additionalitems','items', 'add', 'additionals', 'add items', 'additems']

    while True:

        #options to choose from, the characteristics have \n at the end, and so always go on a separate line
        print('\nChanging "' + changeMeal + '.txt"\n')
        print('Servings? ' + mealChars[2])
        print('Pie? ' + mealChars[6])
        print('Faff? ' + mealChars[4])
        print('Main carbohydrate: ' + mealChars[8])
        print('Meal type: ' + mealChars[10])
        print('Meat type: ' + mealChars[12])
        print('Ingredients, amounts and units:')
        #ingredients, amounts and units are concatenated together
        for i in ingList:
            print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
        print('\nAdditional Items:')
        print(', '.join(addIngs))

        changeChoice = input('\nType what you want to change or do.\n').lower()
        print('')

        #changing servings
        if changeChoice in servResp:
            while True:
                servChoice = input('How many days will this be for? ').lower()
                if servChoice == '1' or servChoice == 'one':
                    mealChars[2] = 'One day'
                    break
                if servChoice == 'end':
                    break
                if servChoice == '2' or servChoice == 'two':
                    while True:
                        twoServChoice = input('Can this also be for one day (y/n)? ').lower()
                        if twoServChoice == 'y' or twoServChoice == 'yes':
                            mealChars[2] = 'One or two days'
                            break
                        if twoServChoice == 'n' or twoServChoice == 'no':
                            mealChars[2] = 'Two days'
                            break
                        if twoServChoice == 'end':
                            break
                        else:
                            print('That does not make sense.')
                    break
                else:
                    print('That does not make sense.')

        #changing pie status (also changes faff status if pie)
        if changeChoice in pieResp:
            while True:
                pieChoice = input('Is this meal a pie (y/n)? ').lower()
                if pieChoice == 'y' or pieChoice == 'yes':
                    mealChars[4] = 'Faffy'
                    mealChars[6] = 'Pie'
                    break
                if pieChoice == 'n' or pieChoice == 'no':
                    mealChars[6] = 'Not pie'
                    break
                if pieChoice == 'end':
                    break
                else:
                    print('That dose not make sense.')

        #changing faff status, not possible to if pie
        if changeChoice in faffResp:
            while True:
                if mealChars[6] == 'Pie':
                    print('All pies are faffy, change to "Not pie" first.')
                    break
                else:
                    while True:
                        faffChoice = (input('Is this a faffy meal (y/n)? ')).lower()
                        if faffChoice == 'y' or faffChoice == 'yes':
                            mealChars[4] = 'Faffy\n'
                            break
                        if faffChoice == 'n' or faffChoice == 'no':
                            mealChars[4] = 'Not faffy\n'
                            break
                        if faffChoice == 'end':
                            break
                        else:
                             print('Please enter if this is a faffy meal "y" or "n" ')
                    break

        #changing the main carbohydrate
        if changeChoice in carbResp:
            carbList = ['Pasta','Rice','Bread','Couscous','Potato']
            while True:
                carbChoice = input('What is the main carbohydrate (pasta, rice, bread, couscous, potato)? ').title()
                if carbChoice in carbList:
                    mealChars[8] = carbChoice
                    break
                else:
                    print('That does not make sense.')

        #changine meal type (also change meat type if meat meal)
        if changeChoice in mealResp:
            while True:
                mealChoice = input('What mealtype is this (vegetarian, fish, meat)? ').lower()
                if mealChoice == 'vegetarian' or mealChoice == 'veg':
                    mealChars[10] = 'Vegetarian'
                    break
                if mealChoice == 'fish':
                    mealChars[10] = 'Fish'
                    break
                if mealChoice == 'meat':
                    mealChars[10] = 'Meat'
                    meatList = ['Poultry','Beef','Pork','Game','Lamb']
                    while True:
                        meatChoice = input('What kind of meat is it (poultry, beef, pork, game, lamb)? ').title()
                        if meatChoice in meatList:
                            mealChars[12] = meatChoice
                            break
                        if meatChoice == 'End':
                            break
                        else:
                            print('That does not make sense.')
                    break
                if mealChoice == 'end':
                    break
                else:
                    print('That does not make sense.')

        #change meat type is it's a meat meal
        if changeChoice in meatResp:
            if mealChars[10] == 'Meat':
                meatList = ['Poultry','Beef','Pork','Game','Lamb']
                while True:
                    meatChoice = input('What kind of meat is it (poultry, beef, pork, game, lamb)? ').title()
                    if meatChoice in meatList:
                        mealChars[12] = meatChoice
                        break
                    else:
                        print('That does not make sense.')
            else:
                print('Change meal type to "Meat" first.')

        #changing ingredients, amounts and units
        if changeChoice in ingResp or changeChoice in amResp or changeChoice in unitResp:
            while True:
                changeOrAdd = input("""Do you want to add an ingredient or make changes to the ingredients, amounts and units?
Enter "add" or "change" or type "end" anytime to go back.\n""").lower()
                print('')
                if changeOrAdd == 'change':
                    while True:
                        print('Ingredients: ' + (', '.join(ingList)))
                        print('Amounts: ' + (', '.join([str(i) for i in amList])))
                        print('Units: ' + (', '.join(unitList)))
                        ingChangeChoice = input("""\nWhat do you want to change (ingrediets, amounts or units)?\n""").lower()
                        print('')

                        if ingChangeChoice in ingResp:
                            while True:
                                print('Ingredients: ' + (', '.join(ingList)))
                                ingChoice = input('Which ingredient do you want to change? \n').title()
                                print('')
                                if ingChoice in ingList:
                                    changeIndex = ingList.index(ingChoice)
                                    ingList[changeIndex] = input('What do you want to replace it with?\n').title()
                                    print('')
                                    amList[changeIndex] = int(input('What is the amount?\n'))
                                    print('')
                                    unitList[changeIndex] = input('In what unit?\n').lower()
                                    print('')
                                    break
                                elif ingChoice == 'End':
                                    break
                                else:
                                    print('That does not make sense.1\n')

                        elif ingChangeChoice in amResp:
                            while True:
                                print('Ingredients: ' + (', '.join(ingList)))
                                amChoice = input('What ingredient do you want to change the amount of?\n').title()
                                print('')
                                if amChoice in ingList:
                                    try:
                                        changeIndex = ingList.index(amChoice)
                                        amList[changeIndex] = int(input('What is the new amount?\n'))
                                        print('')
                                        break
                                    except ValueError:
                                        print('\nOUCH! Only enter numbers please!\n')
                                        break
                                if amChoice == 'End':
                                    break
                                else:
                                    print('That does not make sense.2\n')

                        elif ingChangeChoice in unitResp:
                            while True:
                                print('Ingredients: ' + (', '.join(ingList)))
                                unitChoice = input('What ingredient do you want to change the unit of?\n').title()
                                print('')
                                if unitChoice in ingList:
                                    changeIndex = ingList.index(unitChoice)
                                    unitList[changeIndex] = input('What is the new unit?\n').lower()
                                    print('')
                                    break
                                if unitChoice == 'End':
                                    break
                                else:
                                    print('That does not make sense.3\n')

                        elif ingChangeChoice == 'end':
                            break
                        else:
                            print('That does not make sense.4\n')

                elif changeOrAdd == 'add':
                    print(changeOrAdd)
                elif changeOrAdd == 'end':
                    break
                else:
                #if changeOrAdd != 'change' or changeOrAdd != 'add' or changeOrAdd != 'end':
                    print('That does not make sense.5')



        #changing additional items
        if changeChoice in addResp:
            print(ingList)
            print(amList)
            print(unitList)

        #finilaize change and write to meal file
        if changeChoice == 'Finalize change':
            print(changeChoice)

        #end option
        if changeChoice == 'end':
            break

        #default error response
        if changeChoice not in servResp + pieResp + faffResp + carbResp + mealResp + meatResp + ingResp + addResp:
            print('That does not make sense.')


def deletemeal():
    """This function will give the option to delete a meal file in the
    recipe_book directory."""

    import os
    from menufunctions_win import meallist

    #producing a list of meals in the recipe_book directory
    mealList = meallist()
    for i in mealList:
        print(i)
    print('')

    #choosing the file for deletion
    while True:
        delQuest = input('What meal do you want to remove? ').title()
        if delQuest not in mealList:
            print('That is not a meal on the list!')
        else:
            break

    #generation of the file path to file and deletion of meal file
    while True:
        print('Are you sure you want to delete "' + delQuest + '" (y/n)?')
        delCheck = input('\n').lower()
        if delCheck == 'yes' or delCheck == 'y':
            delPath = str(os.getcwd() + '\\recipe_book' + '\\' + delQuest + '.txt')
            os.remove(delPath)

            # end process
            print(delQuest + '.txt deleted!\n')
            mealList = meallist()
            for i in mealList:
                print(i)
            break
        elif delCheck == 'no' or delCheck == 'n':
            break
        else:
            print('That does not make sense.')

    #delPath = str(os.getcwd() + '\\recipe_book' + '\\' + delQuest + '.txt')
    #os.remove(delPath)

    # end process
    #print(delQuest + '.txt deleted!')
    #mealList = meallist()
    #for i in mealList:
    #    print(i)

def mealselector():
    """ This function randomly chooses a meal file for meal 1 and asigns the characheristics
    of that meal file to a list which can then be sliced returning the desired
    characteristics.
    """
    import os
    import ast
    import random
    from menufunctions_win import meallist

    #randomly chooses a meal from meallist and finds the file path
    mealChoice = str(random.choice(meallist()))
    choicePath = str(os.getcwd() + '\\recipe_book\\' + mealChoice + '.txt')

    #reads all the lines from the mealfile and removes quotes
    with open(choicePath,"r") as x:
        allChars = [i.strip() for i in x.readlines()]

    #asigns the appropriate characteristics to reasonable local variables
    #interprets the lists given in the meal file as actual lists

    if allChars[2] == 'Two days':
        servings = [2,2]
    elif allChars[2] == 'One or two days':
        servings = [random.choice([1,2]),2]
    else:
        servings = [1,1]

    if allChars[4] == 'Faffy':
        faffCheck = 1
    else:
        faffCheck = 0

    if allChars[6] == 'Pie':
        pieCheck = 1
    else:
        pieCheck = 0

    mainCarb = allChars[8]
    mealType = allChars[10]
    meatType = allChars[12]
    ingredients = ast.literal_eval(allChars[14])
    amounts = ast.literal_eval(allChars[16])
    units = ast.literal_eval(allChars[18])
    additionalItems = ast.literal_eval(allChars[20])

    # lists the important characteristics of the randomly selected meal file
    #           0          1          2         3          4         5         6          7          8       9              10
    return [mealChoice, servings, faffCheck, pieCheck, mainCarb, mealType, meatType, ingredients, amounts, units, additionalItems]

def generatemenu():
    """Using the mealselector function the meal choices are made and the characteristics are evaluated to return a menu which .
    """
    import os
    from menufunctions_win import mealselector

    while True:
        mealChoice_1 = mealselector()
        mealChoice_2 = mealselector()
        mealChoice_3 = mealselector()
        mealChoice_4 = mealselector()

        if mealChoice_1[2] + mealChoice_2[2] + mealChoice_3[2] + mealChoice_4[2] == 1: # check for faff
            faffCheck = 1
        else:
            faffCheck = 0

        if mealChoice_1[3] + mealChoice_2[3] + mealChoice_3[3] + mealChoice_4[3] == 0: # check for pie
            pieCheck = 1
        else:
            pieCheck = 0
        if len(set([mealChoice_1[4], mealChoice_2[4], mealChoice_3[4], mealChoice_4[4]])) == 4: # check for carb types
            carbCheck = 1
        else:
            carbCheck = 0
        if len(set([mealChoice_1[5], mealChoice_2[5], mealChoice_3[5], mealChoice_4[5]])) == 3: # check for meal type
            typeCheck = 1
        else:
            typeCheck = 0
        if [mealChoice_1[5], mealChoice_2[5], mealChoice_3[5], mealChoice_4[5]].count('Meat') == 2:
            meatList = list([mealChoice_1[6], mealChoice_2[6], mealChoice_3[6], mealChoice_4[6]])
            uniqueMeats = []
            for i in meatList:
                if i not in uniqueMeats and i != 'No meat':
                    uniqueMeats.append(i)
            if len(uniqueMeats) == 2:
                meatCheck = 1
            else:
                meatCheck = 0
        elif [mealChoice_1[5], mealChoice_2[5], mealChoice_3[5], mealChoice_4[5]].count('Meat') == 1:
            meatList = list([mealChoice_1[6], mealChoice_2[6], mealChoice_3[6], mealChoice_4[6]])
            meatList = [x for x in meatList if x != 'No meat']
            meatCheck = 1
        else:
            meatCheck = 0
        if mealChoice_1[1][0] + mealChoice_2[1][0] + mealChoice_3[1][0] + mealChoice_4[1][0] == 7:
            servingCheck = 1
        else:
            servingCheck = 0
        if len(set([mealChoice_1[0],mealChoice_2[0],mealChoice_3[0],mealChoice_4[0]])) == 4:
            nameCheck = 1
        else:
            nameCheck = 0
        if faffCheck + carbCheck + typeCheck + meatCheck + servingCheck + nameCheck + pieCheck == 7:
            break
    return([mealChoice_1,mealChoice_2,mealChoice_3,mealChoice_4])

def generatepie():
    """Using the mealselector function the meal choices are made and the characteristics are evaluated to return a menu which .
    """
    import os
    from menufunctions_win import mealselector

    while True:
        mealChoice_1 = mealselector()
        mealChoice_2 = mealselector()
        mealChoice_3 = mealselector()
        mealChoice_4 = mealselector()

        if mealChoice_1[3] + mealChoice_2[3] + mealChoice_3[3] + mealChoice_4[3] == 1: # check for faff, later this will be the check for pie
            pieCheck = 1
        else:
            pieCheck = 0
        if len(set([mealChoice_1[4], mealChoice_2[4], mealChoice_3[4], mealChoice_4[4]])) == 4: # check for carb types
            carbCheck = 1
        else:
            carbCheck = 0
        if len(set([mealChoice_1[5], mealChoice_2[5], mealChoice_3[5], mealChoice_4[5]])) == 3: # check for meal type
            typeCheck = 1
        else:
            typeCheck = 0
        if [mealChoice_1[5], mealChoice_2[5], mealChoice_3[5], mealChoice_4[5]].count('Meat') == 2:
            meatList = list([mealChoice_1[6], mealChoice_2[6], mealChoice_3[6], mealChoice_4[6]])
            uniqueMeats = []
            for i in meatList:
                if i not in uniqueMeats and i != 'No meat':
                    uniqueMeats.append(i)
            if len(uniqueMeats) == 2:
                meatCheck = 1
            else:
                meatCheck = 0
        elif [mealChoice_1[5], mealChoice_2[5], mealChoice_3[5], mealChoice_4[5]].count('Meat') == 1:
            meatList = list([mealChoice_1[6], mealChoice_2[6], mealChoice_3[6], mealChoice_4[6]])
            meatList = [x for x in meatList if x != 'No meat']
            meatCheck = 1
        else:
            meatCheck = 0
        if mealChoice_1[1][0] + mealChoice_2[1][0] + mealChoice_3[1][0] + mealChoice_4[1][0] == 7:
            servingCheck = 1
        else:
            servingCheck = 0
        if len(set([mealChoice_1[0],mealChoice_2[0],mealChoice_3[0],mealChoice_4[0]])) == 4:
            nameCheck = 1
        else:
            nameCheck = 0
        if pieCheck + carbCheck + typeCheck + meatCheck + servingCheck + nameCheck == 6:
            break
    return([mealChoice_1,mealChoice_2,mealChoice_3,mealChoice_4])

def generatenew():
    """Using the mealselector function the meal choices are made and the characteristics are evaluated to return a menu which .
    """
    import os
    import random
    from menufunctions_win import mealselector

    while True:
        mealChoice_1 = mealselector()
        mealChoice_2 = mealselector()
        mealChoice_3 = mealselector()
        mealChoice_4 = mealselector()

        if mealChoice_1[2] + mealChoice_2[2] + mealChoice_3[2] + mealChoice_4[2] == 1: # check for faff
            faffCheck = 1
        else:
            faffCheck = 0

        if mealChoice_1[3] + mealChoice_2[3] + mealChoice_3[3] + mealChoice_4[3] == 0: # check for pie
            pieCheck = 1
        else:
            pieCheck = 0
        if len(set([mealChoice_1[4], mealChoice_2[4], mealChoice_3[4], mealChoice_4[4]])) == 4: # check for carb types
            carbCheck = 1
        else:
            carbCheck = 0
        if len(set([mealChoice_1[5], mealChoice_2[5], mealChoice_3[5], mealChoice_4[5]])) == 3: # check for meal type
            typeCheck = 1
        else:
            typeCheck = 0
        if [mealChoice_1[5], mealChoice_2[5], mealChoice_3[5], mealChoice_4[5]].count('Meat') == 2:
            meatList = list([mealChoice_1[6], mealChoice_2[6], mealChoice_3[6], mealChoice_4[6]])
            uniqueMeats = []
            for i in meatList:
                if i not in uniqueMeats and i != 'No meat':
                    uniqueMeats.append(i)
            if len(uniqueMeats) == 2:
                meatCheck = 1
            else:
                meatCheck = 0
        elif [mealChoice_1[5], mealChoice_2[5], mealChoice_3[5], mealChoice_4[5]].count('Meat') == 1:
            meatList = list([mealChoice_1[6], mealChoice_2[6], mealChoice_3[6], mealChoice_4[6]])
            meatList = [x for x in meatList if x != 'No meat']
            meatCheck = 1
        else:
            meatCheck = 0
        if mealChoice_1[1][0] + mealChoice_2[1][0] + mealChoice_3[1][0] + mealChoice_4[1][0] == 7:
            servingCheck = 1
        else:
            servingCheck = 0
        if len(set([mealChoice_1[0],mealChoice_2[0],mealChoice_3[0],mealChoice_4[0]])) == 4:
            nameCheck = 1
        else:
            nameCheck = 0
        if faffCheck + carbCheck + typeCheck + meatCheck + servingCheck + nameCheck + pieCheck == 7:
            break

    newCheck = [mealChoice_1,mealChoice_2,mealChoice_3,mealChoice_4]
    mealChange = random.choice(newCheck)
    newCheck[newCheck.index(mealChange)] = ['New Meal', mealChange[1], mealChange[2], 0, mealChange[4], mealChange[5], mealChange[6], [], [], [], []]
    return([newCheck[0],newCheck[1],newCheck[2],newCheck[3]])

def generatelist(confirmedMenu):
    """confimredMenu is generated before running this function and  that contains the 4 chosen meals as lists and is outside the function (= to generatemenu()).
    It also contains the uniqueMeats list which is used in this function during development, but won't be used in the main program.
    Remember mealChoice_x indexing is:

        0          1          2         3          4         5         6          7          8       9              10
    mealChoice, servings, faffCheck, pieCheck, mainCarb, mealType, meatType, ingredients, amounts, units, additionalItems
    """

    import os
    import datetime

    #gives an appropriate variable to each meal choice list
    mealChoice_1 = confirmedMenu[0]
    mealChoice_2 = confirmedMenu[1]
    mealChoice_3 = confirmedMenu[2]
    mealChoice_4 = confirmedMenu[3]

    mealAms_1 = mealChoice_1[8]
    mealAms_2 = mealChoice_2[8]
    mealAms_3 = mealChoice_3[8]
    mealAms_4 = mealChoice_4[8]

    #halves the ingredient amounts for the multiple servings meal (if present)
    while True:
        if mealChoice_1[1][0] == 1 and mealChoice_1[1][1] == 2:
            mealAms_1 = []
            for i in mealChoice_1[8]:
                mealAms_1.append(round(i/2,1))
            break
        elif mealChoice_2[1][0] == 1 and mealChoice_2[1][1] == 2:
            mealAms_2 = []
            for i in mealChoice_2[8]:
                mealAms_2.append(round(i/2,1))
            break
        elif mealChoice_3[1][0] == 1 and mealChoice_3[1][1] == 2:
            mealAms_3 = []
            for i in mealChoice_3[8]:
                mealAms_3.append(round(i/2,1))
            break
        elif mealChoice_4[1][0] == 1 and mealChoice_4[1][1] == 2:
            mealAms_4 = []
            for i in mealChoice_4[8]:
                mealAms_4.append(round(i/2,1))
            break
        else:
            break

    allIngs = mealChoice_1[7] + mealChoice_2[7] + mealChoice_3[7] + mealChoice_4[7] #all ingredients

    noDupIngs = [] #all ingredients no duplicated items
    for i in allIngs:
        if i not in noDupIngs:
            noDupIngs.append(i)

    dupIngs = [] #all duplicated items
    for i in noDupIngs:
        if allIngs.count(i) > 1:
            dupIngs.append(i)

    #summing amounts from the various duplicated ingredients and appending to a list with indexes corresponding to the indexes
    #of dupIngs
    #note that mealAms_x is used instead of mealChoice_x[8] due to the potentail presence of a multiple serving meal with
    #modified amounts
    checkQ = 0
    dupIngsAms = []
    while checkQ != len(dupIngs):
        currDup = dupIngs[checkQ]

        amCurrDupMeal_1 = 0
        amCurrDupMeal_2 = 0
        amCurrDupMeal_3 = 0
        amCurrDupMeal_4 = 0

        try:
            amCurrDupMeal_1 = mealAms_1[mealChoice_1[7].index(currDup)]
        except ValueError:
            pass
        try:
            amCurrDupMeal_2 = mealAms_2[mealChoice_2[7].index(currDup)]
        except ValueError:
            pass
        try:
            amCurrDupMeal_3 = mealAms_3[mealChoice_3[7].index(currDup)]
        except ValueError:
            pass
        try:
            amCurrDupMeal_4 = mealAms_4[mealChoice_4[7].index(currDup)]
        except ValueError:
            pass

        currDupAm = amCurrDupMeal_1 + amCurrDupMeal_2 + amCurrDupMeal_3 + amCurrDupMeal_4
        dupIngsAms.append(currDupAm)
        checkQ += 1

    #examining the units of the duplicated items across all the meal choices and appending to a list with indexes corresponding
    #to the indexes of dupIngs
    #an error will be flagged if the units across duplicated ingredients do not match
    checkQ = 0
    dupIngsUnits = []
    while checkQ != len(dupIngs):
        currDup = dupIngs[checkQ]

        unCurrDupMeal_1 = ''
        unCurrDupMeal_2 = ''
        unCurrDupMeal_3 = ''
        unCurrDupMeal_4 = ''

        try:
            unCurrDupMeal_1 = mealChoice_1[9][mealChoice_1[7].index(currDup)]
        except ValueError:
            pass
        try:
            unCurrDupMeal_2 = mealChoice_2[9][mealChoice_2[7].index(currDup)]
        except ValueError:
            pass
        try:
            unCurrDupMeal_3 = mealChoice_3[9][mealChoice_3[7].index(currDup)]
        except ValueError:
            pass
        try:
            unCurrDupMeal_4 = mealChoice_4[9][mealChoice_4[7].index(currDup)]
        except ValueError:
            pass

        unCurrDupList = [unCurrDupMeal_1, unCurrDupMeal_2, unCurrDupMeal_3, unCurrDupMeal_4]
        try:
            unCurrDupList.remove('')
            unCurrDupList.remove('')
        except ValueError:
            pass
        unCurrDupList = list(set(unCurrDupList))

        if len(unCurrDupList) != 1:
            unitError = '***In the meal files selected, check the units are consistent between duplicated ingerdients***'

        dupIngsUnits.append(unCurrDupList[0])
        checkQ += 1

    #concatenating the amounts and units of only the duplicated items into a list with indexes corresponding to the indexes
    #of dupIngs
    dupRange = list(range(0,len(dupIngs)))
    dupAmsUnits = []
    for i in dupRange:
        dupAmsUnits.append(str(dupIngsAms[i]) + ' ' + dupIngsUnits[i])

    #generates a dictionary containing all ingredients as keys and the amounts and units as values from both the duplicated items
    #and th unique items
    ingsAmsUnits = {}
    for i in noDupIngs:
        if i in dupIngs:
            ingsAmsUnits.update({i:dupAmsUnits[dupIngs.index(i)]})
        else:
            try:
                ingsAmsUnits.update({i:str(mealAms_1[mealChoice_1[7].index(i)]) + ' ' + mealChoice_1[9][mealChoice_1[7].index(i)]})
            except ValueError:
                pass
            try:
                ingsAmsUnits.update({i:str(mealAms_2[mealChoice_2[7].index(i)]) + ' ' + mealChoice_2[9][mealChoice_2[7].index(i)]})
            except ValueError:
                pass
            try:
                ingsAmsUnits.update({i:str(mealAms_3[mealChoice_3[7].index(i)]) + ' ' + mealChoice_3[9][mealChoice_3[7].index(i)]})
            except ValueError:
                pass
            try:
                ingsAmsUnits.update({i:str(mealAms_4[mealChoice_4[7].index(i)]) + ' ' + mealChoice_4[9][mealChoice_4[7].index(i)]})
            except ValueError:
                pass

    #making the list.txt file with timestanp in the format year-month-date-hour-minute-second. Will change this to just the
    #date after development
    timeStampFormat = 'List made on %Y-%m-%d-%H-%M-%S'
    listFile = open(str(os.getcwd() + '\\' + datetime.datetime.now().strftime(timeStampFormat) + '.txt'), 'w')

    while True:
        if mealChoice_1[1][0] == 1:
            mealChoice_1[0] = str(mealChoice_1[0] + ' (1)')
            break
        elif mealChoice_2[1][0] == 1:
            mealChoice_2[0] = str(mealChoice_2[0] + ' (1)')
            break
        elif mealChoice_3[1][0] == 1:
            mealChoice_3[0] = str(mealChoice_3[0] + ' (1)')
            break
        elif mealChoice_4[1][0] == 1:
            mealChoice_4[0] = str(mealChoice_4[0] + ' (1)')
            break
        else:
            servError = '***In the meal files selected, check one of the selected meals is a single or multiple meal***'
            break

    #write errors if any to list file
    try:
        listFile.write(unitError + '\n')
    except NameError:
        pass
    try:
        listFile.write(servError + '\n')
    except NameError:
        pass

    # writes meal names to the listfile
    listFile.write('Meals:\n')
    listFile.write(mealChoice_1[0] + '\n')
    listFile.write(mealChoice_2[0] + '\n')
    listFile.write(mealChoice_3[0] + '\n')
    listFile.write(mealChoice_4[0] + '\n\n')

    #writes the ingredients and amounts + units to the list file
    listFile.write('Ingredients:\n')
    listList =  []
    for key in ingsAmsUnits:
        x = str(key + " - " + ingsAmsUnits[key])
        listList.append(x)
        listFile.write(x + '\n')
    listFile.write('\n')

    #generate list of additional items for all the meal choices and write to list file
    addItemsTotal = mealChoice_1[10] + mealChoice_2[10] + mealChoice_3[10] + mealChoice_4[10]
    addItems = []
    for i in addItemsTotal:
        if i not in addItems:
            addItems.append(i)
    listFile.write('Additional items:\n')
    for i in addItems:
        listFile.write(i + '\n')
    listFile.close()

    return(listList)
