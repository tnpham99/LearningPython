#Question: https://juejung.github.io/jdocs/Comp/html/Lecture_OOP/Homework/Homework_OOP.html

import math

class Student():
    def __init__(self, firstname, lastname, gender, status, gpa) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.status = status
        self.gpa = gpa

    def show_myself(self):
        print('First Name:', self.firstname, '\nLast Name:', self.lastname, '\nGender:', self.gender, '\nStatus:', self.status, '\nGPA:', self.gpa)
    
    def study(self, study_time):
        self.gpa = self.gpa + math.log(study_time)
        if self.gpa >= 4.0:
            self.gpa = 4.0
        return round(float(self.gpa),1)

student_info = [['Mike', 'Barnes', 'Male', 'Freshman', 4], ['Jim', 'Nickerson', 'Male', 'Sophomore', 3], ['Jack', 'Indabox', 'Male', 'Junior', 2], ['Jane', 'Miller', 'Female', 'Senior', 3.6], ['Mary', 'Scott', 'Female', 'Senior', 2.7]]
student_list = []
for student in student_info:
    student_list.append(Student(student[0], student[1], student[2], student[3], student[4]))

time_study = [60, 100, 4, 300, 1000]
for i in range(len(student_list)):
    student = student_list[i]
    student.show_myself()
    print('GPA after study:', student.study(time_study[i]))
    print('-'*20)