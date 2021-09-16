import random
from pprint import pprint
from time import sleep
import time
from  .constants import CONSTANT_A, magic_number


def fun_roll_dice(number, sides):
    total = 0
    rolls = []
    for x in range(1, number+1):
        role = random.randint(1, sides)
        total = total+role
        rolls.append(role)
        rolls.sort()
    return {'total': total, 'rolls': rolls}


def guess_number(num):
    result = fun_roll_dice(1,4) ['total']
    if result == num:
        return "You win!"
    else:
        return "You lost!"


CONSTANT_A = 12
def double():
    return CONSTANT_A * 2

def the_magic_number():
    return magic_number() *2

class test_class:

    def __init__(self):
        self.data = None

    def load_data(self):
        time.sleep(4)
        self.data = 'slow data'
        return self.data

def slow_dataset():
    dataset = test_class()
    return dataset.load_data()

