import random

def generate_lottery_number():
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
    return random.sample(elements[:10], 4) + [random.choice(elements[10:])]

def get_user_input():
    print("Enter your lottery number (four numbers and one letter):")
    user_numbers = []
    for i in range(4):
        num = int(input(f"Enter number {i+1}: "))
        user_numbers.append(num)
    letter = input("Enter a letter: ").upper()
    return user_numbers + [letter]

def check_winner(lottery_number, user_number):
    if sorted(lottery_number) == sorted(user_number):
        print("Congratulations! You won the lottery!")
    else:
        print(f"Sorry, you lost. The winning number was {lottery_number}.")

# Main Program
lottery_number = generate_lottery_number()
user_number = get_user_input()
check_winner(lottery_number, user_number)