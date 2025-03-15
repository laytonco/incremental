import pygame
import math
import sys


# Helper function to format numbers
def format_number(number):
    if number >= 1000000:
        return f"{number:.2e}"  # Scientific notation for large numbers
    return f"{number:.2f}"  # 2 decimal places for small numbers


def order_pizza(size, *toppings, **details):
    print(f"Ordering a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

    print(details)
order_pizza("large", "pepperoni", "mushrooms", "onions", delivery="Express", table=12)
