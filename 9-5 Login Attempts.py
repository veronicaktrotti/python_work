class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}, Email: {self.email}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating an instance of User
user1 = User("John", "Doe", 30, "john.doe@example.com")

# Simulating multiple login attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Printing the current number of login attempts
print(f"Login attempts: {user1.login_attempts}")

# Resetting login attempts
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")
