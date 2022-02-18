# Imports
# Global variables
# Classes

class Character:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    
    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"

    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if actual_damage < 0: actual_damage = 0            
        if (self.health - actual_damage) < 0: self.health = 0
        else: self.health -= actual_damage
    
    def attack(self):
        return self.damage
        
    def get_health(self):
        return self.health

    def get_name(self):
        return self.name

    def get_all_atributes(self):
        return self.name, self.health, self.damage, self.armor
        
class Monster:

    def __init__(self, id):
        self.id = id
        self.health = 10
        self.damage = 4
        self.armor = 1
    
    def __str__(self):
        return f"Gruffbarb: {self.id}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"

    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if actual_damage < 0: actual_damage = 0 
        if (self.health - actual_damage) < 0: self.health = 0
        else: self.health -= actual_damage
        print(f"Gruffbarb #{self.id} took {actual_damage} dmg")


    def attack(self):
        return self.damage
        
    def get_health(self):
        return self.health

    def get_name(self):
        return f"Gruffbarb #{self.id}"

# Functions
def save_character(character : Character):
    """
    Takes in a character and breaks down its' attributes och saves them in a file
    Args:
        character (Character): The object that gets saved in a file
    """

    name, health, damage, armor = character.get_all_atributes()
    with open("character_file.txt", "w", encoding="utf8") as f:
        save_string = f"{name}/{health}/{damage}/{armor}\n"
        f.write(save_string)
        print(f"{name} has been successfully saved.")

def load_characters():

    with open("character_file.txt", "r", encoding="utf8") as f:
        characters = []
        for line in f.readlines():
            attributes = line.split("/")
            this_char = Character(attributes[0],
                                  int(attributes[1]),
                                  int(attributes[2]),
                                  int(attributes[3]))
            characters.append(this_char)
        print("Characters have been loaded from your file:\n")
        return characters
# Main code