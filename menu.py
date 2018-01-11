from menufunctions_win import newmeal, mealchange, deletemeal, meallist, generate_menu_and_list

number_of_options_1 = 5
option_range = list(range(1,number_of_options_1 + 1))
ddpegobzcw = 0
while ddpegobzcw != 1:
    check_gxSm = 0
    while check_gxSm != 1:
        try:
            #simple number menu, needs more options within mian listed options, e.g. for
            #change meal, needs to have the option to change specific ingredients and
            #amounts or running a pie menu
            choice = int(input("""What do you want to do (enter a number)?\n\n
            1 - Add a meal\n
            2 - Change a meal\n
            3 - Delete a meal\n
            4 - Generate a menu and list\n
            5 - Exit\n
            \n"""))
            if choice not in option_range:
                print('Please enter a number between 1 and ' + str(number_of_options_1) + '.')
            else:
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
                    check_gxSm = 1
                    ddpegobzcw = 1
        except ValueError:
            print('Please enter a number between 1 and ' + str(number_of_options_1) + '.')
