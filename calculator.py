def calculator():
    print("START")
    
    # First input
    print("Please input a number")
    x = float(input("User input = "))
    
    # Second input
    print("Please enter another number")
    y = float(input("User input = "))
    
    # Operation selection
    print("Select operation:")
    print("1. Subtraction (x - y)")
    print("2. Multiplication (x * y)")
    print("3. Addition (x + y)")
    print("4. Division (x / y)")
    
    operation = input("Enter the number of your chosen operation (1-4): ")
    
    # Perform calculation based on selected operation
    if operation == '1':
        result = x - y
    elif operation == '2':
        result = x * y
    elif operation == '3':
        result = x + y
    elif operation == '4':
        if y != 0:
            result = x / y
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation selected"
    
    # Output result
    print(f"Output: {result}")
    
    print("END")

# Run the calculator
calculator()