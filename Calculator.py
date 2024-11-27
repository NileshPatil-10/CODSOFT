def calculator():
    print("Simple Calculator")
    print("------------------")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        choice = int(input("Enter your choice (1-4): "))
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = num1 + num2
            print(f"The result is: {result}")
        elif choice == 2:
            result = num1 - num2
            print(f"The result is: {result}")
        elif choice == 3:
            result = num1 * num2
            print(f"The result is: {result}")
        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
                print(f"The result is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice! Please select a valid operation.")
    except ValueError:
        print("Invalid input! Please enter numeric values for the numbers and a valid integer for the choice.")

# Call the calculator function
calculator()