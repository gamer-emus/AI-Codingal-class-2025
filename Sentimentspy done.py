# Initialize colorama for colored output
from colorama import Fore, Back, Style, init
from textblob import TextBlob
import time
init(autoreset=True)

# Emojis for sentiment types
positive_emoji = "😀"
negative_emoji = "😠"
neutral_emoji = "😐"


def loading():
    print("Analyzing....")
    for i in range(3):
        print("-" * (i + 1))
        time.sleep(0.3)
    print()

print(f"{Fore.CYAN}Welcome to Sentiment Spy! {Style.DIM} You are going to have fun!!")
print(f"Analyze sentences with TextBlob and I’ll show you the sentiment. 😃")
print(f"{Back.YELLOW}Type 'exit' or 'q' to quit.")
print("Type help for help, summary for summary, and reset to clear history.")
print(f"Type 'history' to view conversation history.")

user_name = "Mystery Agent"  # fallback if user doesn't provide a name
conversation_history = []  # list of tuples: (input, polarity, sentiment_type)

while True:
    user_input = input(f"{Fore.GREEN}Enter text to analyze: {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.YELLOW}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # Exit the conversation
    if user_input.lower() in ['exit', 'q']:
        print(f"{Fore.MAGENTA}Exiting Sentiment Spy. Farewell, {user_name}!{Style.RESET_ALL}")
        break

    # Show history
    elif user_input.lower() == 'history':
        print(f"{Fore.MAGENTA}--- Conversation History ---{Style.RESET_ALL}")
        if not conversation_history:
            print(f"{Fore.YELLOW}No history yet.{Style.RESET_ALL}")
        else:
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                emoji = neutral_emoji
                color = Fore.YELLOW
                if sentiment_type == "Positive":
                    emoji = positive_emoji
                    color = Fore.GREEN
                elif sentiment_type == "Negative":
                    emoji = negative_emoji
                    color = Fore.RED
                print(f"{color}{idx}. \"{text}\" | Polarity: {polarity} | Sentiment: {sentiment_type} {emoji}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}--------------------------{Style.RESET_ALL}")
        continue

    # Help menu
    elif user_input.lower() == 'help':
        print("This app analyzes your sentences using sentiment analysis.")
        print("Special commands:")
        print("  exit / q   → Quit the app")
        print("  history    → Show conversation history")
        print("  reset      → Clear conversation history")
        print("  help       → Show this help message")
        continue

    # Reset history (simplified)
    elif user_input.lower() == 'reset':
        conversation_history.clear()
        print(f"{Fore.RED}Conversation history has been reset!{Style.RESET_ALL}")
        continue

    # Run loading animation before analysis
    loading()

    # Analyze sentiment using TextBlob
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    emoji = neutral_emoji
    color = Fore.YELLOW
    sentiment_type = "Neutral"

    if polarity > 0.1:
        emoji = positive_emoji
        color = Fore.GREEN
        sentiment_type = "Positive"
    elif polarity < -0.1:
        emoji = negative_emoji
        color = Fore.RED
        sentiment_type = "Negative"

    conversation_history.append((user_input, polarity, sentiment_type))

    print(f"{color}Sentiment: {sentiment_type} {emoji} | Polarity: {polarity} | Input: \"{user_input}\"{Style.RESET_ALL}")
