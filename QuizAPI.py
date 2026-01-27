import requests
import random
import html



EDUCATION_CATEGORY_ID = 9
API_URL = f"https://opentdb.com/api.php?amount=2&category={EDUCATION_CATEGORY_ID}&type=multiple"

#
def get_edu_questions():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if data["response_code"] == 0 and data["results"]:
            return data["results"]
    return None

def run_quiz():
    questions = get_edu_questions()
    if not questions:
        print("Failed to fetch the Data Required")
        return
    score = 0 
    print("Welcome to the education quiz\n")


    for i,q in enumerate(questions,1):
        questions = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        incorrect = [html.unescape(a) for a in q["incorrect_answers"]]



        options = incorrect + [correct]
        random.shuffle(options)


        print(f"Question{i}:{questions}")
        for idx, options in enumerate(options,1):
            print(f"{idx}.{options}")

        while True:
            try:
                choice = int(input("Your answer(0-4)"))
                if 1 <= choice <= 4:
                    break
            except ValueError:
                pass
            print("Invalid Input pls try again!")


            if options[choice - 1]== correct:
                print("Correct ✅")
                score += 1
            else:
                print(f"Wrong!! Correct answer is {correct}")


    print(f"FInal score :{score}/{len(questions)}")
    print(f"Percentage :{score/len(questions)*100:.1f})%")
if __name__ == "__main__":
    run_quiz()

                



            


    

