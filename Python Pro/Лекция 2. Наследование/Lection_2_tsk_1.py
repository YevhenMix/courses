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
        return f'Full Name: {self.last_name} {self.first_name} {self.patronymic}\nGender: {self.gender}\nAge: {self.age}\nHeight: {self.height} cm\nWeight: {self.weight} kg'
