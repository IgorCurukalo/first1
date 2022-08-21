'''Порождающие паттерны
Одиночка (Singleton) - паттерн, порождающий объекты.
Гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа.
С помощью паттерна одиночка могут быть реализованы многие паттерны (абстрактная фабрика, строитель, прототип).
'''

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def get_logic(self):
        ...

if __name__ == "__main__":
    sing1 = Singleton()
    sing2 = Singleton()

    if id(sing1) == id(sing2):
        print('Все работает корректно, id двух классов синглтона равны')
    else:
        print('Что-то пошло не по плану')