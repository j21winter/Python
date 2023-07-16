class Character:
    def __init__ (self, name, weapons=[], energy=100):
        self.name = name
        self.energy = energy
        self.weapons = weapons
    
    def __repr__(self):
        return self.name
    
    def eat(self, food):
        print(f'{self} ate {food}')
        self.energy +=1
        print(self.energy)
        return self
    
    def walk(self):
        self.energy -= 1
        print(self.energy)
        return self
    
    def add_weapon(self, weapon_name):
        self.weapons.append(weapon_name)
        print(self.weapons)
        return self


player_1 = Character('jonny', ['laptop'])

player_1.eat('pizza').walk().add_weapon('keyboard')
