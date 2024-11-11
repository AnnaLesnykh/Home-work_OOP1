class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer (self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __lt__(self, other):
       if not isinstance(other, Student):
           print('Невозможно сравнить!')
       return self._average_rating < other._average_rating

    def _average_rating(self):  # средняя оценка
        grade = []
        for key, value in self.grades.items():
            for num in value:
                grade.append(num)
        average = sum(grade) / len(grade)
        return average


    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self._average_rating()}\n Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n Завершенные курсы: {','.join(self.finished_courses)}"


class Mentor:
    def __init__(self, name: object, surname: object) -> object:
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer (Mentor):
    grades = {}

    def rate_st(self, mentor, course, grade):
        if isinstance(mentor, Mentor) and course in self.courses_attached and course in Student.courses_in_progress:
            if course in mentor.grade:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else: 
            return 'Ошибка'

    def _average_rating(self):  # средняя оценка
        grade = []
        for key, value in self.grades.items():
            for num in value:
                grade.append(num)
        average = sum(grade) / len(grade)
        return average

    def __lt__(self, other):
       if not isinstance(other, Lecturer):
           print('Невозможно сравнить!')
       return self._average_rating < other._average_rating
    

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self._average_rating()}"

class Reviewer (Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}"

Student1 = Student("Иван", "Петров", "м")
Student2 = Student("Мария", "Крылова", "ж")
Student1.courses_in_progress = ["Python", "Git"]
Student1.finished_courses = ["Java"]
Student2.courses_in_progress = ["Java", "Git"]
Student2.finished_courses = ["Python", "1C"]
Student1.grades ={"Python": [10, 3, 7, 5, 9], "Git": [3, 8, 10, 6], "Java": [9, 8, 3, 2, 6, 7, 10]}
Student2.grades ={"Python": [2, 8, 4, 10, 5, 9], "Git": [3, 6, 8], "Java": [5, 8, 9, 6], "1C": [10, 8, 5, 7, 6, 8]}

Lecturer1 = Lecturer("Александр", "Новиков")
Lecturer2 = Lecturer("Олег", "Шатский")
Lecturer1.courses_attached = ["Python", "Java"]
Lecturer2.courses_attached = ["Git", "Python", "1C"]
Lecturer1.grades = {"Python": [10, 9, 8, 10, 6], "Java": [5, 3, 8, 9]}
Lecturer2.grades = {"Python": [9, 8, 10, 6], "Git": [10, 10, 9], "1C": [9, 8, 7, 9, 10]}

Reviewer1 = Reviewer("Алексей", "Смыслов")
Reviewer2 = Reviewer("Петр", "Красин")


 
