class OS:
    def show_change(self, change):
        raise NotImplementedError

class IOS(OS):
    def say_what_new(self, change):
        print(f'В новой версии IOS есть изменения: {change}')

class Android(OS):
    def say_what_new(self, change):
        print(f'В новой версии Android есть изменения: {change}')


class PresentationBase:
    def __init__(self):
        self._os = self.get_os()

    def get_os(self):
        raise NotImplementedError

    def compare_versions(self, change):
        self._os.say_what_new(change)


class PresenttationOfAndroid(PresentationBase):
    def __init__(self):
        # super(PresenttationOfAndroid, self).__init__()
        super().__init__()
        self._memory = []

    def get_os(self):
        return Android()

    def compare_versions(self, change):
        # super(PresenttationOfAndroid, self).compare_versions(change)
        super().compare_versions(change)
        self._memory.append(change)


    def say_total(self):
        print(f"\n За все время реализованно:  {', '.join(self._memory)}")


if __name__ == '__main__':
    presentation = PresenttationOfAndroid()
    presentation.compare_versions('Добавили виджеты')
    print('-'*12, 'на следующей презентации','-'*12)
    presentation.compare_versions('Добавили всплывающие окна')
    presentation.say_total()
