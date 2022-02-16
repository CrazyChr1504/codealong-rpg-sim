from resourses import Character, Goblin
import random

def fight(fighter : Character, enemies : list):

    while not len(enemies) == 0:
        fighter_target = random.choice(enemies)
        fighter_target.take_damage(fighter.attack())
        if fighter_target.get_health() == 0:
            print("\nTarget has died!")
            enemies.remove(fighter_target)
            if len(enemies) == 0: break
            
    print(f"Fight is over {fighter.name} won!")

def new_fight(players: list, enemies: list):

    participants = players + enemies # Puts together the participants in one list
    random.shuffle(participants)

    for char in participants:
        target = ""
        # Check if player or goblin
        if char in players:
            target = random.choice(enemies) 
        else:
            target = random.choice(players)

        target.take_damage(char.attack())
        if target.get_health() == 0:
            print(f"{char.get_name()} was attack by {target.get_name()}.")
            print(f"{char.get_name()} has killed {target.get_name()}.")
            if(type(target) == Goblin):
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        else:
            print(f"{target.get_name()} was attack by {char.get_name()}.")
            print(f"{target.get_name()} has {target.get_health()} hp left.")
        

def main():
    
    enemies = []
    players = []

    nick = Character("Nick", 15, 3, 1)
    emy = Character("Emy", 20, 6, 5)
    players.append(nick)
    players.append(emy)
    
    for i in range(random.randint(2,4)):
        enemies.append(Goblin(i))
    

    #fight(emy, enemies)

    while len(enemies) != 0 and len(players) != 0:
        new_fight(players, enemies)

    if len(enemies) == 0:
        print("The players won!")
    elif len(players) == 0:
        print("The Goblins won!")
        print("GAME OVER")
    
if __name__ == "__main__":
    main()