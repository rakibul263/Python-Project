class Classroom:
    def __init__(self,name):
        self.name = name
        self.student = []
        self.subject = []
    
    def add_student(self, student):
        roll_no = f'{self.name} - {len(self.student)+1}'
        student.id = roll_no
        self.students.append(student)
        
    def add_subject(self, subject):
        self.subject.append(subject)
    
    def take_semester_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.student)
        for student in self.students:
            student.calculate_final_grade()
