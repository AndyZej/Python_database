class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"added {num1} to {num2} got {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"multiplied {num1} by {num2} got {result}")
        return result

    def print_operations(self):
        for operation in self.history:
            print(operation)


c1 = Calculator()
print(c1.add(1, 2))
print(c1.add(1, 3))
print(c1.multiply(1, 2))
c1.print_operations()