#Pylint Tutorial
"""Pylint tutorial."""
class Car: #pylint: disable=too-few-public-methods
    """Test class for Pylint Tutorial."""

    def __init__(self, color) -> None:
        self.color = color

my_car = Car("blue")

def crash(car1, car2): #pylint: disable= unused-argument
    "Crash function."

    car1.color = "burnt"

crash(Car("red"), my_car)
