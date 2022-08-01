from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Pizza(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def product_pizza_1(self) -> None:
        pass

    @abstractmethod
    def product_pizza_2(self) -> None:
        pass

    @abstractmethod
    def product_pizza_3(self) -> None:
        pass

class PizzaCook(Pizza):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = PizzaUser()

    @property
    def product(self) -> None:
        product = self._product
        self.reset()
        return product

    def product_pizza_1(self) -> None:
        self._product.add("сыр")

    def product_pizza_2(self) -> None:
        self._product.add("бекон")

    def product_pizza_3(self) -> None:
        self._product.add("перец")


class PizzaUser:
    def __init__(self) -> None:
        self.pats = []

    def add(self, part: Any) -> None:
        self.pats.append(part)

    def show_list(self) -> None:
        print(f"Пицца состоит из инградиентов:{self.pats}")


class Administrator:

    def __init__(self) -> None:
        self._prepares = None

    @property
    def prepares(self) -> Pizza:
        return self._prepares

    @prepares.setter
    def prepares(self, prepares: Pizza):
        self._prepares = prepares

    def prepares_cheese(self):
        self.prepares.product_pizza_1()

    def prepares_cheese_bacon(self):
        self.prepares.product_pizza_1()
        self.prepares.product_pizza_2()

    def prepares_cheese_bacon_pepper(self):
        self.prepares.product_pizza_1()
        self.prepares.product_pizza_2()
        self.prepares.product_pizza_3()


if __name__ == "__main__":
    administrator = Administrator()
    prepares = PizzaCook()
    administrator.prepares = prepares

    print("------------ Pizza cheese ---------------------")

    administrator.prepares_cheese()
    prepares.product.show_list()

    print("-----------------------------------------")

    print("------------ Pizza cheese bacon ---------------------")

    administrator.prepares_cheese_bacon()
    prepares.product.show_list()

    print("-----------------------------------------")

    print("------------ Pizza cheese bacon pepper ---------------------")

    administrator.prepares_cheese_bacon_pepper()
    prepares.product.show_list()

    print("-----------------------------------------")