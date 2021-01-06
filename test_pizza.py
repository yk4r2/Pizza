import pytest
from collections import defaultdict
from pizza import PizzaBase, Margherita, Pepperoni, Hawaiian


@pytest.mark.parametrize(
    "pizza_class, name",
    [
        (Margherita, "Margherita"),
        (Pepperoni, "Pepperoni"),
        (Hawaiian, "Hawaiian"),
    ]
)
def test_pizza(pizza_class, name: str):
    assert str(pizza_class) == name
    assert pizza_class.size == "L"


def test_size_comparison():
    assert Hawaiian(size="L") != Hawaiian(size="XL")
    assert Margherita() != Hawaiian() != Pepperoni()


def test_ingreds():
    ingredients = defaultdict()

