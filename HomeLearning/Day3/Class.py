class Human():
    def __init__(self, name, ssn) -> None:
        self.name = name
        self.__ssn = ssn #private attribute
        self.is_sleeping = False

    def go_to_sleep(self):
        print('Sleep')
        self.is_sleeping = False

    def get_ssn_lastdigit(self):
        return self.__ssn[-1]
        
class Teacher(Human):
    def __init__(self, name, ssn, department, is_in_break=False):
        super().__init__(name, ssn)
        self.department = department
        self.is_in_break = is_in_break
    
    def __str__(self):
        return 'Name: %s, Department: %s, Is in break: %s' % (self.name, self.department, self.is_in_break)

    def __go_home(self): #private method
        print('Go home')

    def finish_teaching(self):
        print('Get out of school')
        self.__go_home()

class Student(Human):
    def __init__(self, name, ssn, id) -> None:
        super().__init__(name, ssn)
        self.id = id

    def study(self):
        print('Study')

        
class PublicSchool():
    category = 'Public'
    def __init__(self, name, prin, size, num_class, teachers):
        self.name = name
        self.principal = prin
        self.size = size
        self.num_class = num_class
        self.num_students_per_class = size/num_class
        self.teachers = teachers
    
    def take_break(self):
        self.size = 0
        for teacher in self.teachers:
            teacher.is_in_break = True
        
    def start_school(self,new_size):
        self.size = new_size
        for teacher in self.teachers:
            teacher.is_in_break = False

a = Student('Sarah','890','579437')
b = Student('Joseph','789','456466')
c = Teacher('Kelly','123','Biology')
d = Teacher('mno','369','Math')

# lhp = PublicSchool('Le Hong Phong','vo giam doc so',3000,100,[c,b])
# nd = PublicSchool('Nguyen Du','abc',200,10,[c,d])

# lhp.take_break()
# for teacher in lhp.teachers:
#     print(teacher)

# lhp.teachers[0].name = 'John'
# print(nd.teachers[0])

# print(lhp.teachers[0].get_ssn_lastdigit())

print(a.name)
e = Human('Hung','8978786')
print(isinstance(a,Human))