import demjson

class Student:
        def __init__(self,StudentName,StudentPhoneNumber,StudentPercentage):
                self.StudentName = StudentName
                self.StudentPhoneNumber = StudentPhoneNumber
                self.StudentPercentage =StudentPercentage

                def Read(self):     
                    print(StudentName)
                    print(StudentPhoneNumber)
                    print(StudentPercentage)

                def  Add():
                    StudentName= input("Enter Student's Name : ")
                    StudentPhoneNumber= input("Enter Student's PhoneNumber : ")
                    StudentPercentage= input("Enter Student's Percentage : ")
                    jsonStudentName = demjson.encode(StudentName)
                    print(jsonStudentName)
                    jsonStudentPhoneNumber = demjson.encode(StudentPhoneNumber)
                    print(jsonStudentPhoneNumber)
                    jsonStudentPercentage = demjson.encode(StudentPercentage)
                    print(jsonStudentPercentage)
                    return

                Add()
