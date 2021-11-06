# This program generates unique ID for a new pet.
class idgenerator:

    def main():
            import random
            import pickle
            FILENAME = 'mypets.dat'
            id_is_unique = 0        # parameter for stopping to stopping the generanor cycle
            
            try:
                input_file = open(FILENAME, 'rb') # open the pets file (binary, reading)
                pets_dct = pickle.load(input_file)
                input_file.close()
            except EOFError:    # if can't open the file
                pets_dct = {} # then create an empty dictionary.
            id = random.randint(0, 9)   # First let's generate a random number from 0 to 9 to make id search easy.
            if id in pets_dct:             # If such number alreay exists then
                id = random.randint(10, 99)      # let's try a two-digit number for id. (this is initial part when there are few pets)
                if id in pets_dct:              # this part if needed for a bigger size of the dictionary.
                                                 # untill this part there is a small chance that the value is not uniqe.
                                                 # However:

                    while id_is_unique != 1:        # loop until the ID is unique, if it is not unique.
                        if id in pets_dct:
                            id = random.randint(10, 99)
                            id_is_unique = 0
                        else:
                            id_is_unique = 1
                            return id
                else:
                    return id 
            else:
                return id
    main()

#idgenerator.main()