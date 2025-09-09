from my_new_users import Users

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