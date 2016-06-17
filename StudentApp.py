import json
from pprint import pprint
import sys


class Student:
    def __init__(self, StudentName, StudentPhoneNumber, StudentPercentage):
        self.StudentName=StudentName
        self.StudentPhoneNumber=StudentPhoneNumber
        self.StudentPercentage=StudentPercentage

    def __repr__(self):
       return ('Name : '+self.StudentName+' PhoneNumber : '+self.StudentPhoneNumber+' Percentage : '+self.StudentPercentage)


StudentList = []

def Add():
    Name = input("Enter Student's Name : ")
    PhoneNumber = input("Enter Student's PhoneNumber : ")
    Percentage = input("Enter Student's Percentage : ")
    new_student=Student(Name,PhoneNumber,Percentage)
    StudentList.append(new_student)
    with open("StudentListFile.txt", 'a') as StudentListFile:
        for s in StudentList:
            StudentListFile.write(str(s) + '\n')

def Read():
    with open("StudentListFile.txt", 'r') as f:
        StudentList = [line.rstrip('\n') for line in f]
        print(StudentList)

def Delete():
    with open("StudentListFile.txt", 'r') as f:
        StudentList = [line.rstrip('\n') for line in f]
    del StudentList[int(input("Enter Index : "))-1]
    #Now WRITING Back
    with open("StudentListFile.txt", 'w') as StudentListFile:
        for s in StudentList:
            StudentListFile.write(str(s) + '\n')

while True:

    func=int(input("Choose Any Number : \n(1) Read\n(2) Add\n(3) Delete\n(4) Quit\n"))
    if func == 1:
        Read()
    elif func == 2:
        Add()
    elif func == 3:
        Delete()
    elif func == 4:
        break
    else:
        print("Your option doesn't make sense to me")