'''Паттерны поведения
Стратегия (Strategy) - паттерн поведения объектов.
Определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми.
Стратегия позволяет изменять алгоритмы независимо от клиентов, которые ими пользуются.
'''

from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    @abstractmethod
    def select(self, menu_list, dish, ingredients):
        pass


class PizzaMenuSelection(Strategy):
    def select(self, menu_list, dish, ingredients: list):
        rezult_menu_list = {}
        for i in menu_list:
            menu_dish = i.split(' ')
            if menu_dish[0] == dish and str(ingredients).strip('[]') in str(menu_list[i]).strip('[]'):
                rezult_menu_list[i] = menu_list[i]
        return rezult_menu_list


class GamburgerMenuSelection(Strategy):
    def select(self, menu_list, dish, ingredients):
        rezult_menu_list = {}
        for i in menu_list:
            menu_dish = i.split(' ')
            if menu_dish[0] == dish and str(ingredients).strip('[]') in str(menu_list[i]).strip('[]'):
                rezult_menu_list[i] = menu_list[i]
        return rezult_menu_list


class DrinkMenuSelection(Strategy):
    def select(self, menu_list, dish, ingredients):
        rezult_menu_list = {}
        for i in menu_list:
            menu_dish = i.split(' ')
            if menu_dish[0] == dish and str(ingredients).strip('[]') in str(menu_list[i]).strip('[]'):
                rezult_menu_list[i] = menu_list[i]
        return rezult_menu_list



class Menu:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def lists(self, menu_list, dish, ingredients):
        result = self._strategy.select(menu_list, dish, ingredients)
        print(result)


if __name__ == "__main__":
    menu_list = {'Pizza 1': 'cheese',
                 'Pizza 2': 'cheese,sausage',
                 'Pizza 3': 'sausage,pepper',
                 'Pizza 4': 'cheese,ham',
                 'Gamburger 1': 'bread,cheese,chicken cutlet',
                 'Gamburger 2': 'bread,cheese,beef cutlet,bacon,onion',
                 'Gamburger 3': 'bread,cheese,beef cutlet',
                 'Drink 1': 'cola',
                 'Drink 2': 'coca cola',
                 'Drink 3': 'coca cola zero',
                 'Drink 4': 'sprite',
                 'Drink 5': 'fanta',
                 'Drink 6': 'cappuccino coffee',
                 'Drink 7': 'macachino coffee',
                 'Drink 8': 'espresso coffee',
                 }

    pizza = Menu(PizzaMenuSelection())
    gamburger = Menu(GamburgerMenuSelection())
    drink = Menu(DrinkMenuSelection())

    pizza.lists(menu_list, 'Pizza', 'cheese')
    gamburger.lists(menu_list, 'Gamburger', 'bread,cheese,beef cutlet')
    drink.lists(menu_list, 'Drink', 'cola')


