class Person:
    def __init__(self, name, age, designation,gender):
        self.name = name
        self.age = age
        self.designation = designation
        self.gender = gender
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old.")
        print(f"My designation is: {self.designation}")
        print(f"Gender :{self.gender}")


class Student(Person):
    def __init__(self, name, age, designation,gender, student_id):
        super().__init__(name, age, designation,gender)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age, designation,gender, subject):
        super().__init__(name, age,designation, gender)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

# Creating objects
student1 = Student("Shyam", 20, "Student","male", "S001")
teacher1 = Teacher("Mr. Ghalley", 35, "HOD","male", "Mathematics")

# Example usage
student1.introduce()  
student1.study()      

teacher1.introduce()  
teacher1.teach()     