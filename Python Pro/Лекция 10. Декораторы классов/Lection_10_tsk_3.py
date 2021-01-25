from random import randint


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z

    @staticmethod
    def get_sum_volume_both(first, second):
        return Box.volume(first) + Box.volume(second)

    def __str__(self):
        return f'Box (x = {self.x}; y = {self.y}; z = {self.z})'


box_1 = Box(randint(1, 20), randint(1, 20), randint(1, 20))
box_2 = Box(randint(1, 20), randint(1, 20), randint(1, 20))

print(box_1)
print(box_2)
print(Box.get_sum_volume_both(box_1, box_2))
print(box_1.get_sum_volume_both(box_1, box_2))
print(box_2.get_sum_volume_both(box_1, box_2))
