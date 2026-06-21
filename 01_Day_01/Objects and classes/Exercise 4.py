class Employee:
    def __init__(self, id: int, first_name: str, last_name: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.__salary = 0

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary: int | float) -> None:
        if not (isinstance(salary, int) or isinstance(salary, float)):
            raise TypeError("Salary must be a float")

        if salary < 0:
            raise ValueError("Salary must be positive")

        self.__salary = salary



employee1 = Employee(1, "Adam", "Npvak")
print(employee1.salary)
employee1.salary = 100
print(employee1.salary)