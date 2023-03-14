# Student Database 2.0

stu_dict_list = [
    {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
    {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
    {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
]
# creating empty list from dictionaries
names = []
hometown = []
favorite_food = []

for s in stu_dict_list:
    names.append((s['name']))
    hometown.append((s['hometown']))
    favorite_food.append((s['favorite_food']))

def list_names(names):
    for name in range(len(names)):
        print(str(name+1) + '.', names[name])

def stu_info():
    name_index = input("Would you like to enter student names or numbers?\n")
    if name_index == 'names':
        search = input("Which student would you like to learn more about? Enter a name\n")
        if search in names:
            if names.index(search) == 0:
                print(f"Student 1 is {names[0]}. What would you like to know?")
                info_select = input("Enter 'hometown' or 'favorite food'")
                info_select = info_select.lower()
                if info_select == 'hometown':
                    print(f"{names[0]} is from {hometown[0]}")
                elif info_select == 'favorite food':
                    print(f"{names[0]}'s favorite food is {favorite_food[0]}")
            elif names.index(search) == 1:
                print(f"Student 2 is {names[1]}. What would you like to know?")
                info_select = input("Enter 'hometown' or 'favorite food'")
                info_select = info_select.lower()
                if info_select == 'hometown':
                    print(f"{names[1]} is from {hometown[1]}")
                elif info_select == 'favorite food':
                    print(f"{names[1]}'s favorite food is {favorite_food[1]}")
            elif names.index(search) == 2:
                print(f"Student 3 is {names[2]}. What would you like to know?")
                info_select = input("Enter 'hometown' or 'favorite food'")
                info_select = info_select.lower()
                if info_select == 'hometown':
                    print(f"{names[2]} is from {hometown[2]}")
                elif info_select == 'favorite food':
                    print(f"{names[2]}'s favorite food is {favorite_food[2]}")
            else:
                print(f"Student 4 is {names[3]}. What would you like to know?")
                info_select = input("Enter 'hometown' or 'favorite food'")
                info_select = info_select.lower()
                if info_select == 'hometown':
                    print(f"{names[3]} is from {hometown[3]}")
                elif info_select == 'favorite food':
                    print(f"{names[3]}'s favorite food is {favorite_food[3]}")
        else:
            print('Please enter a student from the list.')
    elif name_index == 'numbers':
        search = input("Which student would you like to learn more about? Enter a number\n")
        if search == '1':
            print(f"Student 1 is {names[0]}. What would you like to know?")
            info_select = input("Enter 'hometown' or 'favorite food'")
            info_select = info_select.lower()
            if info_select == 'hometown':
                print(f"{names[0]} is from {hometown[0]}")
            elif info_select == 'favorite food':
                print(f"{names[0]}'s favorite food is {favorite_food[0]}")
        elif search == '2':
            print(f"Student 2 is {names[1]}. What would you like to know?")
            info_select = input("Enter 'hometown' or 'favorite food'")
            info_select = info_select.lower()
            if info_select == 'hometown':
                print(f"{names[1]} is from {hometown[1]}")
            elif info_select == 'favorite food':
                print(f"{names[1]}'s favorite food is {favorite_food[1]}")
        elif search == '3':
            print(f"Student 3 is {names[2]}. What would you like to know?")
            info_select = input("Enter 'hometown' or 'favorite food'")
            info_select = info_select.lower()
            if info_select == 'hometown':
                print(f"{names[2]} is from {hometown[2]}")
            elif info_select == 'favorite food':
                print(f"{names[2]}'s favorite food is {favorite_food[2]}")
        elif search == '4':
            print(f"Student 4 is {names[3]}. What would you like to know?")
            info_select = input("Enter 'hometown' or 'favorite food'")
            info_select = info_select.lower()
            if info_select == 'hometown':
                print(f"{names[3]} is from {hometown[3]}")
            elif info_select == 'favorite food':
                print(f"{names[3]}'s favorite food is {favorite_food[3]}")
        else:
            print('Please enter a number in range')
    else:
        print("Please enter names or numbers")



# list_names(names)
def get_new_student():
    stu_name = input("What is the student's name?\n")
    stu_hometown = input("What is the student's hometown?\n")
    stu_favorite_food = input("What is the student's favorite food?\n")
    new_student = {
        'name': stu_name,
        'hometown': stu_hometown,
        'favorite_food': stu_favorite_food
    }
    names.append(new_student['name'])
    hometown.append(new_student['hometown'])
    favorite_food.append(new_student['favorite_food'])
    return new_student


# input code below
switch = True
while switch == True:
    selection = input("Please select which action you'd like to do: add, view, or quit\n")
    selection = selection.lower()
    if selection == 'add':
        stu_dict_list.append(get_new_student())
    elif selection == 'view':
        list_names(names)
        stu_info()
    elif selection == 'quit':
        print("Thank you. <END PROGRAM>")
        switch = False
        break
    else:
        print("Invalid selection, please enter a value given")
