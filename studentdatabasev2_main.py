

def list_names(name_list):
    for name in name_list:
        print(f'{name_list.index(name)+1}. {name}')

def get_new_student():

    stu_name = input("What is the student's name?\n")
    stu_hometown = input("What is the student's hometown?\n")
    stu_favorite_food = input("What is the student's favorite food?\n")
    if stu_name == '' or stu_hometown == '' or stu_favorite_food == '':
        print('Please enter values.')
    new_student = {
        'name': stu_name,
        'hometown': stu_hometown,
        'favorite_food': stu_favorite_food
    }

    return new_student

stu_dict_list = [
  { "name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow" },
  { "name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza" },
  { "name": "Julia", "hometown": "Houston", "favorite_food": "shrimp" }
]
def get_names():
    name_list = []
    for student_dict in stu_dict_list:
        values = list(student_dict.values())
        for name in range(0, len(values), 3):
            name_list.append(values[name])
    return name_list

def name_index():
    more_info = input("Which student would you like to know more about? ").title()
    for students in stu_dict_list:
        if more_info == students['name']:
            print(f'Student {stu_dict_list.index(students)+1} is {more_info} and their\n'
                  f'favorite food is {students["favorite_food"]} and they are from {students["hometown"]}.')
        else:
            print('Please enter a correct value.')
            break

switch = True
while switch == True:
    selection = input("Please select the action you'd like to do: add, view, or quit.\n").lower()
    if(selection == 'add'):
        stu_dict_list.append(get_new_student())

    elif selection == 'view':
        list_names(get_names())
        name_search = input("Would you like to search by name? (y/n) ").lower()
        while name_search == 'y':
            name_index()
            choice = input('Would you like to search by name again? (y/n) ').lower()
            if choice == 'n':
                break
        else:
            more_info = int(input(f'Which student would like to know more about? Enter 1 - {len(get_names())}\n'))
            if more_info in range(len(get_names())+1):
                print(f'Student {more_info} is {get_names()[more_info-1]}. What would you like to know?')
                category = input('Enter "hometown" or "favorite food" ').lower()
                if category == 'hometown':
                    print(f"{get_names()[more_info-1]} is from {stu_dict_list[more_info-1][category]}")
                elif category == 'favorite food' or category == 'food':
                    print(f"{get_names()[more_info-1]}'s favorite food is {stu_dict_list[more_info]['favorite_food']}")

    elif selection == 'quit':
        print('Thank you. <END PROGRAM>')
        break
    else:
        print("Please enter a valid action.")
