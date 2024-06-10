# here we access class members 
class Employee :
   def __init__(self,sal,age):
        self.salary = sal
        self.age = age 


   def display(self):
       print(f'salary is {self.salary} and age is {self.age}')


e1 = Employee(24000,21)
e2 = Employee(26000,26)

# here we accesing the mathod and attribute 
print(e1.salary)

# here printing age of e2
print(e2.age)