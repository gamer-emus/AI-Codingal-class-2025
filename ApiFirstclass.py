import requests


def get_random_joke():
    """ Fetch a random joke From the Joke API 🥶"""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)



    if response.status_code ==200:
        print(f"Full JSON response:{response.json()}")


        joke_data = response.json()
        return f"{joke_data['setup']}{joke_data['punchline']}"
    else:
        return "Return failed to retrieve joke"
    
def main():
    print("Welcome to the random Joke generator!🥶")



    while True:
        user_input = input("Press Enter to get a new joke, or type q to quit" ).strip().lower()



        if user_input in ("q","exit"):
            print("Goodbye!")
            break



if __name__ == "__main__":
    main()



    
    