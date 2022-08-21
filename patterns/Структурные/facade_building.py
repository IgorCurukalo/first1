'''Структурные паттерны
Фасад (Facade) - паттерн, структурирующий объекты.
Предоставляет унифицированный интерфейс вместо набора интерфейсов некоторой подсистемы.
Фасад определяет интерфейс более высокого уровня, который упрощает использование подсистемы.
'''

class BuildingManager:

    def search_for_contractors(self):
        print('I\'m find contractors')

    def contractor_control(self):
        print('I\'m control contractor')

    def accept_construction_site(self):
        print('I\'m accept the construction site')

class Architector:

    def create_construction_plan(self):
        print('I\'m creating a construction plan')


class SalesManager:

    def looking_investors(self):
        print('I\'m looking for investors')

    def selling(self):
        print('I\'m selling')


class Accounting():

    def give_salary(self):
        print('I\'m give salary to contractor')

    def give_awards(self):
        print('I\'m give awards to contractor')


class Construction:

    def digging_moat(self):
        print('I\'m digging a moat')

    def hammers_piles(self):
        print('I\'m piles are hammered')

    def fills_foundation(self):
        print('I\'m fill the foundation')

    def laying_brick(self):
        print('I\'m laying a brick')

    def insert_windows_doors(self):
        print('I\'m insert windows and doors')

    def internal_works(self):
        print('I\'m insert windows and doors')



class Facade:
    def __init__(self):
        self.salesmanager = SalesManager()
        self.buildingmanager = BuildingManager()
        self.architector = Architector()
        self.accounting = Accounting()
        self.construction = Construction()

    def itog(self):
        for i in range(30):
            self.salesmanager.looking_investors()

        for i in range(30):
            self.architector.create_construction_plan()

        for i in range(7):
            self.buildingmanager.search_for_contractors()

        for i in range(2):
            for j in range(30):
                self.buildingmanager.contractor_control()
                self.construction.digging_moat()
            self.accounting.give_salary()
            self.accounting.give_salary()

        for i in range(2):
            for j in range(30):
                self.buildingmanager.contractor_control()
                self.construction.hammers_piles()
            self.accounting.give_salary()
            self.accounting.give_salary()


        for i in range(30):
            self.buildingmanager.contractor_control()
            self.construction.fills_foundation()
        self.accounting.give_salary()
        self.accounting.give_salary()

        for i in range(30):
            self.buildingmanager.contractor_control()
            self.construction.laying_brick()
        self.accounting.give_salary()
        self.accounting.give_salary()

        for i in range(14):
            self.buildingmanager.contractor_control()
            self.construction.insert_windows_doors()

        for i in range(14):
            self.buildingmanager.contractor_control()
            self.construction.internal_works()
        self.accounting.give_salary()
        self.accounting.give_salary()
        self.buildingmanager.accept_construction_site()

        for i in range(100):
            self.salesmanager.selling()


if __name__ == "__main__":
    facade = Facade()
    facade.itog()