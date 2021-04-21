#Create a class called ‘Student’ which contains attributes about students.
class Student:
    def __init__(self, first_name, last_name, undergraduate_programme):
        self.first_name = first_name
        self.last_name = last_name
        self.undergraduate_programme = undergraduate_programme
    def info(self):
        print(self.last_name+self.first_name+"      "+self.undergraduate_programme)

#example of using this class
A = Student('Shuo', 'Cai', 'BMI')
A.info()
    
