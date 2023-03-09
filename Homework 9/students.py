class Student:
    def __init__(self, name = str('ivan'), age = int(18), groupNumber = str('10A')):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def getAll(self):
        return self.name, self.age, self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

def main():
    student_1 = Student()
    student_2 = Student('dima', 21, '11A')
    student_3 = Student('misha', 22, '10B')
    student_4 = Student('vasya', 23, '12C')
    student_5 = Student('oleg', 20, '13D')

    print(student_1.getAll(), student_2.getAll(), student_3.getAll(), student_4.getAll(),student_5.getAll())

if __name__ == '__main__':
    main()



