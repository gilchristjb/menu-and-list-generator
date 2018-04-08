from menufunctions_win import newmeal, mealchange, deletemeal, meallist, clearCLI, mealselector, generatemenu, generatepie, generatelist, generatenew, menuprint
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
                                menuprint(proposedMenu)
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
                                menuprint(proposedMenu)
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
                                menuprint(proposedMenu)
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
            time.sleep(3)
        if optChoice == 8:
            time.sleep(3)
        if optChoice == 9:
            menuprint(generatemenu())
            time.sleep(3)
    except ValueError:
        print('Please enter a number between 1 and 5')
