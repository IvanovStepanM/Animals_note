##Personal_petrmation## this program manages 3 instances of personal petrmation
##It uploads menu from user_interface file and contains instructions for entered commands.

import pickle                           # technical imports

import Pet       # imports of *.py files from working directory
from user_interface import user_interface
from idgenerator import idgenerator
# Global constants for menu choices
ADD = 1
LOOK_UP = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'mypets.dat'

def main():                             ## main function loads pets and checks user's menu choice
    pet = load_pet()              # loads pets from data file
    choice = 0 # variable for user's choice

    while choice != QUIT:               
        choice = user_interface.get_menu_choice()   # loads user interface from user_interface.py
        if choice == LOOK_UP:               # here it checks what user have entered
            look_up(pet)                # and calls for a function to execute. In this case - to show pet by ID.
        elif choice == ADD:                 # Here- to add a new pet
            add(pet)
            save_pet(pet) # save a new pet to the file
        elif choice == CHANGE:
            change(pet)
            save_pet(pet) # save changed pet to the file
        elif choice == DELETE:
            delete(pet)
            save_pet(pet) # save changed pet to the file


        

# now we define all the functions listed above as actions from the menu related to the pets


def load_pet():       # This function loads pets from a database
    try:
        input_file = open(FILENAME, 'rb') # open the pets file (binary, reading)
        pet_dct = pickle.load(input_file)
        input_file.close()
    except IOError: # if can't open the file
        pet_dct = {} # then create an empty dictionary
    return pet_dct

def save_pet(pet):    # This function saves pets back to database.
    output_file = open(FILENAME, 'wb') # writing, binary code
    pickle.dump(pet, output_file) # pickle the dictionary and save it.
    output_file.close()

def look_up(pet): # show pet
    print("Show by animal type or show all? (select an option number):")
    print("[1] Dog [2] Cat [3] Fish [4] Reptilia [5] Insect [6] Other [7] Show all")    # Shows options.

    try:
        type_choice = int(input('>[Enter a number]: '))       # User enters 1-7
        choice_to_show = animal_type_set(type_choice)        # The number is converted to an animal
        if type_choice == 1 or type_choice == 2 or type_choice == 3 or type_choice == 4 or type_choice == 5 or type_choice == 6:
            beast_count = sum([1 for i in pet if pet[i].get_animal_type() == choice_to_show])
            print('There are %i %s(s).' % (beast_count, choice_to_show))
            for id in pet:                                 # prints all animals of a chosen type.
                if pet[id].get_animal_type() == choice_to_show:
                    print(pet.get(id, 'no pet found'))
                    print()
                                                               
        elif type_choice == 7:                                  # Alternatively, prints all the animals.
            beast_count = len(list(pet))
            print('There are %i animals in the database.' % (beast_count))
            for id in list(pet):
                print(pet.get(id, 'no pet found'))              
                print("__________________________")             
    except ValueError:
        print('you have entered an empty string or non-integer value.')

def add(pet):   # This function adds a new pet.
    try:
        inputs_number = int(input("How many pets to enter: "))
    
        for beast in range(inputs_number):
            print('Regarding animal №%i' % (beast+1))
            name = input("Pet's name:") # user inputs title for a new pet

            print('[1] Dog [2] Cat [3] Fish [4] Reptilia [5] Insect [6] Other')
            user_is_stupid = 1
            while user_is_stupid != 0:
                try:
                    type_choice = int(input('Animal type: '))
                    animal_type = animal_type_set(type_choice)
                    user_is_stupid = 0
                except ValueError:
                    print('Please enter an integer number.')
            age = input('Age, full years:')
            id = idgenerator.main()

            entry = Pet.Pet(id, name, animal_type, age) # create pet object
            pet[id] = entry
            print('Animal added with ID: %i.' % (id))
    except ValueError:
        print('You have successfully entered a non-integer value for the number of pets.')

    
def change(pet):                    # This function changes the existing pet.
    try:
        id = int(input("Enter pet's ID: "))  # by its ID.

        if id in pet:
            name = input('Name:') # user inputs
            print('[1] Dog [2] Cat [3] Fish [4] Reptilia [5] Insect [6] Other')
            user_is_stupid = 1
            while user_is_stupid != 0:
                try:
                    type_choice = int(input('Animal type: '))
                    animal_type = animal_type_set(type_choice)
                    user_is_stupid = 0
                except ValueError:
                    print('Please enter an integer number.')
            age = input('Age, full years:')

            entry = Pet.Pet(id, name, animal_type, age) # creates a Personal_petrmation instance.
            pet[id] = entry
            print('Information updated.')
        else:
            print('There is no pet with this ID.')
    except ValueError:
        print('you have entered an empty string or non-integer value.')

def delete(pet):                            # This function deletes pet by its ID.
    try:
        id = int(input('Enter the ID of the pet to delete: '))
             
        # If ID is found, delete the entry.
        if id in pet:
            del pet[id]
            print('Entry deleted.')
        else:
            print('There is no pet with this ID.')

    except ValueError:
        print('you have entered an empty string')

def animal_type_set(type_choice):
        try:
                        
            if type_choice == 1:
                animal_type = 'Dog'
                return animal_type
            elif type_choice == 2:
                animal_type = 'Cat'
                return animal_type
            elif type_choice == 3:
                animal_type = 'Fish'
                return animal_type
            elif type_choice == 4:
                animal_type = 'Reptilia'
                return animal_type
            elif type_choice == 5:
                animal_type = 'Insect'
                return animal_type
            elif type_choice == 6:
                animal_type = 'Other'
                return animal_type
            else:
                print('Just type a number 1-7.')
            
        except ValueError:
            print('Just type a number.')
main()