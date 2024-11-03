#!/usr/bin/env python3
# Author ID: Roniel G. Pangan - 113061220

class Student:
    # Initialize the student object with name and student ID
    def __init__(self, name, number):
        self.name = name          # Store the name
        self.number = number      # Store the student ID
        self.courses = {}         # Initialize an empty dictionary for courses

    # Display student name and number
    def displayStudent(self):
        print('Student Name: ' + self.name)
        print('Student Number: ' + self.number)

    # Add a new course and grade to the student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade  # Add the course and grade to the dictionary

    # Calculate and display the grade point average (GPA)
    def displayGPA(self):
        if self.courses:  # Check if there are any courses
            gpa = sum(self.courses.values()) / len(self.courses)  # Calculate GPA
            print('GPA of student ' + self.name + ' is ' + str(gpa))
        else:
            print('No courses found for student ' + self.name)
