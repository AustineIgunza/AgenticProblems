import random
def intro():
    print("Welcome,adventurer! You wake up in a dark forest with no memory.")
    print("Do you want to explore the forest or head towards the mountains")
    choice=input("Type 'forest' or 'mountains': ").strip().lower()
    if choice =="forest":
        forest()
