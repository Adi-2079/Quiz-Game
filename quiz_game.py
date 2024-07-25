import json

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
    }
]

def load_questions():
    # If you have a file with questions, you can load them using this function
    # with open('questions.json', 'r') as file:
    #     questions = json.load(file)
    # return questions
    return questions  # For now, we use the sample questions defined above

def ask_question(question):
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    return answer == question["answer"]

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

if __name__ == "__main__":
    run_quiz()