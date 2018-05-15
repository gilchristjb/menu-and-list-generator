def meallist():
    """Function to check if there is a directory called 'recipe_book'
    in the cwd, and creates one if it is not present. It then creates and
    returns a list of all the meals present in the recipe_book directory.
    """
    import os

    recipeFiles = os.listdir(os.path.join(os.getcwd(), 'recipe_book'))
    mealList = [x.split('.')[0] for x in recipeFiles]

    return(mealList)

def clearCLI():
    """Clears the CLI when either on Linux or Windows. Prints that it can't
    identify the OS or reports an error if not.
    """
    import platform
    import os

    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    else:
        print('Cannot determine OS, so cannot run clearCLI function')

def newmeal():
    """Function checks to see if there is a directory called 'recipe_book
    in the cwd, and creates one if it's not present. It then allows a user to
    input a new meal by listing the number of ingredients and their amounts.
    Then a file is written with the title, number of servings and the ingredient
    list and amounts. Testing.
    Testing.
    """
    import os
    import time
    from menufunctions_win import meallist, clearCLI

    #setting the title and ingredients, amounts and unit lists
    mealList = meallist()

    while True:
        clearCLI()
        title = input('What is the meal name? ').title()
        if title in mealList:
            print('That is already a meal, please choose another meal name')
            time.sleep(3)
            continue
        if title not in mealList:
            ingredients = []
            amounts = []
            units = []
            while True:
                clearCLI()
                if len(ingredients) != 0:
                    for i in ingredients:
                        print(i, amounts[ingredients.index(i)], units[ingredients.index(i)])
                    print("")
                else:
                    pass
                current_ing = input('Name an ingredient or enter "end" to exit\n').title()
                if current_ing == 'End':
                    break
                else:
                    while True:
                        try:
                            ing_am = float(input('How much of this ingredient?\n'))
                            break
                        except ValueError:
                            print("Please enter a number")
                    ing_unit = input('what is the unit?\n').lower()
                    ingredients.append(current_ing)
                    amounts.append(ing_am)
                    units.append(ing_unit)
        break

    #set number of days meal will be for, one or two days only
    while True:
        clearCLI()
        for i in ingredients:
            print(i, amounts[ingredients.index(i)], units[ingredients.index(i)])
        servQuest = input('\nHow many days will it be for (one or two days only)?\n').lower()
        if servQuest == '1' or servQuest == 'one':
            servings = 'One day'
            break
        elif servQuest == '2' or servQuest == 'two':
            while True:
                clearCLI()
                for i in ingredients:
                    print(i, amounts[ingredients.index(i)], units[ingredients.index(i)])
                print('\nHow many days will it be for (one or two days only)?')
                print(servQuest)
                dayQuest = input('\nCan this also be for one day? (y/n)\n').lower()
                if dayQuest == 'y' or dayQuest == 'yes':
                    servings = 'One or two days'
                    break
                elif dayQuest == 'n' or dayQuest == 'no':
                    servings = 'Two days'
                    break
                else:
                    print('That does not make sense')
                    time.sleep(3)
            break
        else:
            print('That does not make sense')
            time.sleep(3)

    #set if this is a pie meal
    while True:
        clearCLI()
        for i in ingredients:
            print(i, amounts[ingredients.index(i)], units[ingredients.index(i)])
        print('\n' + servings + '\n')
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
        clearCLI()
        if pie == 'Pie':
            faff = 'Faffy'
            break
        else:
            pass
        for i in ingredients:
            print(i, amounts[ingredients.index(i)], units[ingredients.index(i)])
        print('\n' + servings + '\n' + pie + '\n')
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
        clearCLI()
        for i in ingredients:
            print(i, amounts[ingredients.index(i)], units[ingredients.index(i)])
        print('\n' + servings + '\n' + pie + '\n' + faff + '\n')
        carbQuest = input('What is the main carbohydrate (pasta, rice, bread, couscous, potato)? ').title()
        if carbQuest in carbList:
            break
        else:
            print('That does not make sense')

    #set the meal type (vegetarian, fish or meat)
    while True:
        clearCLI()
        for i in ingredients:
            print(i, amounts[ingredients.index(i)], units[ingredients.index(i)])
        print('\n' + servings + '\n' + pie + '\n' + faff + '\n' + carbQuest + '\n')
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
        clearCLI()
        for i in ingredients:
            print(i, amounts[ingredients.index(i)], units[ingredients.index(i)])
        print('\n' + servings + '\n' + pie + '\n' + faff + '\n' + carbQuest + '\n' + mealType + '\n' + meatQuest + '\n' + ', '.join(additionalItems))
        #print(', '.join(additionalItems))
        current_additional = input('\nWhat additional items might be needed (type "end" to quit)? ').title()
        if current_additional == 'End':
            break
        else:
            additionalItems.append(current_additional)

    #creation of the meal file txt file with all the parameters set previously
    filePath = os.path.join(os.getcwd(), 'recipe_book', str(title + '.txt'))
    ingredients = str(ingredients)
    amounts = str(amounts)
    units = str(units)
    additionalItems = str(additionalItems)
    file = open(filePath, 'w')
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
    clearCLI()
    print('New meal "' + title + '" created!\n')
    print(servings)
    print(faff)
    print(pie)
    print(carbQuest)
    print(mealType)
    print(meatQuest)
    print(ingredients)
    print(amounts)
    print(units)
    print(additionalItems)
    input('\nPress enter to continue\n')

