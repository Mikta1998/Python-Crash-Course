class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in responde to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over")

    def show_age(self):
        print(f"{self.name} is {self.age} years old.")


my_dog = Dog("Loki", 3)

print(my_dog.name)
print(my_dog.age)

print("\n")

my_dog.sit()
my_dog.roll_over()
my_dog.show_age()