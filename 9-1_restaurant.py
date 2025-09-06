class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a Macedonian restaurant and has {self.cuisine_type} cuisine.")


    def open_restaurant(self):
        print(f"The {self.restaurant_name} is now open between 09:00AM and 10:00PM.")

    
    def set_number_served(self, served):
        self.number_served = served
        
    
    def increment_number_served(self, increment):
        self.number_served += increment

    
    def total_customers_served(self):
        print(f"We have served a total of {self.number_served} customers!")

my_restaurant = Restaurant("A New Dawn", "Meso")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

"""print(f"My restaurant has served {my_restaurant.number_served} customers.")
my_restaurant.number_served = 50
print(f"My restaurant has served {my_restaurant.number_served} customers.")"""

my_restaurant.increment_number_served(10)
my_restaurant.total_customers_served()
my_restaurant.increment_number_served(90)
my_restaurant.total_customers_served()

