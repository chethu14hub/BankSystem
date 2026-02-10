class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def marks(self,m1,m2,m3,m4,m5,m6):
        grade=(m1+m2+m3+m4+m5+m6)/6
        if grade>=80:
            print("First Class")
        elif grade<80 and grade>=50:
            print("Second Class")
        elif grade<50 and grade>=35:   
            print("Third Class")
std=Student("John",123)
std.marks(20,30,40,50,60,70)


    