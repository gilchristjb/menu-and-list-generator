from menufunctions_win import newmeal, mealchange, deletemeal, meallist, generate_menu_and_list

optRange_1 = list(range(1,7))
optStr_1 = []
for i in optRange_1:
    optStr_1.append(str(i))

while True:
    try:
        choice = input("""What do you want to do (enter a number)?\n\n
            1 - Add a meal\n
            2 - Change a meal\n
            3 - Delete a meal\n
            4 - Generate a menu and list\n
            5 - Exit\n
            \n""")
        if choice in optStr_1:
            if choice == '1':
                newmeal()
            if choice == '2':
                mealchange()
            if choice == '3':
                deletemeal()
            if choice == '4':
                generate_menu_and_list()
            if choice == '5':
                print('\nEnjoy your meals, goodbye!')
                break
            if choice == '6':
                print(meallist())
    except ValueError:
        print('Please enter a number between 1 and 5')