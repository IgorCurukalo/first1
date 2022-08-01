import datetime


def povestka_sud(date):
    def real_decorator(function):
        def wraper_function(*args, **kwargs):
            print(f'Судебная повестка.\n')
            function(*args, **kwargs)
            print(f'Дата проведения судебного заседания: {date}')
        return wraper_function
    return real_decorator

@povestka_sud((datetime.datetime.now() + datetime.timedelta(days=7, hours=10)).replace(second=0, microsecond=0))
def message_function(a, b, c):
    print(f"Суд вызывает, Вас, в качестве истца (ответчика):\n{a} {b} {c}!\n")

message_function("Сидоров", "Иван", "Петрович")