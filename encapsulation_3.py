class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def show(self):
        self.__salary=500
        print(f'{self.name}s salary is {self.__salary}')
emp=Employee('mahtab',100)
emp.show()
emp.__salary=600
print(f'salary is {emp.__salary}')
print(f'salary is {emp._Employee__salary}')

# setter
# getter



