import pygame
import math
import sys


# Helper function to format numbers
def format_number(number):
    if number >= 1000000:
        return f"{number:.2e}"  # Scientific notation for large numbers
    return f"{number:.2f}"  # 2 decimal places for small numbers


