class Travel:
    def __init__(self, strategy):
        self.strategy = strategy

    def start(self):
        self.strategy.travel()


class Car:
    def travel(self):
        print("Travelling By Car")


class Bike:
    def travel(self):
        print("Travelling By Bike")


class Walk:
    def travel(self):
        print("Travelling By Walking")


print("=== CHOOSE YOUR ROUTE ===")
print("1. By Car")
print("2. By Bike")
print("3. By Walk")

choice = int(input("Enter your choice: "))
match choice:

    case 1:
        strategy = Car()
        travel = Travel(strategy)
        travel.start()

    case 2:
        strategy = Bike()
        travel = Travel(strategy)
        travel.start()

    case 3:
        strategy = Walk()
        travel = Travel(strategy)
        travel.start()

    case _:
        print("Invalid travel method")
        exit()