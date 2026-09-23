from app.calculator import Calculator

def main():
    print("Welcome to the Calculator!")
    while True:
        operation = input("Choose operation (add, subtract, multiply, divide, or exit): ").lower()
        if operation == "exit":
            print("Goodbye!")
            break
        if operation not in ("add", "subtract", "multiply", "divide"):
            print("Invalid operation. Please try again.")
            continue
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter numeric values.")
            continue
        try:
            result = Calculator.calculate(a, b, operation)
            print(f"Result: {result}")
        except ValueError as error:
            print(f"Error: {error}")
if __name__ == "__main__":
    main()