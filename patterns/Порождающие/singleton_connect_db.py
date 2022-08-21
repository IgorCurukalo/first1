'''Порождающие паттерны
Одиночка (Singleton) - паттерн, порождающий объекты.
Гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа.
С помощью паттерна одиночка могут быть реализованы многие паттерны (абстрактная фабрика, строитель, прототип).
'''

class DataBase:

    __instance = None

    def __init__(self, server, database, user, password):
        self.server = server
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        print(f"Соединение с БД: {self.server}, {self.database}, {self.user}, {self.password}")

    def disconnect(self):
        DataBase.__instance = None
        print("соединение закрыто")

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

# 1 соединение с БД
db = DataBase('localhost', 'first', 'admin', '123456')
db.connect()

# 2 соединение с БД
db2 = DataBase('localhost', 'first', 'admin', '123456')
db2.connect()

# Как видим соединение осталось прежним id одинаковые
print(id(db), id(db2))

# Отсоединяемся от БД и сново подключаемя, как видно id у нас новый
db2.disconnect()
db3 = DataBase('localhost', 'first', 'admin', '123456')
db3.connect()
print(id(db), id(db2), id(db3))

