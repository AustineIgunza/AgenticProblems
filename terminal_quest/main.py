def start_game():
    print("🧙 Welcome, adventurer!")
    print("You must choose your path: the dark forest or the icy mountains.")
    choice = input("Type 'forest' or 'mountains': ").strip().lower()

    if choice == "forest":
        forest_path()
    elif choice == "mountains":
        mountain_path()
    else:
        print("You hesitated and were eaten by a wild goose. 🪿")
        game_over()

def forest_path():
    print("\n🌲 You enter the forest and hear rustling...")
    choice = input("Do you 'investigate' the sound or 'run'? ").strip().lower()

    if choice == "investigate":
        print("You find a wounded dragon who becomes your ally! 🐉")
        victory()
    elif choice == "run":
        print("You trip over a root and a squirrel steals your sword. 🐿️")
        game_over()
    else:
        print("Lost and confused, you vanish into the woods.")
        game_over()
def mountain_path():
        print("\n You climb the mountains and face a blizzard. ")
        choice = input("Do uou 'build shelter' or 'press on'?").strip().lower()

        if choice == "build shelter":
            print("You survive the night and find a magical artifact! ")
            victory()
        elif choice == "press on":
            print("The cold overwhelms you, your journey end here. ")
            game_over()
        else:
            print("You are buried in snow, never to be found.")
            game_over()
def victory():
            print("\n Congratulations! You completed your quest successfully!")
def game_over():
        print("\n Game over, Try again?")
        choice = input("Type 'yes' to restart or anything else to quit: ").strip().lower()
        if choice == "yes":
            start_game()
        else:
            print("Thanks for playing")
start_game()