import demjson

class Student:
        def __init__(self,StudentName,StudentPhoneNumber,StudentPercentage):
                self.StudentName = StudentName
                self.StudentPhoneNumber = StudentPhoneNumber
                self.StudentPercentage =StudentPercentage

s1=Student()
s1.StudentName=input("Enter Student's Name : ")
s1.StudentPhoneNumber= input("Enter Student's PhoneNumber : ")
s1.StudentPercentage= input("Enter Student's Percentage : ")