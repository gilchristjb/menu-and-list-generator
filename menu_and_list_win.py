def generate_menu_and_list():
    """The main function in the entire program. Using the lineprint function the 
    meal choices are made and then if they all meet the desired menu characteristics. 
    If they do, then one of the single meal files is halved (to get seven meals) 
    and the list file is built and written to the cwd. """
    
    import os
    import datetime
    from lineprints_win import lineprint_m1
    from lineprints_win import lineprint_m2
    from lineprints_win import lineprint_m3
    from lineprints_win import lineprint_m4
     
    # running lineprint functions to get the meal files and the characteristics of that meal
    DLSDbqNGCK = 0 # while loop to check randomly selected meals fit the menu characteristics
    while DLSDbqNGCK == 0:       
        meal_choice_m1 = lineprint_m1()
        meal_choice_m2 = lineprint_m2()
        meal_choice_m3 = lineprint_m3()
        meal_choice_m4 = lineprint_m4()    
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