def mealchange():
    """This function changes characteristics of a meal file.
    Last edit 2018-01-23
    """

    import os
    import ast
    import time

    #choosing what meal is to be chnaged
    while True:
        clearCLI()
        mealList = meallist()
        for i in mealList:
            print(i)
        print('')
        changeMeal = input('What meal do you want to change?\n').title()
        if changeMeal not in mealList:
            print('\nThat is not a listed meal.')
            time.sleep(3)
        else:
            break

    #generating the filepath to the .txt document
    #opening as read and extracting the meal characteristics into a list (mealChars) except for
    #ingredients, amounts, units and additional items which have their own variables
    changeFile = os.path.join(os.getcwd(), 'recipe_book', str(changeMeal + '.txt'))

    with open(changeFile,"r") as tempChangeFile:

        mealChars = []
        withN = tempChangeFile.readlines()
        for i in withN:
            mealChars.append(i.rstrip('\n'))

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

        #options to choose from
        clearCLI()
        print('Changing "' + changeMeal + '.txt"\nType "end" anytime to go back\nType "finalize" to commit the changes to the meal file\n')
        print('Servings? ' + mealChars[2])
        print('Pie? ' + mealChars[6])
        print('Faff? ' + mealChars[4])
        print('Main carbohydrate: ' + mealChars[8])
        print('Meal type: ' + mealChars[10])
        print('Meat type: ' + mealChars[12])
        print('\nIngredients, amounts and units:')
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
                clearCLI()
                print('Changing "' + changeMeal + '.txt"\nType "end" anytime to go back\nType "finalize" to commit the changes to the meal file\n')
                print('Servings? ' + mealChars[2])
                print('Pie? ' + mealChars[6])
                print('Faff? ' + mealChars[4])
                print('Main carbohydrate: ' + mealChars[8])
                print('Meal type: ' + mealChars[10])
                print('Meat type: ' + mealChars[12])
                print('\nIngredients, amounts and units:')
                #ingredients, amounts and units are concatenated together
                for i in ingList:
                    print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                print('\nAdditional Items:')
                print(', '.join(addIngs))

                servChoice = input('\nHow many days will this be for?\n').lower()
                if servChoice == '1' or servChoice == 'one':
                    mealChars[2] = 'One day'
                    break
                if servChoice == 'end':
                    break
                if servChoice == '2' or servChoice == 'two':
                    while True:
                        clearCLI()
                        print('Changing "' + changeMeal + '.txt"\nType "end" anytime to go back\nType "finalize" to commit the changes to the meal file\n')
                        print('Servings? ' + mealChars[2])
                        print('Pie? ' + mealChars[6])
                        print('Faff? ' + mealChars[4])
                        print('Main carbohydrate: ' + mealChars[8])
                        print('Meal type: ' + mealChars[10])
                        print('Meat type: ' + mealChars[12])
                        print('\nIngredients, amounts and units:')
                        #ingredients, amounts and units are concatenated together
                        for i in ingList:
                            print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                        print('\nAdditional Items:')
                        print(', '.join(addIngs))

                        print('\nHow many days will this be for?')
                        print(servChoice)


                        twoServChoice = input('\nCan this also be for one day (y/n)?\n').lower()
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
                            time.sleep(3)
                    break
                else:
                    print('That does not make sense.')
                    time.sleep(3)

        #changing pie status (also changes faff status if pie)
        elif changeChoice in pieResp:
            while True:
                clearCLI()
                print('Changing "' + changeMeal + '.txt"\nType "end" anytime to go back\nType "finalize" to commit the changes to the meal file\n')
                print('Servings? ' + mealChars[2])
                print('Pie? ' + mealChars[6])
                print('Faff? ' + mealChars[4])
                print('Main carbohydrate: ' + mealChars[8])
                print('Meal type: ' + mealChars[10])
                print('Meat type: ' + mealChars[12])
                print('\nIngredients, amounts and units:')
                #ingredients, amounts and units are concatenated together
                for i in ingList:
                    print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                print('\nAdditional Items:')
                print(', '.join(addIngs))

                pieChoice = input('\nIs this meal a pie (y/n)?\n').lower()
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
                    time.sleep(3)

        #changing faff status, not possible to if pie
        elif changeChoice in faffResp:
            while True:
                clearCLI()
                print('Changing "' + changeMeal + '.txt"\nType "end" anytime to go back\nType "finalize" to commit the changes to the meal file\n')
                print('Servings? ' + mealChars[2])
                print('Pie? ' + mealChars[6])
                print('Faff? ' + mealChars[4])
                print('Main carbohydrate: ' + mealChars[8])
                print('Meal type: ' + mealChars[10])
                print('Meat type: ' + mealChars[12])
                print('\nIngredients, amounts and units:')
                #ingredients, amounts and units are concatenated together
                for i in ingList:
                    print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                print('\nAdditional Items:')
                print(', '.join(addIngs))

                if mealChars[6] == 'Pie':
                    print('\nAll pies are faffy, change to "Not pie" first.')
                    time.sleep(3)
                    break
                else:
                    while True:
                        clearCLI()
                        print('Changing "' + changeMeal + '.txt"\nType "end" anytime to go back\nType "finalize" to commit the changes to the meal file\n')
                        print('Servings? ' + mealChars[2])
                        print('Pie? ' + mealChars[6])
                        print('Faff? ' + mealChars[4])
                        print('Main carbohydrate: ' + mealChars[8])
                        print('Meal type: ' + mealChars[10])
                        print('Meat type: ' + mealChars[12])
                        print('\nIngredients, amounts and units:')
                        #ingredients, amounts and units are concatenated together
                        for i in ingList:
                            print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                        print('\nAdditional Items:')
                        print(', '.join(addIngs))

                        faffChoice = (input('\nIs this a faffy meal (y/n)?\n')).lower()
                        if faffChoice == 'y' or faffChoice == 'yes':
                            mealChars[4] = 'Faffy'
                            break
                        elif faffChoice == 'n' or faffChoice == 'no':
                            mealChars[4] = 'Not faffy'
                            break
                        elif faffChoice == 'end':
                            break
                        else:
                             print('That does not make sense.')
                             time.sleep(3)
                    break

        #changing the main carbohydrate
        elif changeChoice in carbResp:
            carbList = ['Pasta','Rice','Bread','Couscous','Potato']
            while True:
                clearCLI()
                print('Changing "' + changeMeal + '.txt"\nType "end" anytime to go back\nType "finalize" to commit the changes to the meal file\n')
                print('Servings? ' + mealChars[2])
                print('Pie? ' + mealChars[6])
                print('Faff? ' + mealChars[4])
                print('Main carbohydrate: ' + mealChars[8])
                print('Meal type: ' + mealChars[10])
                print('Meat type: ' + mealChars[12])
                print('\nIngredients, amounts and units:')
                #ingredients, amounts and units are concatenated together
                for i in ingList:
                    print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                print('\nAdditional Items:')
                print(', '.join(addIngs))

                carbChoice = input('\nWhat is the main carbohydrate (pasta, rice, bread, couscous, potato)?\n').title()
                if carbChoice in carbList:
                    mealChars[8] = carbChoice
                    break
                else:
                    print('That does not make sense.')
                    time.sleep(3)

        #changine meal type (also change meat type if meat meal)
        elif changeChoice in mealResp:
            while True:
                clearCLI()
                print('Changing "' + changeMeal + '.txt"\nType "end" anytime to go back\nType "finalize" to commit the changes to the meal file\n')
                print('Servings? ' + mealChars[2])
                print('Pie? ' + mealChars[6])
                print('Faff? ' + mealChars[4])
                print('Main carbohydrate: ' + mealChars[8])
                print('Meal type: ' + mealChars[10])
                print('Meat type: ' + mealChars[12])
                print('\nIngredients, amounts and units:')
                #ingredients, amounts and units are concatenated together
                for i in ingList:
                    print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                print('\nAdditional Items:')
                print(', '.join(addIngs))

                mealChoice = input('\nWhat mealtype is this (vegetarian, fish, meat)?\n').lower()
                if mealChoice == 'vegetarian' or mealChoice == 'veg':
                    mealChars[10] = 'Vegetarian'
                    mealChars[12] = 'No meat'
                    break
                if mealChoice == 'fish':
                    mealChars[10] = 'Fish'
                    mealChars[12] = 'No meat'
                    break
                if mealChoice == 'meat':
                    mealChars[10] = 'Meat'
                    meatList = ['Poultry','Beef','Pork','Game','Lamb']
                    while True:
                        clearCLI()
                        print('Changing "' + changeMeal + '.txt"\nType "end" anytime to go back\nType "finalize" to commit the changes to the meal file\n')
                        print('Servings? ' + mealChars[2])
                        print('Pie? ' + mealChars[6])
                        print('Faff? ' + mealChars[4])
                        print('Main carbohydrate: ' + mealChars[8])
                        print('Meal type: ' + mealChars[10])
                        print('Meat type: ' + mealChars[12])
                        print('\nIngredients, amounts and units:')
                        #ingredients, amounts and units are concatenated together
                        for i in ingList:
                            print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                        print('\nAdditional Items:')
                        print(', '.join(addIngs))
                        print('\nWhat mealtype is this (vegetarian, fish, meat)?')
                        print(mealChoice)

                        meatChoice = input('\nWhat kind of meat is it (poultry, beef, pork, game, lamb)?\n').title()
                        if meatChoice in meatList:
                            mealChars[12] = meatChoice
                            break
                        if meatChoice == 'End':
                            break
                        else:
                            print('That does not make sense.')
                            time.sleep(3)
                    break
                if mealChoice == 'end':
                    break
                else:
                    print('That does not make sense.')
                    time.sleep(3)

        #change meat type is it's a meat meal
        elif changeChoice in meatResp:
            if mealChars[10] == 'Meat':
                meatList = ['Poultry','Beef','Pork','Game','Lamb']
                while True:
                    clearCLI()
                    print('Changing "' + changeMeal + '.txt"\nType "end" anytime to go back\nType "finalize" to commit the changes to the meal file\n')
                    print('Servings? ' + mealChars[2])
                    print('Pie? ' + mealChars[6])
                    print('Faff? ' + mealChars[4])
                    print('Main carbohydrate: ' + mealChars[8])
                    print('Meal type: ' + mealChars[10])
                    print('Meat type: ' + mealChars[12])
                    print('\nIngredients, amounts and units:')
                    #ingredients, amounts and units are concatenated together
                    for i in ingList:
                        print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                    print('\nAdditional Items:')
                    print(', '.join(addIngs))

                    meatChoice = input('\nWhat kind of meat is it (poultry, beef, pork, game, lamb)?\n').title()
                    if meatChoice in meatList:
                        mealChars[12] = meatChoice
                        break
                    elif meatChoice == 'End':
                        break
                    else:
                        print('That does not make sense.')
                        time.sleep(3)
            else:
                print('Change meal type to "Meat" first.')
                time.sleep(3)

        #changing ingredients, amounts and units
        elif changeChoice in ingResp or changeChoice in amResp or changeChoice in unitResp:
            while True:
                clearCLI()
                print('Ingredients, amounts and units:')
                #ingredients, amounts and units are concatenated together
                for i in ingList:
                    print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                changeOrAdd = input("""\nDo you want to add or delete an ingredient or make changes to the ingredients, amounts and units?
Enter "add", "delete" or "change".\n""").lower()
                print('')
                if changeOrAdd == 'change':
                    while True:
                        clearCLI()
                        print('Ingredients, amounts and units:')
                        for i in ingList:
                            print(i, amList[ingList.index(i)], unitList[ingList.index(i)])

                        ingChangeChoice = input("""\nWhat do you want to change? The ingrediets, amounts or units?\n""").lower()
                        if ingChangeChoice in ingResp:
                            while True:
                                clearCLI()
                                print('Ingredients, amounts and units:')
                                for i in ingList:
                                    print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                                ingChoice = input('\nWhich ingredient do you want to change?\n').title()
                                if ingChoice in ingList:
                                    changeIndex = ingList.index(ingChoice)
                                    clearCLI()
                                    ingList[changeIndex] = input('What do you want to replace it with?\n').title()
                                    amList[changeIndex] = int(input('What is the amount?\n'))
                                    unitList[changeIndex] = input('In what unit?\n').lower()
                                    break
                                elif ingChoice == 'End':
                                    break
                                else:
                                    print('That does not make sense.')
                                    time.sleep(3)

                        elif ingChangeChoice in amResp:
                            while True:
                                clearCLI()
                                print('Ingredients, amounts and units:')
                                for i in ingList:
                                    print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                                amChoice = input('\nWhat ingredient do you want to change the amount of?\n').title()
                                if amChoice in ingList:
                                    try:
                                        changeIndex = ingList.index(amChoice)
                                        amList[changeIndex] = int(input('\nWhat is the new amount?\n'))
                                        break
                                    except ValueError:
                                        print('\nOUCH! Only enter numbers please!\n')
                                        time.sleep(3)
                                        break
                                if amChoice == 'End':
                                    break
                                else:
                                    print('That does not make sense.')
                                    time.sleep(3)

                        elif ingChangeChoice in unitResp:
                            while True:
                                clearCLI()
                                print('Ingredients, amounts and units:')
                                for i in ingList:
                                    print(i, amList[ingList.index(i)], unitList[ingList.index(i)])
                                unitChoice = input('\nWhat ingredient do you want to change the unit of?\n').title()
                                if unitChoice in ingList:
                                    changeIndex = ingList.index(unitChoice)
                                    unitList[changeIndex] = input('\nWhat is the new unit?\n').lower()
                                    break
                                if unitChoice == 'End':
                                    break
                                else:
                                    print('That does not make sense.')
                                    time.sleep(3)

                        elif ingChangeChoice == 'end':
                            break
                        else:
                            print('That does not make sense.')
                            time.sleep(3)

                elif changeOrAdd == 'add':

                    while True:
                        clearCLI()
                        addIngChoice = input('What ingredient do you want to add?\n').title()
                        if addIngChoice == 'End':
                            break
                        else:
                            while True:
                                try:
                                    addAmChoice = int(input('What is the amount?\n'))
                                    break
                                except ValueError:
                                    print('Please only enter numbers!')

                            addUnitChoice = input('In what unit?\n').lower()
                            print('')

                            ingList.append(addIngChoice)
                            amList.append(addAmChoice)
                            unitList.append(addUnitChoice)

                elif changeOrAdd == 'delete' or changeOrAdd == 'del':
                    while True:
                        clearCLI()
                        print('Ingredients, amounts and units:')
                        for i in ingList:
                            print(i, amList[ingList.index(i)], unitList[ingList.index(i)])

                        delIngChoice = input("""\nWhat ingredient do you want to delete?\n""").title()
                        if delIngChoice in ingList:
                            print('Deleting:', delIngChoice + ',', amList[ingList.index(delIngChoice)], unitList[ingList.index(delIngChoice)] + '\n')
                            del amList[ingList.index(delIngChoice)]
                            del unitList[ingList.index(delIngChoice)]
                            del ingList[ingList.index(delIngChoice)]
                            time.sleep(3)

                        elif delIngChoice == 'End':
                            break
                        else:
                            print('That is not an ingredient')
                            time.sleep(3)

                elif changeOrAdd == 'end':
                    break
                else:
                    print('That does not make sense.')
                    time.sleep(3)

        #changing additional items
        elif changeChoice in addResp:
            while True:
                clearCLI()
                print('Additional Items:')
                for i in addIngs:
                    print(i)
                addOrChange = input("""\nDo you want to add, change or delete an additional item?
Type "add", "change" or "delete".\n""").lower()
                if addOrChange == 'change':
                    while True:
                        clearCLI()
                        print('Additional Items:')
                        for i in addIngs:
                            print(i)
                        changeItemChoice = input('\nWhat additional item do you want to change?\n').title()
                        if changeItemChoice in addIngs:
                            newItemChoice = input('\nWhat do you want to change it to?\n').title()
                            addIngs[addIngs.index(changeItemChoice)] = newItemChoice
                        elif changeItemChoice == 'End':
                            break
                        else:
                            print('\nThat is not an additional item.\n')
                            time.sleep(3)

                elif addOrChange == 'add':
                    while True:
                        clearCLI()
                        print('Additional Items:')
                        for i in addIngs:
                            print(i)
                        addItemChoice = input('\nWhat additional item do you want to add?\n').title()
                        if addItemChoice == 'End':
                            break
                        else:
                            addIngs.append(addItemChoice)

                elif addOrChange == 'delete' or addOrChange == 'del':
                    while True:
                        clearCLI()
                        print('Additional Items:')
                        for i in addIngs:
                            print(i)
                        deleteItemChoice = input('\nWhat Item do you want to delete?\n').title()
                        if deleteItemChoice in addIngs:
                            addIngs.pop(addIngs.index(deleteItemChoice))
                            print('\n' + deleteItemChoice + ' deleted!\n')
                            time.sleep(3)
                        elif deleteItemChoice == 'End':
                            break
                        elif deleteItemChoice not in addIngs:
                            print('\nThat is not an additional item.\n')

                elif addOrChange == 'end':
                    break
                else:
                    print('That does not make sense.')

        #finilaize change and write to meal file
        elif changeChoice == 'finalize':
            with open(changeFile,'w') as tempChangeFile:
                tempChangeFile.write(changeMeal + '\n\n')
                tempChangeFile.write(mealChars[2] + '\n\n')
                tempChangeFile.write(mealChars[4] + '\n\n')
                tempChangeFile.write(mealChars[6] + '\n\n')
                tempChangeFile.write(mealChars[8] + '\n\n')
                tempChangeFile.write(mealChars[10] + '\n\n')
                tempChangeFile.write(mealChars[12] + '\n\n')
                tempChangeFile.write(str(ingList) + '\n\n')
                tempChangeFile.write(str(amList) + '\n\n')
                tempChangeFile.write(str(unitList) + '\n\n')
                tempChangeFile.write(str(addIngs))
            tempChangeFile.close()
            print('Mealfile finalized.\n')
            time.sleep(3)
            break

        #go back option
        elif changeChoice == 'end':
            break

        #default error response
        elif changeChoice not in servResp + pieResp + faffResp + carbResp + mealResp + meatResp + ingResp + addResp or changeChoice != 'finalize':
            print('That does not make sense.')
            time.sleep(3)

