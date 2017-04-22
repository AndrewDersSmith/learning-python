"""
def option():
    input = input("Wich option do you pick?\n")
    if input == int(userInput):
        return input
    elif input == float(userInput):
        return input
    else:
        return print("That aint no number, son!")
"""

def multiplication():
    print("Lol math\n")


def division():
    print("Lol division\n")


def powerof():
    print("lol power of\n")

while True:
    options = {1: "Multiplications", 2: "Division", 3: "Power of"}
    print("Welcome to my Calculator!")
    for x in options:
        print("Option ", x, options[x])

    done = False
    while done == False:
        try:
            userInput = int(input("Enter something: "))
        except ValueError:
            print("Not an integer!")
            continue

    if userInput == 2:
        division()
        continue

    if userInput == 3:
        powerof()
        continue

    if userInput not in options.keys():
        print("Hey!! Thats not allowed\nTry again, bitch\n")
        continue
