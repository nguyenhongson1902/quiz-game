import pandas as pd
import random

data = pd.read_csv("./quiz_questions.csv")

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

def run_quiz():
    questions_list = load_questions()
    ask_question(questions_list[0])


if __name__ == "__main__":
    run_quiz()