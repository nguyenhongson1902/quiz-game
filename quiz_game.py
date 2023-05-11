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
        c = chr(ord('A') + i)
        print(c + " " + question.iloc[i])

    ans = input("Enter your answer: ")
    
    if question[ans] == question['Answer'] :
        print("Correct!!!!")
        print("The answer is: " + question['Answer'])
        return 1
    else :
        print("Wrong Answer")
        print("The answer is: " + question['Answer'])
        return 0

def add_to_leaderboad(score):
    leaderboard = pd.read_csv("./LeaderBoard.csv")
    leaderboard = pd.DataFrame(leaderboard)
    print("Congratulations!!!!")
    name = input("Enter your name: ")
    new_score = {"Name" : name, "Score" : score}
    leaderboard = leaderboard.append(new_score, ignore_index = True)
    leaderboard = leaderboard.sort_values(by='Score', ascending = False)
    


def run_quiz():
    questions_list = load_questions()
    score = 0
    for i in range(0, 5) :
        score += ask_question(questions_list[i])

    add_to_leaderboad(score)

if __name__ == "__main__":
    run_quiz()