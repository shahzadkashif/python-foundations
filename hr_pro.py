from datetime import date
employee = []
managers = []
class Employee:
    def __init__(self, name, age, salary, hiredate):
        self.name = name
        self.age = age
        self.salary = salary
        self.hiredate = hiredate
        
        
    def total_years(self):
        today = date.today
        return date.today().year - self.hiredate
    
    def __str__(self):
        return "Name: {}, Age: {}, Salary: {}, working years: {}".format(self.name, self.age, self.salary, self.total_years())
    
    
class Manager(Employee):
    def __init__(self,name, age, salary, hiredate, bonus):
        super().__init__(name,age,salary,hiredate)
        self.bonus = bonus
        
    def get_bonus(self):
        return self.salary * self.bonus
    
    
    def __str__(self):
        return "Name:{}, age:{}, salary:{}, Working Years:{}, bonus: {}".format(self.name, self.age, self.salary, self.total_years(),self.get_bonus())
    
    
menu = ["Show Employees", "Show Managers", "Add an Employee","Add a Manager", "Exit"]
print("Welcome to HR Pro 2019")

counter = 0

while counter == 0:
    print("Options:")
    for i in menu:
        print(f"{menu.index(i) +1}. {i}")

    user_input = int(input("What would you like to do?  "))

    if user_input == 1:
        for facts in employee:
            print(facts)

    elif user_input == 2:
        for facts in managers:
            print(facts)

    elif user_input == 3:
        name = input("Name: ")
        age = int(input("Age: "))
        salary = int(input("Salary: "))
        hiredate = int(input("Employment year: "))
        employee.append(Employee(name, age, salary, hiredate))
        print("Employee added successfully")

    elif user_input == 4:
        name = input("Name: ")
        age = int(input("Age: "))
        salary = int(input("Salary: "))
        hiredate = int(input("Employment year: "))
        bonus = float(input("Bonus Percentge: "))

        managers.append(Manager(name, age, salary, hiredate, bonus))
        print("Manager added successfully")

    elif user_input == 5:
        counter = 1


