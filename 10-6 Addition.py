# 10.6 Addition

print("Let's add two numbers!")
print("Enter 'q' at any time to quit.\n")

while True:
    first_input = input("Enter the first number: ")
    if first_input.lower() == 'q':
        break

    second_input = input("Enter the second number: ")
    if second_input.lower() == 'q':
        break

    try:
        num1 = int(first_input)
        num2 = int(second_input)
    except ValueError:
        print("Oops! Please enter valid numbers.\n")
    else:
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.\n")
