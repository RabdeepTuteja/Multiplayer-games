import random

def rock_paper_scissors():
    print("\nWelcome to Rock Paper Scissors!")
    print("1. Rock\n2. Paper\n3. Scissors")

    target = int(input("Enter how many points are needed to win: "))
    user_score = 0
    computer_score = 0
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    while user_score < target and computer_score < target:
        try:
            user = int(input("\nChoose 1, 2, or 3: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if user not in choices:
            print("Invalid choice. Choose 1, 2, or 3.")
            continue

        computer = random.randint(1, 3)
        print("You chose:", choices[user])
        print("Computer chose:", choices[computer])

        if user == computer:
            print("Match Draw!")
        elif (user == 1 and computer == 3) or \
             (user == 2 and computer == 1) or \
             (user == 3 and computer == 2):
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")

        print(f"Score — You: {user_score} | Computer: {computer_score}")

    if user_score == target:
        print("Congratulations! You reached the target first.")
    else:
        print("Computer reached the target first. Better luck next time!")


def quiz_game():
    print("\nWelcome to the RD Quiz Game!")
    name = input("Enter your name: ")

    questions = [
        ("Which Marvel character dies in Endgame?",
         ["Captain America", "Iron Man", "Thor", "Hulk"], 2),
        ("Who is the Prime Minister of India?",
         ["Narendra Modi", "Bhupendra Jogi", "Yogi Adityanath", "Neeraj Modi"], 1),
        ("Who sang 'Pehle Bhi Main' from Animal?",
         ["Shekhar", "Arijit Singh", "Vishal Mishra", "Benny Dayal"], 3),
        ("Who won Bigg Boss 13?",
         ["Asim Riaz", "Shehnaaz Gill", "Sidharth Shukla", "Rashami Desai"], 3),
        ("Which country won the 2023 Cricket World Cup?",
         ["India", "Australia", "England", "Afghanistan"], 2),
        ("Who is Katrina Kaif's husband?",
         ["Sidharth Malhotra", "Salman Khan", "Ranbir Kapoor", "Vicky Kaushal"], 4),
        ("Who played Berlin in Money Heist?",
         ["Jaime Lorente", "Pedro Alonso", "Patrick Criado", "Sergio Mattarella"], 2),
        ("Which planet is closest to the Sun?",
         ["Mercury", "Venus", "Earth", "Mars"], 1),
        ("Who was Akbar's grandson?",
         ["Babur", "Humayun", "Shah Jahan", "Salim"], 3),
        ("Who was the 10th Sikh Guru?",
         ["Guru Gobind Singh Ji", "Guru Nanak Dev Ji",
          "Guru Angad Dev Ji", "Guru Tegh Bahadur Ji"], 1),
    ]

    score = 0
    print(f"\nHello {name}! Correct answer: +10 points; wrong answer: -5 points.")

    for number, (question, options, answer) in enumerate(questions, start=1):
        print(f"\nQ{number}. {question}")
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        try:
            choice = int(input("Enter the correct option (1-4): "))
        except ValueError:
            choice = 0

        if choice == answer:
            score += 10
            print(f"Correct! Your score is: {score}")
        else:
            score -= 5
            print(f"Wrong answer. Your score is: {score}")

    print(f"\n{name}, your total score is: {score}")
    if score >= 80:
        print("You played really well! Excellent knowledge.")


def main():
    print("\nWelcome to the Multiplayer Game Hub!")
    print("1. Rock Paper Scissors")
    print("2. RD Quiz Game")
    print("3. Exit")

    while True:
        try:
            choice = int(input("\nChoose an option (1-3): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            rock_paper_scissors()
        elif choice == 2:
            quiz_game()
        elif choice == 3:
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()