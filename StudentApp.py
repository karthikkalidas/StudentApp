import json
from pprint import pprint
import sys
import os


class Student:
    def __init__(self, Name, PhoneNumber, Marks1, Marks2, Marks3):
        self.Name=Name
        self.PhoneNumber=PhoneNumber
        self.Marks1=Marks1
        self.Marks2=Marks2
        self.Marks3=Marks3

    def __repr__(self):
       return (self.Name+' '+self.PhoneNumber+' '+self.Marks1+' '+self.Marks2+' '+self.Marks3)


StudentList = []

def Add():
    sName = input("Enter Student's Name : ")
    sPhoneNumber = input("Enter Student's PhoneNumber : ")
    sMarks1 = input("Enter Marks1 : ")
    sMarks2 = input("Enter Marks2 : ")
    sMarks3 = input("Enter Marks3 : ")
    new_student=Student(sName,sPhoneNumber,sMarks1,sMarks2,sMarks3)
    StudentList.append(new_student)
    with open("StudentListFile.txt", 'a') as StudentListFile:
        for s in StudentList:
            StudentListFile.write(str(s) + '\n')

def Read():
    with open("StudentListFile.txt", 'r') as f:
        StudentList = [line.rstrip('\n') for line in f]
        print(StudentList)

def Edit(): 
    sindex =int(input("Enter Index : "))-1
    sName = input("Enter Student's Name : ")
    sPhoneNumber = input("Enter Student's PhoneNumber : ")
    sMarks1 = input("Enter Marks1 : ")
    sMarks2 = input("Enter Marks2 : ")
    sMarks3 = input("Enter Marks3 : ")
    # read a list of lines into data
    with open('StudentListFile.txt', 'r') as file:
        data = file.readlines()
    data[sindex] = sName+' '+sPhoneNumber+' '+sMarks1+' '+sMarks2+' '+sMarks3+'\n'
    # and write everything back
    with open('StudentListFile.txt', 'w') as file:
        file.writelines( data )

while True:
    os.system('clear')
    func=int(input("Choose Any Number : \n(1) Read\n(2) Add\n(3) Edit\n(4) Quit\n"))
    os.system('clear')
    if func == 1:
        Read()
    elif func == 2:
        Add()
    elif func == 3:
        Edit()
    elif func == 4:
        quit()
    else:
        print("Your option doesn't make sense to me")

    input("\nPress any key to continue : ")