"""
Simple Calculator - Performs basic arithmetic operations
Skills: Basic syntax, user input, conditionals
"""

def add(a, b):
    """Returns the sum of two numbers"""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers"""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b
1
def divide(a, b):
    """Returns the quotient of two numbers"""
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

def get_number(prompt):
    """Helper function to get a valid number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    """Main function to run the calculator"""
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)
    print("\nAvailable operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        print("\n" + "-" * 40)
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue
        
        # Get two numbers from user
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        # Perform the selected operation
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        
        # Display the result
        if isinstance(result, str):  # Error message
            print(f"Result: {result}")
        else:
            print(f"Result: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
