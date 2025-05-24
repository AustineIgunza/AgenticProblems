import random

def intro():
    print("Welcome, adventurer! You wake up in a dark forest with no memory.")
    print("Do you want to explore the forest or head towards the mountains?")
    choice = input("Type 'forest' or 'mountains': ").strip().lower()
    if choice == "forest":
        forest()
    elif choice == "mountains":
        mountains()
    else:
        print("Invalid choice. Try again.")
        intro()

def forest():
    print("\nYou walk into the forest and find a mysterious glowing sword.")
    has_sword = True
    print("Suddenly, a wild beast appears!")
    fight = input("Do you want to 'fight' or 'run'? " ).stripe().lower()
    if fight == "fight":
        if has_sword:
            print("You slay the beast with the glowing sword!")
            treasure_cave()
        else:
            print("You try to fight with your fists but the peast overpowers you. ")
            game_over()
    else:
        print("You run away and get lost in the forest.")
        game_over()
        def mountains():
            print("\nYoy climb the mountain and find a wise old man")