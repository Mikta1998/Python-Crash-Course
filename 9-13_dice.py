import random



class Lottery:
    def __init__(self, my_ticket:list, my_stars:list):
        self.my_ticket = my_ticket
        self.my_stars = my_stars
        self.numbers = list(range(1,51))
        self.stars = [1,2,3,4,5,6,7,8,9]
        self.counter = 0


    def my_odds_of_winning(self):
        self.new_numbers = random.sample(self.numbers, 5)
        self.new_stars = random.sample(self.stars, 2)
        while set(self.my_ticket) != set(self.new_numbers) or set(self.my_stars) != set(self.new_stars):
            self.new_numbers = random.sample(self.numbers, 5)
            self.new_stars = random.sample(self.stars, 2)
            self.counter += 1
        print(self.counter)


my_lottery = Lottery([2, 27, 50, 31, 42], [2,9])
my_lottery.my_odds_of_winning()


