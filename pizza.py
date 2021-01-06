from collections import defaultdict
from enum import Enum


class Size(Enum):
    """This is done for sizes checkup using the EAFP-paradigm."""
    L = 1
    XL = 2


class PizzaBase:
    """A basic class for pizza creating

    Has a returnable dict of basic ingredients, their amount and size.
    """

    def __init__(self, size: str = "L"):
        self.size = size
        ingredients = defaultdict(int)
        ingredients.setdefault(0)
        ingredients["tomato sauce"] = 200
        ingredients["mozzarella"] = 200
        self._ingredients = ingredients

    @property
    def size(self):
        return self._size

    @property
    def ingredients(self):
        return self._ingredients

    @size.setter
    def size(self, value: str = "L"):
        """This weird setter checkup is how it is made in EAFP, lol."""
        try:
            self._size = Size[value].name
        except KeyError:
            print("Size is not suitable.")

    def anime(self):
        pass
