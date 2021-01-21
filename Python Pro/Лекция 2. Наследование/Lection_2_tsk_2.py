class Student(Human):

    def __init__(self, last_name, first_name, patronymic, gender, age, height, weight, speciality, group, course):
        super().__init__(last_name, first_name, patronymic, gender, age, height, weight)
        self.speciality = speciality
        self.group = group
        self.course = course

    def show_inform(self):
        return f'Full Name: {self.last_name} {self.first_name} {self.patronymic}\nSpeciality: {self.speciality}\nGroup: {self.group}\nCourse: {self.course}'

    def __str__(self):
        return f'Full Name: {self.last_name} {self.first_name} {self.patronymic}\nSpeciality: {self.speciality}\nGroup: {self.group}\nCourse: {self.course}'

