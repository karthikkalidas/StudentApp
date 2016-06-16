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

while True:
    func=input("Choose Any Number : \n(1) Read\n(2) Add\n(3) Delete\n(4) Search\n(5) Quit")
    if func==1
        Read()
    elif func==2
        Add()
    elif func==3
        Delete()
    elif func==4
        Search()
    elif func==5
        break



