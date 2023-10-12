questions = ("What countries are in Europe?: ",
                "What is the strongest phone in the world?: ",
                "How many letters are in the chinese alphabet?: ",
                "What is the hardest language to learn?: ",
                " How many bhp have Koenigsegg Jesko Absolut?: ")

options = (("A.42","B.46","C.44","D.39"),
                ("A.NOKIA 3310","B.SAMSUNG GALAXY NOTE 7","C.SONIM XP3300 FORCE","D.IPHONE SE2"),
                ("A.36","B.45","C.5.000","D.20.000"),
                ("A.HUNGARY","B.MANDARIN","C.CHINESE","D.JAPANESE"),
                ("A.1000","B.950","C.1320","D.1280"))

answers = ("C", "C", "A", "B", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("WHO WANTS TO BE A BILLIONAIRE"
          "")
    print("-------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers= ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses= ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")