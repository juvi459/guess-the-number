import random

lower_bound = 1
upper_bound = 5
max_attempt = 12

secret_number = random.randint(lower_bound, upper_bound)

def get_guess():
    while True:
        guess = int(input("Guess a number between 1 to 5"))
        if lower_bound <= guess <= upper_bound:
            return guess
        else:
           print("Invalid input.Please eneter a number whithin the range") 

def check_guess(guess,secret_number):
    if guess == secret_number:
        return "correct"  
    elif guess < secret_number:
        return "Too Low"
    else:
        return "too high" 

def play_games():
    attempts = 0
    win = False

    while attempts < max_attempt:
        attempts = attempts +1
        guess = get_guess()

        result = check_guess(guess ,secret_number)
        if result == "correct":
            print(f"Congratulations you have won {secret_number} in {attempts} attempts.")
        win = True
        break
    else:
        print(f"{result}. Try agian")

    if not win:
        print(f"sorry,you ran out of attempts your secret number is {secret_number}.")

if __name__== "__main__":
    print("Welcome to the Number Guessing Game")
    play_games()




