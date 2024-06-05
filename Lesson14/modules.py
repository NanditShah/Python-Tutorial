from math import pi # importing specific object from module
import sys # importing entire module

import random as rdm #Giving alias name to import
from enum import Enum
import kansas
from rps7 import playRPS

print(pi)

# for item in dir(rdm):
#     print(item)

print(kansas.capital)
kansas.randomfunfact()

print(__name__)
print(kansas.__name__)

playRPS()