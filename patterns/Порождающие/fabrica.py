'''Порождающие паттерны
Фабричный метод (Factory Method) - паттерн, порождающий классы.
Определяет интерфейс для создания объекта, но оставляет подклассам решение о том, какой класс инстанцировать.
Позволяет делегировать инстанцирование подклассам.
Абстрактная фабрика часто реализуется с помощью фабричных методов.
Фабричные методы часто вызываются внутри шаблонных методов.
'''

from __future__ import annotations
from abc import ABC, abstractmethod

class Fabrica(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Mi proizvodim {product}"


class LaptopFabrica(Fabrica):
    def factory_method(self) -> Product:
        return LaptopProduct().main_process()


class SmartFabrica(Fabrica):
    def factory_method(self) -> Product:
        return SmartphoneProduct().main_process()


class Product(ABC):

    @abstractmethod
    def main_process(self) -> str:
        ...


class SmartphoneProduct(Product):

    def main_process(self) -> str:
        return "Gadget kotoriy umeet zvonit"


class LaptopProduct(Product):

    def main_process(self) -> str:
        return "Skladivayuschiysya gadget dlya raboty"

def client_code(fabrica: Fabrica) -> None:
    print(f"Ya kupil kakoy-to gadget u kompanii. Oni mne skazali pri prodage: {fabrica.some_operation()}")


if __name__ == "__main__":
    print("Deniy 1 mne schto-to prodaly")
    client_code(LaptopFabrica())
    print("Deniy 2 mne schto-to prodaly")
    client_code(SmartFabrica())
