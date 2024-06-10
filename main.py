# write your code here
from random import randint
OPERATORS = ["+", "-", "*"]
INTEGRALS = [11, 29]
LEVELS = {1: "1 (simple operations with numbers 2-9)",
          2: "2 (integral squares of 11-29)"}


def level_choice():
    while True:
        try:
            level = int(input("""Which level do you want? Enter a number:
            1 - simple operations with numbers 2-9
            2 - integral squares of 11-29"""))
        except ValueError:
            print("Incorrect format.")
            continue

        if level not in [1, 2]:
            print("Incorrect format.")
            continue
        else:
            break
    return level

level = level_choice()

result = 0
if level == 1:
    for _ in range(5):
        expression = f"{randint(2, 9)} {OPERATORS[randint(0, 2)]} {randint(2, 9)}"
        print(expression)
        while True:
            try:
                user = int(input())
                if eval(expression) == user:
                    print("Right!")
                    result += 1
                else:
                    print("Wrong!")
                break
            except ValueError:
                print("Incorrect format.")

else:
    for _ in range(5):
        expression = randint(INTEGRALS[0], INTEGRALS[1])
        print(expression)
        while True:
            try:
                user = int(input())
                if expression ** 2 == user:
                    print("Right!")
                    result += 1
                else:
                    print("Wrong!")
                break
            except ValueError:
                print("Incorrect format.")

print(f"Your mark is {result}/5.")

save = input("Would you like to save your result to the file? Enter yes or no.")
if save in ["yes", "YES", "y", "Yes"]:
    name = input("What is your name?")
    with open("results.txt", "a") as f:
        f.write(f"{name}: {result}/5 in level {LEVELS.get(level)}.\n")
    print('The results are saved in "results.txt".')
