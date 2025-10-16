import random
from colorama import init, Fore, Style
init(autoreset=True)

def player_choice():
    print("Choose your move:")
    print("1 = Rock")
    print("2 = Paper")
    print("3 = Scissors")
    choice = input("Enter your choice (1/2/3): ")

    while choice not in ["1", "2", "3"]:
        print(Fore.RED + "Invalid choice! Please enter 1, 2, or 3.")
        choice = input("Enter your choice (1/2/3): ")

    return int(choice)

def ai_choice():
    return random.randint(1, 3)

def rpss():
    print(Fore.CYAN + "Welcome to Rock Paper Scissors Shoot!")
    name = input("Enter player name: ")
    print(f"Welcome to the game, {name}!\n")

    moves = {1: "Rock", 2: "Paper", 3: "Scissors"}

    player = player_choice()
    ai = ai_choice()

    print(f"\n{name} chose: {moves[player]}")
    print(f"AI chose: {moves[ai]}")

    if player == ai:
        print(Fore.YELLOW + "It's a tie!")
    elif (player == 1 and ai == 3) or (player == 2 and ai == 1) or (player == 3 and ai == 2):
        print(Fore.GREEN + f"{name} wins!")
    else:
        print(Fore.RED + "AI wins!")

rpss()
