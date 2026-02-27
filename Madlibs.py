print("Welcome to Mad Libs Game developed by Monty")

name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
food = input("Enter a food name: ")
emotion = input("Enter an emotion: ")

story = f"""
One day {name} went to {place}.
There they saw a very {adjective} {animal}.
The {animal} decided to {verb} near the food stall.
{name} felt very {emotion} and started eating {food}.
It was the most memorable day ever.
"""

print("\nYour Mad Libs Story:")
print(story)
