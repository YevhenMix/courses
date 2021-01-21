class Group:

    def __init__(self, *args):
        self.group_lst = [i for i in args]
        self.for_str = [(i.last_name, i.first_name, i.patronymic) for i in args]

    def add_to_group(self, student):
        self.group_lst.append(student)
        self.for_str.append((student.last_name, student.first_name, student.patronymic))

    def delete_from_group(self, student):
        index = self.group_lst.index(student)
        del self.group_lst[index]
        del self.for_str[index]

    def inform_about(self, last_name):
        for student in self.group_lst:
            if student.last_name == last_name:
                return str(student)
        else:
            return 'Такого студента нет!'

    def __str__(self):
        return str(self.for_str)
