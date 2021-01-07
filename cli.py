import sys

import click
from enum import Enum
from random import randint
from collections import defaultdict
from auxiliary.decorators import log
from main.pizza import PizzaBase, Margherita, Hawaiian, Pepperoni, Size

MENU = defaultdict(PizzaBase)
MENU["Margherita"] = Margherita()
MENU["Hawaiian"] = Hawaiian()
MENU["Pepperoni"] = Pepperoni()


class AdjectiveVars(Enum):
    best = 0
    hottest = 1
    tastiest = 2
    heaviest = 3


class ComplementVars(Enum):
    your_life = 0
    the_world = 1
    eastern_Europe = 2
    my_moms_book = 3


@log("Made in {} seconds.")
def bake(pizza: PizzaBase) -> None:
    pass


@log("Delivered in {} seconds.")
def delivery(pizza: PizzaBase) -> None:
    pass


@click.group()
def cli():
    pass


def menu_stringify(string: defaultdict) -> str:
    return ", ".join(string)


@cli.command()
@click.option(
    "--delivery",
    "is_delivered",
    default=False,
    is_flag=True,
    help="If chosen, your order will be delivered.",
)
@click.option("--size", default="L", help="You can choose your pizza size.")
@click.argument("pizza", nargs=1)
def order(pizza: str, size: str, is_delivered: bool):
    """Bakes and deliveres pizza."""
    if pizza not in MENU:
        pizza_str = ("No such pizza but your opinion is very"
                     "important for us (no).\n"
                     "Choose between the possible options: "
                     )
        pizza_str += menu_stringify(MENU)
        print(pizza_str)
        return None
    try:
        Size[size].name
    except KeyError:
        raise KeyError("Size is not suitable.")

    bake(MENU[pizza])
    if is_delivered:
        delivery(MENU[pizza])
    else:
        print("Now you can eat your pizza.")


def random_word_chooser(word_class, var_count: int) -> str:
    return word_class(randint(0, var_count)).name.replace("_", " ")


def ingredients_stringify(pizza) -> str:
    return ", ".join(list(pizza.ingredients().keys())[1:])


@cli.command()
def menu():
    """Returns menu"""
    for pizza in MENU.values():
        adj_variant = random_word_chooser(AdjectiveVars, 3)
        compl_variant = random_word_chooser(ComplementVars, 3)
        # taking all the keys except of the default one.
        ingredients = ingredients_stringify(pizza)
        print(f"- the {adj_variant} {pizza} in {compl_variant}: "
              f"{ingredients}."
              )


if __name__ == "__main__":
    status = cli()
    sys.exit(status)
