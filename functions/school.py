class TooManyStudents(Exception):
    pass


class ClassRoom:
    def __init__(self, teacher: str, students:list, course_title:str):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title

    def add_student(self, student):
        if len(self.students) <= 10:
            return self.students.append(student)
        else:
            raise TooManyStudents
        
    

    def remove_student(self, name):
        for student in self.students:
            if student == name:
                self.students.remove(student)
                break

    def add_teacher(self, new_teacher):
        self.teacher = new_teacher
        return self.teacher
    

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    pass

class Student(Person):
    pass