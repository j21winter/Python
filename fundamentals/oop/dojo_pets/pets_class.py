class Pet:
    def __init__(self, name, type, tricks, health=100, energy=100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    
    def sleep(self):
        self.energy = self.energy + 25
        print('pet slept')
        return self
    
    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print('pet ate')
        return self
    
    def play(self):
        self.health = self.health + 5
        print('pet played')
        return self
    
    def noise(self):
        if self.type == 'dog':
            print("woof")
            return self
        if self.type == 'cat':
            print('meow')
            return self
        else:
            print('you have an odd animal')
            return self

class Dog(Pet):
    def __init__(self, name, tricks, health=100, energy=100):
        super().__init__(self, name, tricks, health, energy)
        self.type = "dog"
    
    def noise(self):
        print('Bark')