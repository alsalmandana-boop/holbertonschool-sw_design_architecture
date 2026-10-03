#!/usr/bin/env python3
"""Decorator design pattern example."""


class Beverage:
    """Base beverage interface."""

    def cost(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class Coffee(Beverage):
    """Basic coffee."""

    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class MilkDecorator(Beverage):
    """Add milk to a beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Add sugar to a beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Add caramel to a beverage."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    """Run decorator examples."""
    drink1 = MilkDecorator(Coffee())
    print(drink1.description(), drink1.cost())

    drink2 = MilkDecorator(SugarDecorator(Coffee()))
    print(drink2.description(), drink2.cost())

    drink3 = CaramelDecorator(
        MilkDecorator(
            SugarDecorator(
                Coffee()
            )
        )
    )
    print(drink3.description(), drink3.cost())


if __name__ == "__main__":
    main()
