import random
import time


def generate_digits():
    digits = []
    while len(digits) < 4:
        random_digit = random.randint(0, 9)
        if random_digit not in digits:
            digits.append(random_digit)
    return digits


def ask_number():
    while True:
        number = input("Enter a number\n")
        if number.isdigit() and len(set(number)) == 4:
            return (list(int(i) for i in number))
        print("You must enter an 4 four digits number with different digits.")


def evaulate_number(guess_number, random_digits):
    result = [0, 0]
    for index, num in enumerate(guess_number):
        if num not in random_digits:
            continue
        if num == random_digits[index]:
            result[0] += 1
        else:
            result[1] += 1
    return result


def result_print(result):
    print("{} bulls, {} cows".format(*result))


def end_game(attempt,time_to_guess):
    if attempt < 5:
        evaulation = "amazing"
    elif attempt < 10:
        evaulation = "average"
    elif attempt < 14:
        evaulation = "not so good"
    else:
        evaulation = "really bad"
    print(f"Correct, you've guessed the right number in {attempt} guesses")
    print(f"Your time to guess the number was {time_to_guess} seconds.")
    print(f"That's {evaulation}!!!")


def main():
    random_digits = generate_digits()
    print("""Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
    guess_number = 0
    attempt = 0
    start_time = time.time()
    while guess_number != random_digits:
        attempt += 1
        guess_number = ask_number()
        result = evaulate_number(guess_number, random_digits)
        result_print(result)
        print("=" * 15)
        print()
    end_time = time.time()
    time_to_guess = int(end_time - start_time)
    end_game(attempt, time_to_guess)


main()