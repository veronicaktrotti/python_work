# 10-4. Guest Book

print("Welcome to the Guest Book!")
print("Enter 'q' at any time to quit.\n")

# Open the file in append mode
with open("guest_book.txt", "a") as file:
    while True:
        name = input("Please enter your name: ")
        if name.lower() == 'q':
            print("Thank you for visiting!")
            break
        print(f"Hello, {name}! Thanks for signing the guest book.")
        file.write(f"{name} visited.\n")
