from student import Student
from group import Group

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

print(group_rt)
group_rt.add_to_group(student11)
group_rt.delete_from_group(student8)
print(group_rt.find_student('Самойлов'))
print(group_rt.find_student('Mix'))

group_rt.add_to_group(student11)
group_rt.add_to_group(student11)
group_rt.add_to_group(student11)
print(group_rt)
