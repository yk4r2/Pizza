import pytest
from collections import defaultdict
from main.pizza import Margherita, Hawaiian, Pepperoni


@pytest.mark.parametrize(
    "pizza_class, name",
    [
        (Margherita, "Margherita"),
        (Pepperoni, "Pepperoni"),
        (Hawaiian, "Hawaiian"),
    ],
)
def test_pizza_default(pizza_class, name: str):
    assert str(pizza_class()) == name
    assert pizza_class().size == "L"


def test_size_comparison():
    assert Margherita(size="L") != Margherita(size="XL")
    assert Margherita() != Hawaiian() != Pepperoni()


def test_ingredients():
    ingredients = defaultdict(int)
    ingredients.setdefault(0)
    ingredients["tomatoes"] = 250
    ingredients["tomato sauce"] = 200
    ingredients["mozzarella"] = 200
    assert Margherita().ingredients() == ingredients


def test_wrong_size():
    with pytest.raises(KeyError):
        Margherita(size="S")
