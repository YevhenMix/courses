class ToManyPeople(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exc(self):
        return self.message


class Human:

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


class Student(Human):

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
        full_name = f'Full Name: {self.last_name} {self.first_name} {self.patronymic}\n'
        university = f'Speciality: {self.speciality}\nGroup: {self.group}\nCourse: {self.course}'
        all_info = full_name + university
        return all_info


class Group:

    def __init__(self, *args):
        self.group_lst = [i for i in args]
        self.for_str = [(i.last_name, i.first_name, i.patronymic) for i in args]

    def add_to_group(self, student):
        try:
            if len(self.group_lst) == 10:
                raise ToManyPeople('Вы добавили слишком много людей в группу максимум 10')
            else:
                self.group_lst.append(student)
                self.for_str.append((student.last_name, student.first_name, student.patronymic))
        except ToManyPeople as tm:
            print(tm.get_exc())

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


human1 = Student('Лихачёв', 'Бенедикт', 'Дамирович', 'male', 25, 185, 91, 'IT', 'RT-518', 'III')
human2 = Student('Шилов', 'Святослав', 'Якунович', 'male', 23, 160, 50, 'IT', 'RT-518', 'III')
human3 = Student('Самойлов', 'Иннокентий', 'Георгиевич', 'male', 24, 175, 65, 'IT', 'RT-518', 'III')
human4 = Student('Григорьев', 'Лука', 'Сергеевич', 'male', 26, 145, 82, 'IT', 'RT-518', 'III')
human5 = Student('Громов', 'Ибрагил', 'Артемович', 'male', 22, 192, 73, 'IT', 'RT-518', 'III')
human6 = Student('Хохлова', 'Илона', 'Лукьевна', 'female', 23, 134, 85, 'IT', 'RT-518', 'III')
human7 = Student('Силина', 'Элизабет', 'Альбертовна', 'female', 24, 154, 84, 'IT', 'RT-518', 'III')
human8 = Student('Рогова', 'Кира', 'Авксентьевна', 'female', 25, 132, 89, 'IT', 'RT-518', 'III')
human9 = Student('Щербакова', 'Неолина', 'Вячеславовна', 'female', 23, 164, 76, 'IT', 'RT-518', 'III')
human10 = Student('Лукина', 'Эвелина', 'Митрофановна', 'female', 24, 165, 59, 'IT', 'RT-518', 'III')

group_rt = Group(human1, human2, human3, human4, human5, human6, human7, human8, human9, human10)

human11 = Student('Суханова', 'Аделия', 'Игнатьевна', 'male', 25, 157, 49, 'IT', 'RT-518', 'III')

print(group_rt)
group_rt.add_to_group(human11)
print(group_rt)
group_rt.delete_from_group(human8)
print(group_rt)
print(group_rt.inform_about('Самойлов'))
print(group_rt.inform_about('Mix'))

group_rt.add_to_group(human11)
group_rt.add_to_group(human11)
group_rt.add_to_group(human11)
print(group_rt)
