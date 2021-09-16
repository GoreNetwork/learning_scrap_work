import sys
sys.path.insert(1, "D:\github\learning_scrap_work\pytest")
import app.roll_dice
# from app.roll_dice import (fun_roll_dice, guess_number, 
#                     double, the_magic_number, slow_dataset )

from app.roll_dice import *

from unittest import mock
from pprint import pprint

import time

# mock_roll_dice = mock.Mock(name='roll dice mock', return_value={
#                            'rolls': [3], 'total': 3})



# pprint(mock_roll_dice(3, 8))


@mock.patch('app.roll_dice.fun_roll_dice')
def test_guess_rolls(mock_roll_dice):
    mock_roll_dice.return_value={'rolls': [3], 'total': 3}
    assert guess_number(3) == "You win!"

# change value of CONSTANT_A
# Imported files are objects
# This changes what constant_a is into a 2
def test_mocking_constant_a(mocker):
    mocker.patch.object(app.roll_dice, 'CONSTANT_A', 2)
    expected = 4  
    actual = double()  # now it returns 4, not 2

    assert expected == actual

# change value of CONSTANT_A
# Imported files are objects
# 2 is the return value

def fake_magic_number():
    return 4

# replace object (from the constants import in roll_dice.py) magic_number with the 
# function fake_magic_number from above
def test_mocking_constant_a(mocker):
    mocker.patch.object(app.roll_dice, 'magic_number', fake_magic_number)
    expected = 8  
    actual = the_magic_number()  

    assert expected == actual    


def test_mocking_class_method(mocker):
    expected = 'xyz'
    # expected = 'slow data'

    def mock_load(self):
        return 'xyz'

    mocker.patch(
        # test_class is in slow.py, but imported to main.py
        'app.roll_dice.test_class.load_data',  mock_load
    )
    actual = slow_dataset()
    pprint (dir(actual))
    print (actual)
    assert expected == actual