import random

list_of_foods = []

recipe1 = []
recipe2 = []
recipe3 = []

fridge = []

dict1 = {'ingredients': recipe1}
dict2 = {'ingredients': recipe2}
dict3 = {'ingredients': recipe3}

print("Hello there! Would you like to eat out today, or stay at home and cook?")
choice = input("Type 'out' to eat outside, or 'home' to eat inside. \n").strip().lower()

while True:
    if choice == "out":
        print("\nNice! What genre of food are you in the mood for? Press 'Q' once you list all your choices")
        while True:
            food = input()
            if food == "":
                print("You can't eat nothing. Please type something")
            elif str.lower(food) == 'q':
                break
            list_of_foods.append(food)

        for i in list_of_foods:
            if i == '':
                list_of_foods.remove('')

        print("You're gonna eat", random.choice(list_of_foods)+"! Enjoy!")

    elif choice == "home":
        print("Great choice! Here's how this will work: ")
        print("First, we're gonna have you list the names of the three receipes that you're willing to cook.")
        print("Once you name your receipes, we're going to have you list the ingredients that you use for each reciepes")
        print("After that, you're going to list the ingredients that you see in your fridge.")
        print("Once you list all your ingredients, we'll tell you what you're going to cook.")

        print('What is the name of the first recipe?')
        dict1["Name"] = input()

        print('What is the name of your second recipe?')
        dict2["Name"] = input()

        print('What is the name of your last recipe?')
        dict3["Name"] = input()

        print("\nNow, what are the ingredients you use for", dict1["Name"] + "?")
        print("Hit enter to list the next ingredient; hit 'q' to move on.")

        while True:
            ingredients1 = input()
            if str.lower(ingredients1) == 'q':
                break
            recipe1.append(ingredients1)

        print('Now, list the ingredients for', dict2["Name"]+".")

        while True:
            ingredients2 = input()
            if str.lower(ingredients2) == 'q':
                break
            recipe2.append(ingredients2)

        print("List the ingredients of", dict3["Name"] + ".")

        while True:
            ingredients3 = input()
            if str.lower(ingredients3) == 'q':
                break
            recipe3.append(ingredients3)

        print("What items do you currently have that you can cook with?")
        print("Hit enter to add a new ingredient; hit 'Q' when you list all your ingredients")

        while True:
            available_ingredients = input()
            if str.lower(available_ingredients) == 'q':
                break
            fridge.append(available_ingredients)

        recipe1_points = 0
        recipe2_points = 0
        recipe3_points = 0

        a = set(recipe1)
        b = set(recipe2)
        c = set(recipe3)
        d = set(fridge)

        for i in d.intersection(a):
            recipe1_points += 1
        for i in d.intersection(b):
            recipe2_points += 1
        for i in d.intersection(c):
            recipe3_points += 1

        if recipe1_points > recipe2_points and recipe1_points > recipe3_points:
            print("You're gonna make " + dict1['Name']+"! Enjoy!")
        if recipe2_points > recipe1_points and recipe2_points > recipe3_points:
            print("You're gonna make " + dict2['Name']+"! Enjoy!")
        if recipe3_points > recipe1_points and recipe3_points > recipe2_points:
            print("You're gonna make " + dict3['Name']+"! Enjoy!")

    else:
        print("INVALID RESPONSE. PLEASE TRY AGAIN ")
        choice = input().strip().lower()