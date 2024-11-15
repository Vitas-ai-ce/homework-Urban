# днамическая типизация
name = "Виталий"
print(name, type(name))
age = 36
print(age, type(age))
age = 36 + 1
print(age)
is_student = 36 == 37 - 1
print(is_student, type(is_student))

# Переменные
number_of_complete_hw = '12'
number_of_hours_spent = '1.5'
course_name = 'Python'
time_for_one_task = 1.5 / 12
print(time_for_one_task)
time_for_one_task = '0.125'
print('Курс: ' + course_name ,', всего задач: '+ number_of_complete_hw ,', затрачено часов:'+ number_of_hours_spent ,', среднее_время_выполнения: '+time_for_one_task +' часа')

# Практическое задание по уроку "Строки и индексация строк"
example = 'Топинамбур'
print(example, type(example))
print(example[0])
print(example[-1])
print(example[5:])
print(example[::-1])
print(example[1:10:2])  # первый и второй индексозначает начало и конец среза, третий индекс означает шаг пропуска элемента строки
