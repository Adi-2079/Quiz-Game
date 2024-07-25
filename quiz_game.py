import json
import os

# Sample questions
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Paris", "B. Madrid", "C. Berlin", "D. Rome"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "choices": ["A. Elephant", "B. Whale", "C. Shark", "D. Hippo"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. F. Scott Fitzgerald"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["A. Au", "B. Ag", "C. Pb", "D. Fe"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "choices": ["A. Beijing", "B. Tokyo", "C. Seoul", "D. Bangkok"],
        "answer": "B"
    },
    {
        "question": "What is the longest river in the world?",
        "choices": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
        "answer": "A"
    }
]

HIGH_SCORE_FILE = 'high_score.txt'

def load_questions():
    return questions

def ask_question(question):
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    return answer == question["answer"]

def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'r') as file:
            return int(file.read().strip())
    return 0

def save_high_score(score):
    with open(HIGH_SCORE_FILE, 'w') as file:
        file.write(str(score))

def run_quiz():
    questions = load_questions()
    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {question['answer']}.\n")
    print(f"Your final score is {score} out of {len(questions)}.")

    high_score = load_high_score()
    if score > high_score:
        print(f"Congratulations! You have a new high score: {score}")
        save_high_score(score)
    else:
        print(f"Your high score is: {high_score}")

if __name__ == "__main__":
    run_quiz()