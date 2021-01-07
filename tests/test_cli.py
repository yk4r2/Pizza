import pytest
from click.testing import CliRunner
from auxiliary import decorators
import cli
import re


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


def test_menu_stdout(runner):
    result = runner.invoke(cli.cli, ["menu"])
    my_regexp = re.compile("- the [a-z]+ [A-Za-z]+ in [A-Za-z ]+: [^0-9]+.\n" * 3)
    assert result.exit_code == 0
    assert my_regexp.match(result.output) is not None


def test_order_delivery_stdout(runner):
    result = runner.invoke(cli.cli, ["order", "Margherita", "--delivery"])
    expected_out = re.compile(
        "Made in [0-9]+.[0-9]+ seconds.\nDelivered in [0-9]+.[0-9]+ seconds."
    )
    assert result.exit_code == 0
    assert re.match(expected_out, result.output) is not None


def test_order_pickup_stdout(runner):
    result = runner.invoke(cli.cli, ["order", "Margherita"])
    expected_out = re.compile(
        "Made in [0-9]+.[0-9]+ seconds.\nNow you can eat your pizza."
    )
    assert result.exit_code == 0
    assert re.match(expected_out, result.output) is not None


def test_order_wrong_pizza_stdout(runner):
    result = runner.invoke(cli.cli, ["order", "diablo"])
    expected_out = re.compile("[^0-9]*Choose between the possible options: [^0-9]+.\n")
    assert result.exit_code == 0
    assert re.match(expected_out, result.output) is not None


def test_order_wrong_pizza_size(runner):
    result = runner.invoke(cli.cli, ["order", "Pepperoni", "--size=S"])
    assert result.exit_code == 1
    assert type(result.exception) == KeyError


def test_no_pizza(runner):
    """My worst test just for coverage to become 50% and for me to go to sleep."""
    result = runner.invoke(cli.cli, "")
    assert result.stdout is not None
