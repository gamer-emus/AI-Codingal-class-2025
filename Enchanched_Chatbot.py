from textblob import TextBlob  

print("Hello welcome to The text ")
name_U = input("Enter your name : ")
print(f"Hello!, {name_U}")

while True:
    Input_U = input("Enter your sentence: ")
    blob = TextBlob(Input_U)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        print("Your text is happy 😁")
    elif polarity < -0.1:
        print("Your text is sad 😢")
    else:
        print("Your text is neutral 😐")

    Qinput = input("Do you want to exit the program? (press 'q' to quit): ")
    if Qinput.lower() == 'q':
        print("You have exited the program")
        break
