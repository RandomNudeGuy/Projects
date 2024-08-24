# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to subtract one number from another
def subtract(x, y):
    return x - y

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Define a function to divide one number by another
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main code
print("Welcome to the Nigster Calc!")
print("(calc is short for calculator chat)")
print("Choose:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user to select the operation
choice = input("Enter choice (1/2/3/4): ")

# Take input from the user for the numbers to operate on
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the chosen operation and store the result
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    print("Invalid input")
    result = None

print("Result:", result)

# Continue the operations indefinitely until the user decides to stop
while True:
    print("Do you want to continue?")
    print("1. Yes")
    print("2. No")

    choice2 = input("Enter choice (1/2): ")

    if choice2 == '2':
        print("Eat Shit!")
        break
    elif choice2 == '1':
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        # Take input from the user to select the operation
        choice3 = input("Enter choice (1/2/3/4): ")

        # Take input from the user for the next number to operate on
        num3 = float(input("Enter next number: "))

        # Perform the chosen operation on the current result
        if choice3 == '1':
            result = add(result, num3)
        elif choice3 == '2':
            result = subtract(result, num3)
        elif choice3 == '3':
            result = multiply(result, num3)
        elif choice3 == '4':
            result = divide(result, num3)
        else:
            print("Invalid input")

        print("Result:", result)
    else:
        print("Invalid input, please choose 1 or 2.")

