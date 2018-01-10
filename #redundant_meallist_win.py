def meallist():
    """This function checks to see if there is a directory called 'recipe_book'
    in the cwd, and creates one if it's not present. It then creates a list of
    all the meals present in the recipe_book directory.
    """
    import os

    #checks for and creation of the recipe_book directory
    recipe_book_path = str(os.getcwd() + '\\recipe_book')
    if not os.path.exists(recipe_book_path):
        os.makedirs(recipe_book_path)

    #lists all the files in the recipe_book
    recipe_book_list = os.listdir(recipe_book_path)

    #makes a list with no .txt extention
    meal_list = [recipe_book_list[i].strip('.txt') for i in range(len(recipe_book_list))]
    return(meal_list)