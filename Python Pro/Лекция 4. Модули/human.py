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
