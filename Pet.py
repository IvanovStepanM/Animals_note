class Pet:  # 
    # The _ _init_ _ method initializes the attributes.
    def __init__(self, id, name, animal_type, age):
        self.__id = id
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age


    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def set_id(self, id):
        self.__id = id



    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def get_id(id):
        return self.__id




    def __str__(self):                              # attributes to show
        return 'Id: ' + str(self.__id) + \
            '\nName: ' + str(self.__name) + \
            '\nAnimal_type: ' + str(self.__animal_type) + \
            '\nAge (years): ' + str(self.__age)