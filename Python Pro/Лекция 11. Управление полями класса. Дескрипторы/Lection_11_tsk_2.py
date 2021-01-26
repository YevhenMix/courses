class OnlyInt:

    def __init__(self, value: int):
        self.chek_value(value)

    def chek_value(self, value):
        if type(value) is int:
            self.value = value
        else:
            raise AttributeError('set only int')

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.chek_value(value)


class Diary:

    math = OnlyInt(5)
    geo = OnlyInt(2)


vlad = Diary()

print(vlad.math)
print(vlad.geo)
vlad.math = 1
print(vlad.math)
vlad.geo = '2'
