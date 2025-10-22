from utils import add, subtract, divide, multiply


def calculator():
    '''Simple calculator with add, subtract, multiply and divide functions.'''

    consent = True
    while consent:
        print("\n--- Calculator Menu ---")
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        num1, num2 = 0, 0

        operation = input("\nEnter operation (1-4): ").strip()

        if operation not in ['1', '2', '3', '4']:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        while type(num1) is not float or type(num2) is not float:
            try:
                num1 = float(input("Enter first number: ").strip())
                num2 = float(input("Enter second number: ").strip())

                if operation == '1':
                    result = add(num1, num2)
                    print(f"The result of addition is: {result}")
                elif operation == '2':
                    result = subtract(num1, num2)
                    print(f"The result of subtraction is: {result}")
                elif operation == '3':
                    result = multiply(num1, num2)
                    print(f"The result of multiplication is: {result}")
                elif operation == '4':
                    if num2 == 0:
                        print("Cannot divide by zero.")
                    else:
                        result = divide(num1, num2)
                        print(f"The result of division is: {result}")

            except ValueError:
                print('Invalid input. Please enter numeric values.')
                continue

        while True:
            user_consent = input(
                "\nDo you want to perform another operation? (yes/no): "
            ).strip().lower()
            if user_consent == 'no':
                consent = False
                print("Thank you for using the calculator. Goodbye!")
                break
            elif user_consent == 'yes':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    calculator()
