from School import School
from Person import Teacher, Student
from Subject import Subject
from Classroom import Classroom


eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

School.add_classroom("Eight")
School.add_classroom("Nine")
School.add_classroom("Ten")

abul = Student('Abul Khan', eight)
babul = Student('Babul Khan', nine)
cabul = Student('Cabul Khan', eight)

School.student_admission(abul)
School.student_admission(babul)
School.student_admission(cabul)

physics_teacher = Teacher('Shahjahan Tapon Rana')
chemistry_teacher = Teacher('Haradon Nag')
biology_teacher = Teacher('Azmal Sir')

physics = Subject('physics', physics_teacher)
chemistry = Subject('chemistry', chemistry_teacher)
biology = Subject('biology', biology_teacher)

eight.add_subject(physics)
eight.add_subject(chemistry)
eight.add_subject(biology)

eight.take_semester_final_exam()

print(School)


