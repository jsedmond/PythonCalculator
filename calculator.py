def add(num1, num2):
    """Returns num1 plus num2."""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2."""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 times num2."""
    return num1 * num2


def div(num1, num2):
    """Returns num1 divided by num2."""
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Handled div by zero. Returning zero.")
        return 0


def runOperation(operation, num1, num2):
    """Determines the operation to run based on the operation argument
    which should be passed in as an int."""
    #  Determine the operation
    if (operation == 1):
        print("Adding...")
        print(add(num1, num2))
    elif (operation == 2):
        print("Subtracting...")
        print(sub(num1, num2))
    elif (operation == 3):
        print("Multiplying...")
        print(mul(num1, num2))
    elif (operation == 4):
        print("Dividing...")
        print(div(num1, num2))
    else:
        print("I don't understand")


def main():
    """Allows user to run basic calculator operations with two numbers."""
    validInput = False
    while not validInput:
        # Get user input
        try:
            num1 = int(input("What is your first number? "))
            num2 = int(input("What is your second number? "))
            operation = int(input("What do you want to do? 1) Add, 2) Subtract, 3) Multiply and 4) Divide). "
                                  " Enter  number: "))
            validInput = True
        except ValueError:
            print("Invalid input. Try again.")
        except:
            print("Unknown error")
        runOperation(operation, num1, num2)

main()