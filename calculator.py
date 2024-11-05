def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def show_menu():
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Choose an operation (1/2/3/4/5): "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Invalid input! Please choose a valid option (1-5).")
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def calculator():
    while True:
        show_menu()  # Display the menu
        choice = get_user_choice()  # Get user's operation choice

        if choice == 5:
            print("Exiting the calculator. Goodbye!")
            break  # Exit the calculator

        num1, num2 = get_numbers()  # Get the two numbers to perform calculation

        if choice == 1:
            result = add(num1, num2)
            print(f"The result is: {result}")
        elif choice == 2:
            result = subtract(num1, num2)
            print(f"The result is: {result}")
        elif choice == 3:
            result = multiply(num1, num2)
            print(f"The result is: {result}")
        elif choice == 4:
            result = divide(num1, num2)
            print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()




    