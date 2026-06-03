# Class 18 - Modules and Packages

# Built-in modules - no install needed
import math
import random
import os

# math module
print(math.pi)              # 3.14159...
print(math.sqrt(16))        # 4.0
print(math.floor(3.9))      # 3
print(math.ceil(3.1))       # 4

# random module
print(random.randint(1, 10))        # random number 1 to 10
print(random.choice(["Ali", "Sara", "Omar"]))   # random name

# os module
print(os.getcwd())          # current folder path

# import only what you need
from math import sqrt, pi
print(sqrt(25))             # 5.0
print(pi)                   # 3.14159...

# practical example - dice roller
import random
def roll_dice():
    return random.randint(1, 6)

for i in range(5):
    print(f"Roll {i+1}: {roll_dice()}")
