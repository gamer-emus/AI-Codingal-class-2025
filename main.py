#from hf import generate_response
from groq import generate_response


import time



def temperature_prompt_activity():
    print("="*70)

    print("ADVANCED PROMPT ENGINEERING: Temp+Instruction")

    print("="*70)



    print("\n Part 1: Temperature Exploration")
    base = input("Enter a creative prompt:").strip()


    for t, label in [(0.1, "Low(0.1) - Deterministic"),
                     (0.5, "Medium(0.5) - Balanced"),
                     (0.9, "High(0.9) - Creative")]:
        print(f"\n --{label}---")
        print(generate_response(base, temperature=t, max_tokens=512))
        time.sleep(1)


    print("\n Part 2: --Instruction based prompts---")
    topic = input("Choose a topic (e,g Climate change, space exploration)").strip()

    prompts=[
        f"Summarize key facts about {topic} in 3-4 sentances", 
        f"Explain {topic} as if im a 10 year old "
        f"Write pro's/con's about {topic} :"
        f"Create a fictional news headline from 2050 about {topic}"



    ] 


    for i, p in enumerate(prompts,1):
        print(f"\n ---Instruction {i}--- \n{p}")

        print(generate_response(p, temperature=0.7, max_tokens=512))
        time.sleep(1)



    print("Part 3: your own instruction prompt")
    custom = input("Enter your instruction based prompt: ").strip()

    try:
        temp = float(input("Set temperature (0.1-1.0): ").strip())

        if not (0.1 <= temp <= 1.0): raise ValueError
    except ValueError:
        print("Invalid temperature Using 0.7 ")
        temp = 0.7

    print(f"\n ---Your prompt @ Temp {temp}--- ")
    print(generate_response(custom,temperature=temp,max_tokens=512))




    print("\n REFLECTION")
    print("1) What changed when the promps became more specific")
    print("2) What Impovered when context was added?")
    print("3) Which prompts felt the most usefull and why ")
    print("\n CHALLENGE: Create a prompt chain?")
    print("Generate content -> rewrite constraints -> create a sequel (try different temps)")

def pseudo_stream(text,delay=0.013):
    for ch in text:
        print(ch,end="",flush=True)
        time.sleep(delay)
    print()



def bonus_stream():
    choice = input("\n BONUS: STREAMING LIKE OUTPUT?(Y/N)").lower().strip()
    if choice == "y":
        p = input("Enter a Prompt :").strip()
        out = generate_response(p,temperature=0.7,max_tokens=512)
        print("\n Streaming like response (Not real streaming):")
        pseudo_stream(out)


if __name__ == "__main__":
    temperature_prompt_activity()
    bonus_stream()




