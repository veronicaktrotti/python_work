# List of sandwich orders
sandwich_orders = ["tuna", "chicken", "veggie", "turkey", "ham and cheese"]

# Empty list for finished sandwiches
finished_sandwiches = []

# Process each sandwich order
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print finished sandwiches
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")