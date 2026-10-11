from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Base example
# class Student(BaseModel):
#     name: str

# new_student = {"name":"Abhishek"}


#Defalut values
class Student(BaseModel):
    name: str = 'abhishek'
    age: Optional[int] = None
    email: EmailStr #Pydantic has built-in email validator 
    cgpa: float = Field(gt=0, lt=10, default=8, description = 'A decimal value representing the CGPA of a student') 
    # All the use cases of field function are mention in CGPA and we can also add regex expressions

new_student = {'age': '32', 'email': 'abs@gmail.com','cgpa': 5} 
#Python can automatically convert string to int. In python, it is called type coercion

student = Student(**new_student)


print(student) 

print(student.name)
print(student.age)

print(type(student)) # It is a pydantic object
# We can also convert pydantic object into python dict and json

#student_dict = dict(student) # Explicit conversion of student into dictionary
student_dict = student.model_dump()


print(student_dict)
print(student_dict['age'])
print(type(student_dict))



student_json = student.model_dump_json()
print(student_json)