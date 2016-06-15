import demjson

class Student:
        def __init__(self,StudentName,StudentPhoneNumber,StudentPercentage):
                self.StudentName = StudentName
                self.StudentPhoneNumber = StudentPhoneNumber
                self.StudentPercentage =StudentPercentage

Name=input("Enter Student's Name : ")
PhoneNumber= input("Enter Student's PhoneNumber : ")
Percentage= input("Enter Student's Percentage : ")
s1=Student(Name,PhoneNumber,Percentage)

def Read():     
                print(s1.StudentName)
                print(s1.StudentPhoneNumber)
                print(s1.StudentPercentage)

Read()
