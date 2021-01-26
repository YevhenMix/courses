from datetime import datetime
from time import sleep


class Button:

    def __init__(self, file_name, active=0):
        self.__active = active
        self.file_name = file_name

    def get_state(self):
        return self.__active

    def set_state(self, value):
        self.__active = value
        with open(f'{self.file_name}.txt', 'a') as file:
            text = f'{datetime.now()} -> {self.active}\n'
            file.writelines(text)

    active = property(get_state, set_state)

    def __str__(self):
        return f'State: {self.active}'


big_red_button = Button('BRB', 0)
reactor = Button('Stop', 1)

for i in range(1, 10):
    print(big_red_button)
    big_red_button.active = i
    sleep(1)

for i in range(15):
    print(reactor)
    reactor.active = i
    sleep(1)