def deletemeal():
    """This function will give the option to delete a meal file in the
    recipe_book directory."""

    import os
    import time
    from menufunctions_win import meallist, clearCLI

    #choosing the file for deletion
    while True:
        clearCLI()
        mealList = meallist()
        for i in mealList:
            print(i)
        delQuest = input("""\nWhat meal do you want to remove?
Type "End" to go back.\n""").title()
        if delQuest == 'End':
            break
        elif delQuest not in mealList:
            print('That is not a meal on the list!')
            time.sleep(3)
        else:
            #deletion check
            while True:
                print('\nAre you sure you want to delete "' + delQuest + '" (y/n)?')
                delCheck = input('\n').lower()
                if delCheck == 'yes' or delCheck == 'y':
                    delPath = os.path.join(os.getcwd(), 'recipe_book', str(delQuest + '.txt'))
                    os.remove(delPath)
                    #end process
                    print(delQuest + '.txt deleted!\n')
                    time.sleep(3)
                    break
                elif delCheck == 'no' or delCheck == 'n':
                    break
                else:
                    print('\nThat does not make sense.')
                    time.sleep(3)

def mealselector():
    """ This function randomly chooses a meal file for meal 1 and asigns the characheristics
    of that meal file to a list which can then be sliced returning the desired
    characteristics.
    """
    import os
    import ast
    import random
    from menufunctions_win import meallist, clearCLI

    #randomly chooses a meal from meallist and finds the file path
    mealChoice = str(random.choice(meallist()))
    choicePath = os.path.join(os.getcwd(), 'recipe_book', str(mealChoice + '.txt'))

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
    from menufunctions_win import mealselector, clearCLI

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
    from menufunctions_win import mealselector, clearCLI

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
    from menufunctions_win import mealselector, clearCLI

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

    timeStampFormat = 'List made on %Y-%m-%d-%H-%M-%S.txt'
    listFileName = datetime.datetime.now().strftime(timeStampFormat)
    listFile = open(os.path.join(os.getcwd(), listFileName), 'w')

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

