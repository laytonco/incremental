import pygame
import math
import sys


# Helper function to format numbers
def format_number(number):
    if number >= 1e6:
        return f"{number:.2e}"  # Scientific notation for numbers >= 1,000,000
    else:
        return f"{number:,.2f}"  # Comma as thousand separator for smaller numbers