class ToManyPeople(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exc(self):
        return self.message


class Group:

    def __init__(self, *args):
        try:
            if len(args) > 10:
                self.group_lst = [args[i] for i in range(10)]
                raise ToManyPeople('Вы создаете группу больше необходимого максимум 10. Создан список из первых 10')
            else:
                self.group_lst = [i for i in args]
        except ToManyPeople as tm:
            print(tm.get_exc())

    def add_to_group(self, student):
        try:
            if len(self.group_lst) >= 10:
                raise ToManyPeople('Вы добавили слишком много людей в группу максимум 10')
            else:
                self.group_lst.append(student)
        except ToManyPeople as tm:
            print(tm.get_exc())

    def delete_from_group(self, student):
        index = self.group_lst.index(student)
        del self.group_lst[index]

    def find_student(self, last_name):
        for student in self.group_lst:
            if student.last_name == last_name:
                return str(student)
        else:
            return 'Такого студента нет!'

    def show_group(self):
        for num, student in enumerate(self.group_lst):
            print(f'{num+1}. {student.last_name} {student.first_name} {student.patronymic}')

    def __str__(self):
        self.show_group()
        return ''
