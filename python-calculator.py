
def calculator():
    # Prompt user for the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt user for the second number
    num2 = float(input("Enter the second number: "))
    
    # Prompt user for the operation choice
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter your choice (1/2/3/4): ")
    
    # Perform calculation based on the operation choice
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '4':
        if num2 != 0:  # Ensure no division by zero
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice. Please select a valid option.")

# Call the calculator function
calculator()
