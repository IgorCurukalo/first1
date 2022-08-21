'''Структурный паттерн
Адаптер - паттерн, структурирующий классы и объекты.
Преобразует интерфейс одного класса в интерфейс другого, который ожидают клиенты.
Адаптер обеспечивает совместную работу классов с несовместимыми интерфейсами, которая без него была бы невозможна.
'''

class JsonData:
    def __init__(self, some_data):
        self.data = f"{{ {some_data} }}"

    def show_json(self):
        print(self.data)


class XMLData:
    def __init__(self, some_data):
        self.data = f"<tag>{some_data}</tag>"

    def show_xml(self):
        print(self.data)


class Adapter:
    def __init__(self, data):
        super().__init__()
        self.data = data

    def convert_to_json(self):
        self.data = self.data.replace('<tag>', '{')
        self.data = self.data.replace('</tag>', '}')

        print(self.data)

    def convert_to_XML(self):
        self.data = self.data.replace('{', '<tag>')
        self.data = self.data.replace('}', '</tag>')

        print(self.data)
        

if __name__ == "__main__":

    string = 'Some data which I use to show'
    my_xml = XMLData(string)
    my_xml.show_xml()
    convertator = Adapter(my_xml.data)
    convertator.convert_to_json()
    convertator.convert_to_XML()






    # def convert_to_xml(self):
    #     xml.replace('<tag>', '{')
    #     xml.replace('</tag>', '}')
    #
    #     return self.show_xml()