def menuprint(proposedMenu):
    """Given a suitable menu list of meal characteristics (proposedMenu), this will print the important ones in an easy to read format.
    """
    #meal 1
    print(proposedMenu[0][0])
    if proposedMenu[0][1][0] == 2:
        print(' - ' + str(proposedMenu[0][1][0]) + ' days')
    else:
        print(' - ' + str(proposedMenu[0][1][0]) + ' day')
    print(' - ' + str(proposedMenu[0][4]))
    if proposedMenu[0][5] == 'Meat':
        print(' - ' + str(proposedMenu[0][5]) + ' (' + str(proposedMenu[0][6]) + ')')
    else:
        print(' - ' + str(proposedMenu[0][5]))
    if proposedMenu[0][2] == 1:
        print(' - Faffy\n')
    else:
        print(' - Not faffy\n')

    #meal 2
    print(proposedMenu[1][0])
    if proposedMenu[1][1][0] == 2:
        print(' - ' + str(proposedMenu[1][1][0]) + ' days')
    else:
        print(' - ' + str(proposedMenu[1][1][0]) + ' day')
    if proposedMenu[1][5] == 'Meat':
        print(' - ' + str(proposedMenu[1][5]) + ' (' + str(proposedMenu[1][6]) + ')')
    else:
        print(' - ' + str(proposedMenu[1][5]))
    if proposedMenu[1][2] == 1:
        print(' - Faffy\n')
    else:
        print(' - Not faffy\n')

    #meal 3
    print(proposedMenu[2][0])
    if proposedMenu[2][1][0] == 2:
        print(' - ' + str(proposedMenu[2][1][0]) + ' days')
    else:
        print(' - ' + str(proposedMenu[2][1][0]) + ' day')
    if proposedMenu[2][5] == 'Meat':
        print(' - ' + str(proposedMenu[2][5]) + ' (' + str(proposedMenu[2][6]) + ')')
    else:
        print(' - ' + str(proposedMenu[2][5]))
    if proposedMenu[2][2] == 1:
        print(' - Faffy\n')
    else:
        print(' - Not faffy\n')

    #meal 4
    print(proposedMenu[3][0])
    if proposedMenu[3][1][0] == 2:
        print(' - ' + str(proposedMenu[3][1][0]) + ' days')
    else:
        print(' - ' + str(proposedMenu[3][1][0]) + ' day')
    if proposedMenu[3][5] == 'Meat':
        print(' - ' + str(proposedMenu[3][5]) + ' (' + str(proposedMenu[3][6]) + ')')
    else:
        print(' - ' + str(proposedMenu[3][5]))
    if proposedMenu[3][2] == 1:
        print(' - Faffy\n')
    else:
        print(' - Not faffy\n')
