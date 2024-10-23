from Person import Teacher
from School import School
class Subject :
    def __init__(self, name, teacher) :
        self.name = name
        self.teacher = teacher
        self.max_number = 100
        self.pass_mark = 33

    def exam (self, students):
        for student in students:
            mark = self.teacher.evalute_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)