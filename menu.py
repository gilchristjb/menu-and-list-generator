from menufunctions_win import newmeal, mealchange, deletemeal, meallist, mealselector, generatemenu, generatepie, generatelist, generatenew

while True:
    try:
        optChoice = int(input("""What do you want to do (enter a number)?\n\n
            1 - Add a meal\n
            2 - Change a meal\n
            3 - Delete a meal\n
            4 - Generate a menu and list\n
            5 - Exit\n
            \n"""))
        if optChoice == 1:
            newmeal()
        if optChoice == 2:
            mealchange()
        if optChoice == 3:
            deletemeal()
        if optChoice == 4:
            while True:
                try:
                    menuChoice = int(input("""What do you want to do (enter a number)?\n\n
            1 - Generate a regular menu\n
            2 - Generate a pie menu\n
            3 - Generate a menu with a new meal\n
            4 - Go back\n
            \n\n"""))
                    if menuChoice == 1:
                        while True:
                            try:
                                proposedMenu = generatemenu()
                                print('\n')
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
                                regChoice = int(input("""Looks tasty?\n\n
            1 - Yeah!\n
            2 - Nah, re-roll!\n
            3 - Go back\n
            \n"""))
                                if regChoice == 1:
                                    confirmedMenu = proposedMenu
                                    listList = generatelist(confirmedMenu)
                                    print('\nIngredients\n')
                                    for i in listList:
                                        print(i)
                                    print('')
                                    #menuChoice = 4
                                    #optChoice = 5
                                    break
                                if regChoice == 2:
                                    continue
                                if regChoice == 3:
                                    break
                            except ValueError:
                                print('Please enter a number between 1 and 2')
                    if menuChoice == 2:
                        while True:
                            try:
                                proposedMenu = generatepie()
                                print('\n')
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
                                print(proposedMenu[1][0])

                                if proposedMenu[1][1][0] == 2:
                                    print(' - ' + str(proposedMenu[1][1][0]) + ' days')
                                else:
                                    print(' - ' + str(proposedMenu[1][1][0]) + ' day')

                                print(' - ' + str(proposedMenu[1][4]))
                                if proposedMenu[1][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[1][5]) + ' (' + str(proposedMenu[1][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[1][5]))
                                if proposedMenu[1][2] == 1:
                                    print(' - Faffy\n')
                                else:
                                    print(' - Not faffy\n')
                                print(proposedMenu[2][0])

                                if proposedMenu[2][1][0] == 2:
                                    print(' - ' + str(proposedMenu[2][1][0]) + ' days')
                                else:
                                    print(' - ' + str(proposedMenu[2][1][0]) + ' day')

                                print(' - ' + str(proposedMenu[2][4]))
                                if proposedMenu[2][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[2][5]) + ' (' + str(proposedMenu[2][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[2][5]))
                                if proposedMenu[2][2] == 1:
                                    print(' - Faffy\n')
                                else:
                                    print(' - Not faffy\n')
                                print(proposedMenu[3][0])

                                if proposedMenu[3][1][0] == 2:
                                    print(' - ' + str(proposedMenu[3][1][0]) + ' days')
                                else:
                                    print(' - ' + str(proposedMenu[3][1][0]) + ' day')

                                print(' - ' + str(proposedMenu[3][4]))
                                if proposedMenu[3][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[3][5]) + ' (' + str(proposedMenu[3][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[3][5]))
                                if proposedMenu[3][2] == 1:
                                    print(' - Faffy\n')
                                else:
                                    print(' - Not faffy\n')
                                pieChoice = int(input("""Looks tasty?\n\n
            1 - Yeah!\n
            2 - Nah, re-roll!\n
            3 - Go back\n
            \n"""))
                                if pieChoice == 1:
                                    confirmedMenu = proposedMenu
                                    listList = generatelist(confirmedMenu)
                                    print('\nIngredients\n')
                                    for i in listList:
                                        print(i)
                                    print('')
                                    #menuChoice = 4
                                    #optChoice = 5
                                    break
                                if pieChoice == 2:
                                    continue
                                if pieChoice == 3:
                                    break
                            except ValueError:
                                print('Please enter a number between 1 and 2')
                    if menuChoice == 3:
                        while True:
                            try:
                                proposedMenu = generatenew()
                                print('\n')
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
                                print(proposedMenu[1][0])

                                if proposedMenu[1][1][0] == 2:
                                    print(' - ' + str(proposedMenu[1][1][0]) + ' days')
                                else:
                                    print(' - ' + str(proposedMenu[1][1][0]) + ' day')

                                print(' - ' + str(proposedMenu[1][4]))
                                if proposedMenu[1][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[1][5]) + ' (' + str(proposedMenu[1][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[1][5]))
                                if proposedMenu[1][2] == 1:
                                    print(' - Faffy\n')
                                else:
                                    print(' - Not faffy\n')
                                print(proposedMenu[2][0])

                                if proposedMenu[2][1][0] == 2:
                                    print(' - ' + str(proposedMenu[2][1][0]) + ' days')
                                else:
                                    print(' - ' + str(proposedMenu[2][1][0]) + ' day')

                                print(' - ' + str(proposedMenu[2][4]))
                                if proposedMenu[2][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[2][5]) + ' (' + str(proposedMenu[2][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[2][5]))
                                if proposedMenu[2][2] == 1:
                                    print(' - Faffy\n')
                                else:
                                    print(' - Not faffy\n')
                                print(proposedMenu[3][0])

                                if proposedMenu[3][1][0] == 2:
                                    print(' - ' + str(proposedMenu[3][1][0]) + ' days')
                                else:
                                    print(' - ' + str(proposedMenu[3][1][0]) + ' day')

                                print(' - ' + str(proposedMenu[3][4]))
                                if proposedMenu[3][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[3][5]) + ' (' + str(proposedMenu[3][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[3][5]))
                                if proposedMenu[3][2] == 1:
                                    print(' - Faffy\n')
                                else:
                                    print(' - Not faffy\n')
                                newChoice = int(input("""Looks tasty?\n\n
            1 - Yeah!\n
            2 - Nah, re-roll!\n
            3 - Go back\n
            \n"""))
                                if newChoice == 1:
                                    confirmedMenu = proposedMenu
                                    listList = generatelist(confirmedMenu)
                                    print('\nIngredients\n')
                                    for i in listList:
                                        print(i)
                                    print('')
                                    #menuChoice = 4
                                    #optChoice = 5
                                    break
                                if newChoice == 2:
                                    continue
                                if newChoice == 3:
                                    break
                            except ValueError:
                                print('Please enter a number between 1 and 2')
                    if menuChoice == 4:
                        break
                except ValueError:
                    print('Please enter a number between 1 and 4')
        if optChoice == 5:
            print('\nEnjoy your meals, goodbye!')
            break
        if optChoice == 6:
            mealchange()
        if optChoice == 7:
            print(mealselector())
        if optChoice == 8:
            generatemenu()
        if optChoice == 9:
            confirmedMenu = generatemenu()
            generatelist(confirmedMenu)
    except ValueError:
        print('Please enter a number between 1 and 5')
