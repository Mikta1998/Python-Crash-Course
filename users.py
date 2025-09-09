class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"User's first and last name is {self.first_name} {self.last_name}")

    
    def greet_user(self):
        print(f"Welcome back {self.first_name} {self.last_name}")

    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"There have been a total of {self.login_attempts} made.")

    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts have been reset to 0")


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def show_privileges(self):
        print(f"An admin can execute the following commands:")
        for privilege in self.privileges:
            print(privilege)
    


class Admin(Users):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

    


"""user1 = Users("Filip", "Timov")
user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

admin = Admin("Mikta", "Timov")
admin.privileges.show_privileges()"""