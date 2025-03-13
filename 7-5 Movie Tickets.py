total_cost = 0

while True:
    age = input("Enter your age (or type 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break
    
    if not age.isdigit():
        print("Invalid input. Please enter a valid age or 'quit' to exit.")
        continue
    
    age = int(age)
    
    if age < 3:
        cost = 0
        print("The ticket is free!")
    elif 3 <= age <= 12:
        cost = 10
        print("The ticket is $10.")
    else:
        cost = 15
        print("The ticket is $15.")
    
    while True:
        tickets = input("How many tickets do you need? ")
        
        if not tickets.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
        
        tickets = int(tickets)
        total_cost += cost * tickets
        break
    
    print(f"The total cost of the tickets so far is ${total_cost:.2f}.")
    print("---------------------------")
    
print(f"Final total cost: ${total_cost:.2f}")
