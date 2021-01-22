from human import Human


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
        return self.show_inform()
