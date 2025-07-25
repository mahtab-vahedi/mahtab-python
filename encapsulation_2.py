class Company:
    def __init__(self):
        self._project='Bale'

class Employee(Company):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self._project='Rubika'

    def show(self):
        print(f'employee name {self.name}')
        print(f'working on project {self._project}')

e=Employee('mahtab')
e.show()
e._project='Digikala' 