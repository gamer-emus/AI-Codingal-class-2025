from groq import generate_response


def reinforcement_learning_activity():
    print("\n ==== REINFORCEMNET LEARNING ACTIVITY=====\n")
    prompt = input("Enter a prompt FOr the AI model (e.g Describe the lion): ").strip()
    if not prompt:
        print("Please enter a prompt to run this activity")
        return
    



    initail_response= generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"\n Initial AI Response: {initail_response}")



    try:

        rating= int(input("Rate the response from 1(bad) - 5(good) :").strip())
        if rating < 1 or rating > 5:
            print("Invalid Rating Using 3..")
            rating = 3
    except ValueError:
        print("Invalid Rating using 3 ")
        rating =3


    feedback = input("Provide Feedback for improvment: ").strip()
    improved_response= f"{initail_response} (Improved by your feedback): {feedback}"
    print(f"The response Better : {improved_response}")



    print("\n Reflection")
    print("1. How did the models response improve with the feedback?")
    print("2. How does Reinforcement Learning help AI to imprvoe its performance over time")


def role_based_prompt_activity():
    print("Role based prompt activity")
    category = input("Enter a category (e.g , Science , history , math): ").strip()
    items = input(f"Enter a specific {category} Topic (e.g Photosynthesis, for science )").strip()



    if not category or not items:
        print("Please fill in both fields to run this activity")
        return
    
    teacher_prompt = f"You are a teacher explain {items} in simple terms for a kid to understand"
    expert_prompt = f"your an expert in {category} Explain {items} In a high detail , And techincal manner"



    teacher_response = generate_response(teacher_prompt ,temperature=0.3 , max_tokens=1024)
    expert_response = generate_response(expert_prompt, temperature=0.3, max_tokens=1024)

    print(f"\n ---- Teachers Perspective ---- \n {teacher_response}")
    print(f"\n ---- Expert perspective --- \n {expert_response}")

    print("Reflection ")
    print("1.How did the Ai's Response differ between the teachers and experts perspective")
    print("2. How Can role-based prompts help Tailor Ai response for different context")


def run_activity():
    print("\n === AI learn activty === ")
    print("Choose an Activty")
    print("1) Reinforcement Learning ")
    print("2) ROle based prompts")
    choice = input("> ").strip()


    if choice == "1":
        reinforcement_learning_activity()
    elif choice =="2":
        role_based_prompt_activity()

    else:
        print("Invalid Choice , Please Choice 1 or 2 ")


if __name__ == "__main__":
    run_activity()
        

        






