from student import Student  # Import the Student class

# Create instances of the Student class
student1 = Student('John', '013454900')
student2 = Student('Jessica', '023384103')

# Displaying student information
student1.displayStudent()
student2.displayStudent()

# Adding grades for student1
student1.addGrade('uli101', 4.0)
student1.addGrade('ops245', 3.5)

# Adding grades for student2
student2.addGrade('ipc144', 4.0)

# Displaying GPA for both students
student1.displayGPA()
student2.displayGPA()

# Modifying student1's name
print(student1.name)  # Print original name
student1.name = 'Jack'  # Change name
print(student1.name)  # Print new name
