# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???
name_count = {}
for student in students:
    name = student['first_name']
    name_count[name] = name_count.get(name, 0) + 1

for name, count in name_count.items():
    print(f'{name}: {count}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
names = [student['first_name'] for student in students]
print(max([student['first_name'] for student in students], key=names.count))

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
i = 0
for s_class in school_students:
  names = [student['first_name'] for student in s_class]
  i+=1
  print(f'{i} класс ' + max([student['first_name'] for student in s_class], key=names.count))

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
for s_class in school:
  boys_count = sum(1 for student in s_class['students'] if is_male.get(student['first_name']))
  girls_count = sum(1 for student in s_class['students'] if not is_male.get(student['first_name']))
  print(f"класс {s_class['class']}: мальчиков - {boys_count}, девочек - {girls_count}")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
for s_class in school:
  max_boys = 0
  max_girls = 0
  boys_count = sum(1 for student in s_class['students'] if is_male.get(student['first_name']))
  girls_count = sum(1 for student in s_class['students'] if not is_male.get(student['first_name']))
  max_boys = max(boys_count, max_boys)
  max_girls = max(girls_count, max_girls)
  if max_boys:
    print(f"Больше всего мальчиков в классе {s_class['class']}")
  if max_girls:
    print(f"Больше всего девочек в классе {s_class['class']}")
  