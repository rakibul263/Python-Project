class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teacher = {} #"subject":"teacher_object"
        self.classroom = {} #"eight":"classrooom_object"
    
    def add_classroom(self, classroom):
        self.classroom[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teacher[subject.name] = teacher

    def student_admission(self, student):
        classname = student.classroom.name
        self.classroom[classname].add_student(student)

    # def calculate_grade(marks):
    #     pass

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks < 70:
            return 'A-'
        elif 50 <= marks < 60:
            return 'B'
        elif 40 <= marks < 50:
            return 'C'
        elif 33 <= marks < 40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00, 
            'A': 4.00, 
            'A-': 3.50, 
            'B': 3.00, 
            'C': 2.00, 
            'D': 1.00, 
            'F': 0.00
            }
        return grade_map[grade]

    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return 'A+'
        elif 3.5 <= value < 4.5:
            return 'A'
        elif 3.0 <= value < 3.5:
            return 'A-'
        elif 2.5 <= value < 3.0:
            return 'B'
        elif 2.0 <= value < 2.5:
            return 'C'
        elif 1.0 <= value < 2.0:
            return 'D'
        else:
            return 'F'
        

    def __repr__(self):
        print('--------ALL CLASSROOMS--------')
        for key, value in self.classrooms.items():
            print(key)

        print('--------Students-------')
        eight = self.classrooms['eight']
        for student in eight.students:
            print(student.name)
        
        print('------subjects------')
        for subject in eight.subjects:
            print(subject.name, subject.teacher.name)

        print('----Student Exam Marks-------')
        for student in eight.students:
            for key, value in student.marks.items():
                print(student.name, key, value, student.subject_grade[key])
            print('----student end----')
        return ''
        