import random

def number_guessing_game():
    
    number_to_guess = random.randint(1, 100)

    attempts = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    while True:
        
        user_guess = input("Take a guess: ")
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("That's not a valid number!")
            continue

       
        attempts += 1


        if user_guess == number_to_guess:
            print(f"Congratulations! You found the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")

if __name__ == "__main__":
    number_guessing_game()

