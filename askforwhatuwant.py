import requests
Urlf = "https://uselessfacts.jsph.pl/random.json?language=en"
urlJ = "https://official-joke-api.appspot.com/random_joke"
urlV = "https://zenquotes.io/api/random"
def get_random_technology_fact():
    response = requests.get(Urlf)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to fetch fact")

def get_random_joke():
    
    
    print("Fetching a joke from the internet...")
    response = requests.get(urlJ)
    
    if response.status_code == 200:
        joke_data = response.json()
        return f"{joke_data['setup']} {joke_data['punchline']}"
    else:
        return f"Failed to retrieve joke. Status: {response.status_code}"
    
def get_random_quote():
    print("Finding a random quote")
    response = requests.get(urlV)
    if response.status_code == 200:
        quote_data = response.json()
        return f"{quote_data["q"]}"
    else:
        print('Failed to fetch your quote!')


    


    
while True:

    User_input = input("Enter 'f' for a random fact and enter j for a random joke and v for a random quote or presss q to exit the program: ").lower()


    if User_input == "f":
        print("Your random fact:")
        get_random_technology_fact()
    elif User_input == "j":
        print("Your random joke")
        get_random_joke()
    elif User_input =="v":
        print("Your random quote")
        get_random_quote()
    elif User_input == "q":
        break

    






    
    