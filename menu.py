from menufunctions_win import newmeal, mealchange, deletemeal, meallist, clearCLI, mealselector, generatemenu, generatepie, generatelist, generatenew
import os
import time

while True:
    try:
        clearCLI()
        optChoice = int(input("""What do you want to do (enter a number)?\n\n
            1 - Add a meal\n
            2 - Change a meal\n
            3 - Delete a meal\n
            4 - Generate a menu and list\n
            5 - Exit\n
            \n"""))
        if optChoice == 1:
            clearCLI()
            newmeal()
        if optChoice == 2:
            clearCLI()
            mealchange()
        if optChoice == 3:
            clearCLI()
            deletemeal()
            clearCLI()
        if optChoice == 4:
            while True:
                try:
                    clearCLI()
                    menuChoice = int(input("""What do you want to do (enter a number)?\n\n
            1 - Generate a regular menu\n
            2 - Generate a pie menu\n
            3 - Generate a menu with a new meal\n
            4 - Go back\n
            \n\n"""))
                    if menuChoice == 1:
                        while True:
                            try:
                                clearCLI()
                                proposedMenu = generatemenu()
                                print(proposedMenu[0][0]) #better to have a function to print the meal characteristics rather than 50 lines of print statements
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
            3 - Go back\n"""))
                                if regChoice == 1:
                                    confirmedMenu = proposedMenu
                                    listList = generatelist(confirmedMenu)
                                    clearCLI()
                                    print('Ingredients\n')
                                    for i in listList:
                                        print(i)
                                    print('')
                                    input('Press enter to continue\n')
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
                                clearCLI()
                                proposedMenu = generatepie()
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
            3 - Go back\n"""))
                                if pieChoice == 1:
                                    confirmedMenu = proposedMenu
                                    listList = generatelist(confirmedMenu)
                                    clearCLI()
                                    print('Ingredients\n')
                                    for i in listList:
                                        print(i)
                                    print('')
                                    input('Press enter to continue\n')
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
                                clearCLI()
                                proposedMenu = generatenew()
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
            3 - Go back\n"""))
                                if newChoice == 1:
                                    confirmedMenu = proposedMenu
                                    listList = generatelist(confirmedMenu)
                                    clearCLI()
                                    print('Ingredients\n')
                                    for i in listList:
                                        print(i)
                                    print('')
                                    input('Press enter to continue\n')
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
            clearCLI()
            print('Enjoy your meals, goodbye!')
            time.sleep(1)
            clearCLI()
            break
        if optChoice == 6:
            print(meallist())
            time.sleep(3)
        if optChoice == 7:
            print(mealselector())
        if optChoice == 8:
            generatemenu()
        if optChoice == 9:
            confirmedMenu = generatemenu()
            generatelist(confirmedMenu)
    except ValueError:
        print('Please enter a number between 1 and 5')
