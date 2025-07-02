# Bible Quiz App - Step 1
from colorama import Fore, Style, init
init(autoreset=True)
from datetime import datetime
import random

score = 0
questions = [
    {
        "question": "Who built the ark?",
        "options": ["A. Moses", "B. Noah", "C. Abraham", "D. Peter"],
        "answer": "B"
    },
    {
        "question": "Where was Jesus born?",
        "options": ["A. Nazareth", "B. Jerusalem", "C. Bethlehem", "D. Egypt"],
        "answer": "C"
    },
    {
        "question": "How many disciples did Jesus have?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    },
    {
        "question": "Who was swallowed by a big fish?",
        "options": ["A. Jonah", "B. Paul", "C. Elijah", "D. David"],
        "answer": "A"
    },
    {
        "question": "Which book comes first in the Bible?",
        "options": ["A. Exodus", "B. Psalms", "C. Matthew", "D. Genesis"],
        "answer": "D"
    },
    {
        "question": "What did Jesus turn water into?",
        "options": ["A. Blood", "B. Oil", "C. Wine", "D. Honey"],
        "answer": "C"
    },
    {
        "question": "What did David use to defeat Goliath?",
        "options": ["A. Sword", "B. Stone and sling", "C. Bow and arrow", "D. Fire"],
        "answer": "B"
    },
    {
        "question": "Who led the Israelites out of Egypt?",
        "options": ["A. Aaron", "B. Moses", "C. Joshua", "D. Jacob"],
        "answer": "B"
    },
    {
        "question": "What is the last book of the Bible?",
        "options": ["A. Malachi", "B. Revelation", "C. Acts", "D. Romans"],
        "answer": "B"
    },
    {
        "question": "Who denied Jesus three times?",
        "options": ["A. Judas", "B. Peter", "C. John", "D. Thomas"],
        "answer": "B"
    }
]
# Shuffle questions before starting the quiz
random.shuffle(questions)

print(Fore.CYAN + Style.BRIGHT + "\n===== WELCOME TO THE BIBLE QUIZ APP =====")

print("Test your knowledge of the Bible and learn as you go!\n")

for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {q['question']}")
    for option in q["options"]:
        print(option)

    answer = input("Your answer (A/B/C/D): ").upper()

    if answer == q["answer"]:
        print(Fore.GREEN + "✅ Correct!")
        score += 1
    else:
        print(Fore.RED + f"❌ Wrong. The correct answer was {q['answer']}.")


# ✅ Final score section starts here (outside loop!)
print(f"\n🎉 Quiz complete! Your score: {score}/{len(questions)}")

    # Calculate performance
percentage = (score / len(questions)) * 100

    # Determine feedback message
if percentage >= 80:
        message = "⭐ Excellent! You really know your Bible."
        color = Fore.GREEN
elif percentage >= 50:
        message = "👍 Good effort! Keep studying."
        color = Fore.YELLOW
else:
        message = "💡 Keep practicing! You'll improve with time."
        color = Fore.RED

    # Print feedback
print(color + message)

    # Save result to file
with open("score_history.txt", "a") as file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{now} - Score: {score}/{len(questions)} ({percentage:.2f}%) - {message}\n")


