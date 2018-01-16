from menufunctions_win import newmeal, mealchange, deletemeal, meallist, mealselector, generatemenu, generatepie, generatelist

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
            4 - Exit\n
            \n\n"""))
                    if menuChoice == 1:

                        while True:
                            try:
                                proposedMenu = generatemenu()
                                print('\n')
                                print(proposedMenu[0][0])
                                print(' - ' + str(proposedMenu[0][1][0]) + ' days')
                                print(' - ' + str(proposedMenu[0][4]))
                                if proposedMenu[0][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[0][5]) + ' (' + str(proposedMenu[0][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[0][5]))
                                if proposedMenu[0][2] == 1:
                                    print(' - Faffy')
                                else:
                                    print(' - Not faffy')
                                print(proposedMenu[1][0])
                                print(' - ' + str(proposedMenu[1][1][0]) + ' days')
                                print(' - ' + str(proposedMenu[1][4]))
                                if proposedMenu[1][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[1][5]) + ' (' + str(proposedMenu[1][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[1][5]))
                                if proposedMenu[1][2] == 1:
                                    print(' - Faffy')
                                else:
                                    print(' - Not faffy')
                                print(proposedMenu[2][0])
                                print(' - ' + str(proposedMenu[2][1][0]) + ' days')
                                print(' - ' + str(proposedMenu[2][4]))
                                if proposedMenu[2][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[2][5]) + ' (' + str(proposedMenu[2][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[2][5]))
                                if proposedMenu[2][2] == 1:
                                    print(' - Faffy')
                                else:
                                    print(' - Not faffy')
                                print(proposedMenu[3][0])
                                print(' - ' + str(proposedMenu[3][1][0]) + ' days')
                                print(' - ' + str(proposedMenu[3][4]))
                                if proposedMenu[3][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[3][5]) + ' (' + str(proposedMenu[3][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[3][5]))
                                if proposedMenu[3][2] == 1:
                                    print(' - Faffy')
                                else:
                                    print(' - Not faffy\n')
                                regChoice = int(input("""Looks tasty?\n\n
            1 - Yeah!\n
            2 - Nah, re-roll!\n
            \n\n"""))
                                if regChoice == 1:
                                    confirmedMenu = proposedMenu
                                    generatelist(confirmedMenu)
                                    menuChoice = 4
                                    optChoice = 5
                                    break
                                if regChoice == 2:
                                    continue
                            except ValueError:
                                print('Please enter a number between 1 and 2')
                    if menuChoice == 2:
                        while True:
                            try:
                                proposedMenu = generatepie()
                                print('\n')
                                print(proposedMenu[0][0])
                                print(' - ' + str(proposedMenu[0][1][0]) + ' days')
                                print(' - ' + str(proposedMenu[0][4]))
                                if proposedMenu[0][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[0][5]) + ' (' + str(proposedMenu[0][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[0][5]))
                                if proposedMenu[0][2] == 1:
                                    print(' - Faffy')
                                else:
                                    print(' - Not faffy')
                                print(proposedMenu[1][0])
                                print(' - ' + str(proposedMenu[1][1][0]) + ' days')
                                print(' - ' + str(proposedMenu[1][4]))
                                if proposedMenu[1][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[1][5]) + ' (' + str(proposedMenu[1][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[1][5]))
                                if proposedMenu[1][2] == 1:
                                    print(' - Faffy')
                                else:
                                    print(' - Not faffy')
                                print(proposedMenu[2][0])
                                print(' - ' + str(proposedMenu[2][1][0]) + ' days')
                                print(' - ' + str(proposedMenu[2][4]))
                                if proposedMenu[2][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[2][5]) + ' (' + str(proposedMenu[2][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[2][5]))
                                if proposedMenu[2][2] == 1:
                                    print(' - Faffy')
                                else:
                                    print(' - Not faffy')
                                print(proposedMenu[3][0])
                                print(' - ' + str(proposedMenu[3][1][0]) + ' days')
                                print(' - ' + str(proposedMenu[3][4]))
                                if proposedMenu[3][5] == 'Meat':
                                    print(' - ' + str(proposedMenu[3][5]) + ' (' + str(proposedMenu[3][6]) + ')')
                                else:
                                    print(' - ' + str(proposedMenu[3][5]))
                                if proposedMenu[3][2] == 1:
                                    print(' - Faffy')
                                else:
                                    print(' - Not faffy\n')
                                regChoice = int(input("""Looks tasty?\n\n
            1 - Yeah!\n
            2 - Nah, re-roll!\n
            \n\n"""))
                                if regChoice == 1:
                                    confirmedMenu = proposedMenu
                                    generatelist(confirmedMenu)
                                    menuChoice = 4
                                    optChoice = 5
                                    break
                                if regChoice == 2:
                                    continue
                            except ValueError:
                                print('Please enter a number between 1 and 2')
                    if menuChoice == 3:
                        pass
                    if menuChoice == 4:
                        break
                except ValueError:
                    print('Please enter a number between 1 and 4')
        if optChoice == 5:
            print('\nEnjoy your meals, goodbye!')
            break
        if optChoice == 6:
            print(meallist())
        if optChoice == 7:
            print(mealselector())
        if optChoice == 8:
            generatemenu()
        if optChoice == 9:
            confirmedMenu = generatemenu()
            generatelist(confirmedMenu)
    except ValueError:
        print('Please enter a number between 1 and 5')
