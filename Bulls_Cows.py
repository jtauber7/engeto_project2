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


def end_game(attempt, time_to_guess, name):
    if attempt < 5:
        evaulation = "amazing"
    elif attempt < 10:
        evaulation = "average"
    elif attempt < 14:
        evaulation = "not so good"
    else:
        evaulation = "really bad"
    print(f"Correct {name}, you've guessed the right number in {attempt} guesses")
    print(f"Your time to guess the number was {time_to_guess} seconds.")
    print(f"That's {evaulation}!!!")


def main():
    random_digits = generate_digits()
    print("""Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
    guess_number = 0
    attempt = 0
    name = input("Please enter your name:\n")
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
    end_game(attempt, time_to_guess, name)
    stats_tab = user_stats(name, attempt, time_to_guess)
    print_stats(stats_tab)

def user_stats(name, attempt, time_to_guess):
    with open("players_stats.txt", "a+") as file:
        print(str(name)+",", str(attempt)+",", str(time_to_guess), file=file)
        file.seek(0)
        stats_tab = [i.strip("\n").split(", ") for i in file.readlines()]
        for row in stats_tab:
            row[1:] = (int(x) for x in row[1:])
        return stats_tab

def print_stats(stats_tab):
    stats_tab.sort(key=lambda row: (row[1], row[2]))
    header = ["Order", "Name", "Attempts", "Time"]
    widths = table_widths(stats_tab)
    c1 = max(len(header[0]), len(str(len(stats_tab))))
    c2 = max(len(header[1]), widths[0] + 2)
    c3 = max(len(header[2]), widths[1] + 2)
    c4 = max(len(header[3]), widths[2] + 2)
    print("="*14)
    print("BEST PLAYERS: ")
    print("="*14)
    firstrow = "| {:^" + str(c1) + "} | {:<" + str(c2) + "} | {:^" + str(c3) + "} | {:^" + str(c4) + "} |"
    print(firstrow.format(*header))
    print("-"*(c1 + c2 + c3 + c4 + 13))
    for i, row in enumerate(stats_tab):
        print(f"| {str(i+1)+'.':^{c1}} | {row[0]:<{c2}} | {row[1]:^{c3}} | {str(row[2])+'s':^{c4}} |")


def table_widths(stats_tab):
    widths = [0] * len(stats_tab[0])
    for row in stats_tab:
        for i, word in enumerate(row):
            if len(str(word)) > widths[i]:
                widths[i] = len(str(word))
    print(widths)
    return widths

main()