import random

class Animal:  # PascalCase

    # class level data
    animals = []

    map = [ #multidimensional array
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
    ]

    def __init__(self, name, species, age, energy=100): # self = instance level data
        self.name = name
        self.species = species
        self.age = age

        self.energy = energy
        self.location = {'x': 0, 'y': 0}

        Animal.add_animal(self)

    def get_description(self):
        return f"{self.name} is a {self.species} and is {self.age} years old."

    def walk(self, distance):
        self.energy -= distance
        return f"{self.name} walked {distance} kilometers and lost {distance} energy!"

    def eat(self, food, energy):
        self.energy += energy
        return f"{self.name} ate {food} and gained {energy} energy!"
    
    @classmethod
    def pass_time(cls):
        for animal in cls.animals:
            animal.energy -= 1
    
        return True
    
    @classmethod
    def add_animal(cls, animal):
        cls.animals.append(animal)
        def random_x_y():
            x = random.randint(0,9)
            y = random.randint(0,9)
            return x,y
        x,y = random_x_y()
        while cls.map[y][x] == animal:
            x,y = random_x_y()
        cls.map[y][x] = animal
        animal.location['x'] = x
        animal.location['y'] = y
        print(f'animal location has been updated to {animal.location}')
        return animal.location

        """
            Challenge:
                - add_animal
                    - add to map
                        - randomly place animal on map
                            - update animal's location
                        - cannot be placed on top of another animal

        """

test = Animal('test', 'test', 10, 100)
test2 = Animal('test', 'test', 10, 100)
test3 = Animal('test', 'test', 10, 100)
test4 = Animal('test', 'test', 10, 100)

