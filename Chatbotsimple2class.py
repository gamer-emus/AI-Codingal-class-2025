import re , random 
from colorama import Fore, init
init(autoreset=True)



Dest = {
    "City":["Tokyo","Singapore","New York"],
    "Beaches":["Bali","Maldives","Phuket"],
    "Mountains": ["Himalyas", "Rocky mountains" , "Swiss Alphs"]


}

jokes = [

"Why don't programmers like nature? Too many bugs!",

"Why did the computer go to the doctor? Because it had a virus!",

"Why do travelers always feel warm? Because of all their hot spots!"

]



def normal_input(text):
    return re.sub(r"/s" ,"", text.strip().lower())



def recommend():
    print(Fore.CYAN +"TravelBot: Beaches , Mountains , Cities?")
    prefrence = input(Fore.YELLOW+"You chose:")
    prefrence = normal_input(prefrence)

    if prefrence in Dest:
        Sugestion = random.choice(Dest[prefrence])
        print(Fore.GREEN + f"Travelbot: how about {Sugestion}?")
        print(Fore.BLUE + "Do You like the sugestion? Type YES/NO")
        answer = input(Fore.YELLOW + "You :").lower()


        if answer == 'yes':
            print(Fore.GREEN + f"Travelbot: Awsome Enjoy {Sugestion}")
        elif answer == "No":
            print(Fore.RED+ "I will Try again")
            recommend()
        else:
            print("I Will sugest again")
            recommend()
    else:
        print(Fore.RED + "I Dont havr that avalible ")

    
    show_help()


def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normal_input(input(Fore.YELLOW + "You :"))
    print(Fore.CYAN + "TravelBot: How many Days")
    days = input(Fore.LIGHTCYAN_EX + "You: ")




    print(Fore.GREEN + f"Packing Trips for {days} In {location}")
    print(Fore.GREEN + "-- Pack Versitile Clothes")
    print(Fore.GREEN + "-- Pack  Chargers/Adapters")
    print(Fore.GREEN + "-- Chech The weather ")



def Tell_joke():
    print(Fore.MAGENTA + f"Here is a Joke : {random.choice(jokes)}")



def show_help():
    print(Fore.MAGENTA + "\n I can")
    print(Fore.GREEN + "Sugest travel spots ")
    print(Fore.GREEN + "Give Packing advise  ")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")

print(Fore.GREEN + "- Tell a joke (say 'joke')")

print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Main chat loop

def chat():

 print(Fore.CYAN + "Hello! I'm TravelBot.")

name = input(Fore.YELLOW + "Your name? ")

print(Fore.GREEN + f"Nice to meet you, {name}!")


show_help()


while True:

    user_input = input(Fore.YELLOW + f"{name}: ")

    user_input = normal_input(user_input)


    if "recommend" in user_input or "suggest" in user_input:

        recommend()

    elif "pack" in user_input or "packing" in user_input:

        packing_tips()

    elif "joke" in user_input or "funny" in user_input:

        Tell_joke()

    elif "help" in user_input:

     show_help()

    elif "exit" in user_input or "bye" in user_input:

     print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
    break

else:
 print(Fore.RED + "TravelBot: Could you rephrase?")

# Run the chatbot

#if __name__ == "__main__":

chat()


    

    






