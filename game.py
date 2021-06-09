from classes.ninja import Ninja
from classes.pirate import Pirate


# while loop to run the game
    # some variable health to zero exit() or break
    # after health zero input asking quit or play again

# text for game start
# pick your character

# tpyed or input actions
    # make a method with input that calls attack

while True:
    choose_side = input("Welcome to Ninjas VS Pirates\n\n\nChooose your side!\n'Ninja' or 'Pirate':  ")
    while True:
        if choose_side.upper() == 'NINJA':
            name = input("Name your Ninja:  ")
            player = Ninja(name)
            comp = Pirate("Jack Sparrow")
            break
        elif choose_side.upper() == "PIRATE":
            name = input("Name your Pirate:  ")
            player = Pirate(name)
            comp = Ninja("Michelangelo")
            break
        else:
            choose_side = input("Please type 'Ninja' or 'Pirate':  ")

    player.show_stats()
    round = 0
    print(f"ROUND {round}\nFIGHT!")
    while comp.health > 0 and player.health > 0:
        print(f"{player.name} attacks")
        player.attack(comp).show_health()
        print(f"{comp.name} attacks")
        comp.attack(player).show_health()
        print()
        
    print(f"player health: {player.health}\ncomputer health: {comp.health}")
    if player.health > 0:
        print(f"{player.name} WINS!")
    else:
        print(f"YOU LOSE")
    state = input("do you want to continue?\n(Y/N):  ")
    if state.upper() == 'Y':
        continue
    else:
        break
