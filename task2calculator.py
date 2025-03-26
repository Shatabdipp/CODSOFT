import math
import sys
from colorama import Fore, Style, init

# Initialize Colorama for Windows compatibility
init(autoreset=True)

def format_result(result):
    """Ensures whole numbers are displayed as integers without .0"""
    return int(result) if result == int(result) else round(result, 4)

def calculator():
    print(Fore.CYAN + "Welcome to the Advanced Calculator!\n")

    while True:
        try:
            print(Fore.YELLOW + "\nOperations Available:")
            print(Fore.GREEN + " +  |  -  |  *  |  /  |  **  |  %  |  sqrt  |  sin  |  cos  |  tan  |  log  |  !")
            
            operation = input(Fore.BLUE + "\nChoose an operation: ").strip().lower()

            if not operation:
                print(Fore.RED + "Error: No operation entered! Please enter a valid operation.")
                continue  

            valid_operations = {"+", "-", "*", "/", "**", "%", "sqrt", "sin", "cos", "tan", "log", "!"}
            if operation not in valid_operations:
                print(Fore.RED + f"Error: '{operation}' is not a valid operation! Try again.")
                continue

            if operation in ["sin", "cos", "tan"]:
                num = float(input(Fore.YELLOW + "Enter angle in degrees: "))
                radians = math.radians(num)
                result = {"sin": math.sin, "cos": math.cos, "tan": math.tan}[operation](radians)
                print(Fore.MAGENTA + f"{operation}({num}°) = {format_result(result)}")

            elif operation == "log":
                num = float(input(Fore.YELLOW + "Enter number: "))
                if num <= 0:
                    print(Fore.RED + "Error: Logarithm is only defined for positive numbers.")
                    continue
                base = input(Fore.YELLOW + "Enter base (press Enter for base 10): ").strip()
                base = float(base) if base else 10
                result = math.log(num, base)
                print(Fore.MAGENTA + f"log_{base}({num}) = {format_result(result)}")

            elif operation == "!":
                num = input(Fore.YELLOW + "Enter a non-negative integer: ").strip()
                if not num.isdigit():
                    print(Fore.RED + "Error: Factorial is only defined for non-negative integers!")
                    continue
                num = int(num)
                result = math.factorial(num)
                print(Fore.MAGENTA + f"{num}! = {result}")

            elif operation == "sqrt":
                num = float(input(Fore.YELLOW + "Enter a number: "))
                if num < 0:
                    print(Fore.RED + "Error: Square root is not defined for negative numbers!")
                    continue
                result = math.sqrt(num)
                print(Fore.MAGENTA + f"√{num} = {format_result(result)}")

            else:
                num1 = float(input(Fore.YELLOW + "Enter first number: "))
                num2 = float(input(Fore.YELLOW + "Enter second number: "))

                if operation == "/" and num2 == 0:
                    print(Fore.RED + "Error: Cannot divide by zero!")
                    continue

                result = {
                    "+": num1 + num2,
                    "-": num1 - num2,
                    "*": num1 * num2,
                    "/": num1 / num2,
                    "**": num1 ** num2,
                    "%": num1 % num2
                }[operation]

                print(Fore.MAGENTA + f"Result: {format_result(num1)} {operation} {format_result(num2)} = {format_result(result)}")

        except ValueError:
            print(Fore.RED + "Error: Invalid input! Please enter numbers only.")

        cont = input(Fore.BLUE + "\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != "yes":
            print(Fore.CYAN + "Goodbye! Thanks for using the Advanced Calculator.")
            sys.exit()

if __name__ == "__main__":
    calculator()
