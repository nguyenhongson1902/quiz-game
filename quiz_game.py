import pandas as pd
import random

data = pd.read_csv("./quiz_questions.csv")
data.rename(columns={'Option 1': 'A', 'Option 2': 'B', 'Option 3' : 'C', 'Option 4' : 'D'}, inplace=True)

def load_questions():
    num_question = len(data.index)
    questions_list = []
    for i in range(0, 5) :
        id = random.randint(0, num_question - 1)
        questions_list.append(data.loc[id])
    return questions_list

def ask_question(question):
    print("Here is your question: ")
    print(question["Question"])
    for i in range(0, 4) :
        c = chr(ord("A") + i)
        print(c + " " + question[c])
    ans = input("Enter your answer: ")
    if question[ans] == question['Answer'] :
        print("Correct!!!!")
        print("The answer is: " + question['Answer'])
        return 1
    else :
        print("Wrong Answer")
        print("The answer is: " + question['Answer'])
        return 0

def run_quiz():
    questions_list = load_questions()
    score = 0
    for i in range(0, 5) :
        score += ask_question(questions_list[i])

    print(score)

if __name__ == "__main__":
    run_quiz()