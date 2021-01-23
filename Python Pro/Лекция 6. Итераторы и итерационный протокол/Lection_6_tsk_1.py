"""1) Дополните класс Группа (задание Лекции 2) возможностью поддержки итерационного протокола. """


class Human:        # Оставлен для проверки группы

    def __init__(self, last_name, first_name, patronymic, gender, age, height, weight):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight

    def show_inform(self):
        full_name = f'Full Name: {self.last_name} {self.first_name} {self.patronymic}\n'
        gender_age = f'Gender: {self.gender}\nAge: {self.age}\n'
        height_weight = f'Height: {self.height} cm\nWeight: {self.weight} kg'
        all_info = full_name + gender_age + height_weight
        return all_info


class Student(Human):       # Оставлен для проверки группы

    def __init__(self, last_name, first_name, patronymic, gender, age, height, weight, speciality, group, course):
        super().__init__(last_name, first_name, patronymic, gender, age, height, weight)
        self.speciality = speciality
        self.group = group
        self.course = course

    def show_inform(self):
        full_name = f'Full Name: {self.last_name} {self.first_name} {self.patronymic}\n'
        university = f'Speciality: {self.speciality}\nGroup: {self.group}\nCourse: {self.course}'
        all_info = full_name + university
        return all_info

    def __str__(self):
        return self.show_inform()


class ToManyPeople(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exc(self):
        return self.message


class GroupIterator:

    def __init__(self, wrap):
        self.wrap = wrap
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.wrap):
            self.index += 1
            return self.wrap[self.index-1]
        else:
            raise StopIteration


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

    def __iter__(self):
        return GroupIterator(self.group_lst)

    def __str__(self):
        self.show_group()
        return ''


student1 = Student('Лихачёв', 'Бенедикт', 'Дамирович', 'male', 25, 185, 91, 'IT', 'RT-518', 'III')
student2 = Student('Шилов', 'Святослав', 'Якунович', 'male', 23, 160, 50, 'IT', 'RT-518', 'III')
student3 = Student('Самойлов', 'Иннокентий', 'Георгиевич', 'male', 24, 175, 65, 'IT', 'RT-518', 'III')
student4 = Student('Григорьев', 'Лука', 'Сергеевич', 'male', 26, 145, 82, 'IT', 'RT-518', 'III')
student5 = Student('Громов', 'Ибрагил', 'Артемович', 'male', 22, 192, 73, 'IT', 'RT-518', 'III')
student6 = Student('Хохлова', 'Илона', 'Лукьевна', 'female', 23, 134, 85, 'IT', 'RT-518', 'III')
student7 = Student('Силина', 'Элизабет', 'Альбертовна', 'female', 24, 154, 84, 'IT', 'RT-518', 'III')
student8 = Student('Рогова', 'Кира', 'Авксентьевна', 'female', 25, 132, 89, 'IT', 'RT-518', 'III')
student9 = Student('Щербакова', 'Неолина', 'Вячеславовна', 'female', 23, 164, 76, 'IT', 'RT-518', 'III')
student10 = Student('Лукина', 'Эвелина', 'Митрофановна', 'female', 24, 165, 59, 'IT', 'RT-518', 'III')
student11 = Student('Суханова', 'Аделия', 'Игнатьевна', 'male', 25, 157, 49, 'IT', 'RT-518', 'III')

group_rt = Group(student1, student2, student3, student4, student5, student6, student7, student8, student9, student10)

students = iter(group_rt)

for stud in students:
    print(stud)
