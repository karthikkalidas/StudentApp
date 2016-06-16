import demjson
from pprint import pprint
import sys


class Student:
        def __init__(self):
                self.StudentName=input("Enter Student's Name : ")
                self.StudentPhoneNumber= input("Enter Student's PhoneNumber : ")
                self.StudentPercentage= input("Enter Student's Percentage : ")

        def Read(self):     
                print(self.StudentName)
                print(self.StudentPhoneNumber)
                print(self.StudentPercentage)

        
        def __repr__(self):
                return ('Name : '+self.StudentName+' PhoneNumber : '+self.StudentPhoneNumber+' Percentage : '+self.StudentPercentage)


StudentList = []


def Add():
        StudentList.append(Student())

def Delete():
    StudentList.pop(int(input("Enter Index : "))-1)

def Search():     
    Name=input("Enter the Name : ")
    for x in StudentList:
        if x.StudentName == Name:
            print(x.StudentName)
            print(x.StudentPhoneNumber)  
            print(x.StudentPercentage)

Add()
Search()




#Make a command line interface that asks me (teacher) what I want to do (add a student, remove a student, edit) and then calls the appropriate function



