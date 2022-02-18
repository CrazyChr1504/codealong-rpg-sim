# Imports
from resourses import Character, Monster, save_character, load_characters
import random
# Global variables
turn = 1
# Classes
# Functions
def new_fight(players: list, enemies: list):
    global turn
    participants = players + enemies # Puts together the participants in one list
    random.shuffle(participants)

    for char in participants:
        print(f"\nTurn {turn}\n")
        target = ""
        # Check if player or monster
        if char in players:
            target = random.choice(enemies) 
        else:
            target = random.choice(players)

        target.take_damage(char.attack())
        if target.get_health() == 0:
            print(f"{char.get_name()} was attack by {target.get_name()}.")
            print(f"{char.get_name()} has killed {target.get_name()}.")
            if(type(target) == Monster):
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        
        else:
            print(f"{target.get_name()} was attack by {char.get_name()}.")
            print(f"{target.get_name()} has {target.get_health()} hp left.")
        
        turn += 1
        
        if len(players) == 0 or len(enemies) == 0: break

# Main
def main():
    
    enemies = []
   
    for i in range(1, random.randint(3,12)):
        enemies.append(Monster(i))
    
    #save_character(emy)
    players = load_characters()
    for player in players:
        print(player)
        print()
    
    while len(enemies) != 0 and len(players) != 0:
        new_fight(players, enemies)

    if len(enemies) == 0:
        print("The players won!\n")
    elif len(players) == 0:
        print("Gruffbarb won!")
        print("GAME OVER\n")
    

if __name__ == "__main__":
    main()