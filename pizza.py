from collections import defaultdict
from enum import Enum


class Size(Enum):
    """This is done for sizes checkup using the EAFP-paradigm."""
    M = 0
    L = 1
    XL = 2


class PizzaBase:
    """A basic class for pizza creating

    Has a returnable dict of basic ingredients, their amount and size.
    """

    def __init__(self, size: str = "L") -> None:
        self.size = size
        ingredients = defaultdict(int)
        ingredients.setdefault(0)
        ingredients["tomato sauce"] = 200
        ingredients["mozzarella"] = 200
        self._ingredients = ingredients

    @property
    def size(self) -> str:
        return self._size

    def ingredients(self) -> defaultdict:
        return self._ingredients

    @size.setter
    def size(self, value: str) -> None:
        """This weird setter checkup is how it is made in EAFP, lol."""
        try:
            self._size = Size[value].name
        except KeyError:
            raise KeyError("Size is not suitable.")

    def __hash__(self) -> int:
        return hash((self.ingredients, self._size))

    def __eq__(self, other) -> bool:
        """Better type of checkup."""
        if isinstance(other, PizzaBase):
            return self.ingredients == other.ingredients
        raise TypeError("Plz compare pizza and pizza.")

    def __repr__(self) -> str:
        return self.__class__.__name__


class Margherita(PizzaBase):
    """Everything is clear here.

    A margherita pizza class.
    """
    def __init__(self, *args, **kwargs) -> None:
        super(Margherita, self).__init__(*args, **kwargs)
        self._ingredients["tomatoes"] = 250


class Pepperoni(PizzaBase):
    """Wow! A Pepperoni pizza class!"""
    def __init__(self, *args, **kwargs) -> None:
        super(Pepperoni, self).__init__(*args, **kwargs)
        self._ingredients["pepperoni"] = 250


class Hawaiian(PizzaBase):
    """No docstring here (actually there is one)."""
    def __init__(self, *args, **kwargs) -> None:
        super(Hawaiian, self).__init__(*args, **kwargs)
        self._ingredients["pineapples"] = 300
