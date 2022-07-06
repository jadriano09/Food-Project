import random

print('Hello and hi there! What food are you up for today?')
print('Hit enter after every entry, and hit "Q" to quit.')

list_of_foods = []

while True:
    food = input()
    if food == "":
        print("You cannot eat nothing. Please type something.")
    elif str.lower(food) == 'q':
        break
    list_of_foods.append(food)

for i in list_of_foods:
    if i == '':
        list_of_foods.remove('')

print("You're gonna eat", random.choice(list_of_foods))
print('\n')


recipe1 = []
recipe2 = []
recipe3 = []


print("This program will now take the recipe's of the top three meals you would like to cook.")
print("First, we'll start by recording the ingredients in your desired recipes.")
print("List the ingredients that go into the first recipe. Hit enter to list the next ingredient; hit 'Q' to start "
      "the next recipe.")
while True:
    ingredients1 = input()
    if str.lower(ingredients1) == 'q':
        break
    recipe1.append(ingredients1)

print('Now, list the ingredients for the second recipe.')
print("Hit enter to list the next ingredient; hit 'Q' to start the next recipe.")
while True:
    ingredients2 = input()
    if str.lower(ingredients2) == 'q':
        break
    recipe2.append(ingredients2)

print("Let's start on the last recipe.")
print("List the ingredients of the last recipe; hit enter to list the last ingredient and hit 'Q' when you're finished")
while True:
    ingredients3 = input()
    if str.lower(ingredients3) == 'q':
        break
    recipe3.append(ingredients3)


dict1 = {'ingredients': recipe1}
dict2 = {'ingredients': recipe2}
dict3 = {'ingredients': recipe3}

print('What is the name of the first recipe?')
dict1["Name"] = input()

print('What is the name of your second recipe?')
dict2["Name"] = input()

print('What is the name of your last recipe?')
dict3["Name"] = input()

fridge = []
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
    print("You're gonna make " + dict1['Name'])
if recipe2_points > recipe1_points and recipe2_points > recipe3_points:
    print("You're gonna make " + dict2['Name'])
if recipe3_points > recipe1_points and recipe3_points > recipe2_points:
    print("You're gonna make " + dict3['Name'])
