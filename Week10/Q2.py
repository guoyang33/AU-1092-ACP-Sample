import sys
import Person

class Student(Person.Person):
    def __init__(self, name, id, gender, height, weight, department):
        super().__init__(name, id, gender, height, weight)
        self.department = department

    def setDepartment(self, department):
        self.department = department

    def getDepartment(self):
        return self.department

    def showInfo(self):
        print('{0} {1} {2}'.format(self.name, self.id, self.department))

if __name__=='__main__':
    if len(sys.argv)>6:
        student1 = Student(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
        student1.showInfo()

        student1.setID(input('new student ID: '))
        student1.setName(input('new student Name: '))
        student1.setDepartment(input('new Department: '))
        student1.showInfo()