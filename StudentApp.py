import demjson

class Student:
        def __init__(self,StudentName,StudentPhoneNumber,StudentPercentage):
                self.StudentName = StudentName
                self.StudentPhoneNumber = StudentPhoneNumber
                self.StudentPercentage =StudentPercentage

        def Read(self):     
                print(self.StudentName)
                print(self.StudentPhoneNumber)
                print(self.StudentPercentage)

Name=input("Enter Student's Name : ")
PhoneNumber= input("Enter Student's PhoneNumber : ")
Percentage= input("Enter Student's Percentage : ")

s1=Student(Name,PhoneNumber,Percentage)



s1.Read()
