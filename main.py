from groq import generate_response


def bias_mitigation_activity():
    print("\n Bias Activity \n")
    prompt = input("Enter a Prompt to explore bias (e.g 'Descibe the Ideal Doctor'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity")
        return
    

    initial_response = generate_response(prompt, temperature=0.3,max_tokens=1024)
    print(f"\n Innitial AI Response {initial_response}")



    modified_prompt = input(
        "Modify the prompt to make it more neutral (e.g , 'Describe the quallities of a doctor') :"
    ).strip()

    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature=0.3,max_tokens=1024)
        print(f"\n Modified AI response (neutral ) :{modified_response} ")

    else:
        print("No Modified prompt entered , Skipping neutral response")


def token_limit_activity():
    print("\n =====Token Activity=====")
    long_prompt = input("Enter a long prompt (more than 300 words e.g detailed story or description)").strip()



    if long_prompt:
        long_response = generate_response(long_prompt,temperature=0.3,max_tokens=1024)
        preview = (long_response[:500]+"...") if len(long_response) > 500 else long_response
        print(f"\n Response to long prompt {long_response}")

    else:
        print("No Long prompt entered skipping long prompt response")


    short_prompt = input("Now condense the prompt to be more concise :").strip()
    if short_prompt:
        short_response = generate_response(short_prompt, temperature=0.3,max_tokens=1024)
        print(f"\n Response to condensed prompt {short_response}")
    else:
        print("No condensed prompt entered . Skipping condensed prompt response.")


def run_activity():
    print("\n AI LEARNING ACTIVITY ====")

    print("\n Choose an activity:  \n")
    print("1) Bias mitigation")
    print("2) Token limits ")
    choice = input("> ").strip()

    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid Choice choose 1 or 2 as a choice")


if __name__ == "__main__":
    run_activity()



