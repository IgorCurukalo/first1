from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Furniture(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def product_furniture_1(self) -> None:
        pass

    @abstractmethod
    def product_furniture_2(self) -> None:
        pass

    @abstractmethod
    def product_furniture_3(self) -> None:
        pass

class CreatingFurniture(Furniture):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = StyleFurniture()

    @property
    def product(self) -> None:
        product = self._product
        self.reset()
        return product

    def product_furniture_1(self) -> None:
        self._product.add("Шкаф")

    def product_furniture_2(self) -> None:
        self._product.add("Диван")

    def product_furniture_3(self) -> None:
        self._product.add("Кресло")

    def product_furniture_4(self) -> None:
        self._product.add("Стенка под ТВ")

    def product_furniture_5(self) -> None:
        self._product.add("Кровать")


class StyleFurniture:
    def __init__(self) -> None:
        self.price_list = []

    def add(self, part: Any) -> None:
        self.price_list.append(part)

    def show_list(self) -> None:
        print(f"Мебель: {self.price_list}")


class СollectorFurniture:

    def __init__(self) -> None:
        self._assembling = None

    @property
    def assembling(self) -> Furniture:
        return self._assembling

    @assembling.setter
    def assembling(self, assembling: Furniture):
        self._assembling = assembling

    def assembling_classic(self):
        self.assembling.product_furniture_5()

    def assembling_loft(self):
        self.assembling.product_furniture_2()
        self.assembling.product_furniture_3()

    def assembling_hi_tech(self):
        self.assembling.product_furniture_1()
        self.assembling.product_furniture_2()
        self.assembling.product_furniture_3()
        self.assembling.product_furniture_4()


if __name__ == "__main__":
    collector = СollectorFurniture()
    assembling = CreatingFurniture()
    collector.assembling = assembling

    print("-------Furniture classic-----")
    collector.assembling_classic()
    assembling.product.show_list()
    print("-----------------------------")

    print("--------Furniture loft-------")
    collector.assembling_loft()
    assembling.product.show_list()
    print("-----------------------------")

    print("-------Furniture hi tech-----")
    collector.assembling_hi_tech()
    assembling.product.show_list()
    print("-----------------------------")