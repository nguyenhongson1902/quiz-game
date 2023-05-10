import pandas as pd
import csv
def readhs():
    try:
        with open('highscore.txt', 'r') as f:
            high_score = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        high_score = 0
    return high_score
def writehs(new_score):
    high_score = readhs()
    if new_score > high_score:
        with open('highscore.txt', 'w') as f:
            f.write(str(new_score))
def load_questions():
    df = pd.read_csv('quiz_questions.csv')
    qs = df.to_dict('records')
    return qs
def ask_question(data):
    score = 0
    for q in data:
        print(q['Question'])
        print(q['Option 1'])
        print(q['Option 2'])
        print(q['Option 3'])
        print(q['Option 4'])
        user_answer = input('Your answer: ')    
        if user_answer.lower() == q['Answer'].lower():
            score += 1
            print('Correct!')
        else:
            print('Incorrect!')
            print(f'Your score is: {score}')
            hs = readhs()
            if score > hs:
                writehs(score)
                print(f'High score: {readhs()}')
            else:
                print(f'High score: {readhs()}')
            break

if __name__ == "__main__":
    ask_question(load_questions())
    

