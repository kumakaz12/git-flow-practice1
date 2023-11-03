class Subject:
    def __init__(self, name, teacher_name):
        self.name = name  # Название предмета
        self.teacher_name = teacher_name  # Имя учителя
        self.grades = []  # Оценки по предмету

    def add_grade(self, grade):
        self.grades.append(grade)  # Добавление оценки

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0  # Средний балл

class Student:
    def __init__(self, name, class_name):
        self.name = name  # Имя ученика
        self.class_name = class_name  # Класс ученика
        self.subjects = {}  # Словарь предметов

    def add_subject(self, subject):
        self.subjects[subject.name] = subject  # Добавление предмета

    def add_grade(self, subject_name, grade):
        if subject_name in self.subjects:
            self.subjects[subject_name].add_grade(grade)  # Добавление оценки
        else:
            print(f"Subject {subject_name} is not found for student {self.name}")

    def get_average_grade(self):
        total = sum(subject.get_average_grade() for subject in self.subjects.values())
        return total / len(self.subjects) if self.subjects else 0  # Общий средний балл

class Diary:
    def __init__(self):
        self.students = []  # Список учеников

    def add_student(self, student):
        self.students.append(student)  # Добавление ученика в дневник

    def get_student_grades(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return {subject: subj.get_average_grade() for subject, subj in student.subjects.items()}
        return None  # Оценки ученика

# Пример использования модели
math = Subject("Mathematics", "Mr. Smith")
john = Student("John Doe", "10-A")
john.add_subject(math)
john.add_grade("Mathematics", 5)
john.add_grade("Mathematics", 4)

diary = Diary()
diary.add_student(john)

print(diary.get_student_grades("John Doe"))
