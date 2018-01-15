from menufunctions_win import newmeal, mealchange, deletemeal, meallist, generate_menu_and_list, mealselector, generatemenu, generatelist

while True:
    try:
        choice = int(input("""What do you want to do (enter a number)?\n\n
            1 - Add a meal\n
            2 - Change a meal\n
            3 - Delete a meal\n
            4 - Generate a menu and list\n
            5 - Exit\n
            \n"""))
        if choice == 1:
            newmeal()
        if choice == 2:
            mealchange()
        if choice == 3:
            deletemeal()
        if choice == 4:
            generate_menu_and_list()
        if choice == 5:
            print('\nEnjoy your meals, goodbye!')
            break
        if choice == 6:
            print(meallist())
        if choice == 7:
            print(mealselector())
        if choice == 8:
            generatemenu()
        if choice == 9:
            proposedMenu = generatemenu()
            generatelist()
    except ValueError:
        print('Please enter a number between 1 and 5')
