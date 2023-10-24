class Students:
    def __init__(self,name ,course,gender,age):
        self.name = name
        self.course = course
        self.gender = gender
        self. age = age

    def display(self):
        print("Name: %s \nCourse: %s\nGender: %s\nAge:%d" % (self.name,self.course,self.gender,self.age))

myobj = Students("Bruno","IT","male",22 )
myobj.display()