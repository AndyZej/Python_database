class BankAccount:
    def __init__(self, number: int):
        self.__number = number
        self.__cash: float = 0.0

    def get_number(self) -> int:
        return self.__number

    def deposit_cash(self, amount: float):
        if amount < 0:
            raise ValueError("Negative amounts")

        self.__cash += amount


    def withdraw_cash(self, amount: float) -> float:
        if amount > self.__cash:
            output = self.__cash
            self.__cash = 0
            return output

        self.__cash -= amount
        return amount

    def print_info(self):
        print(f"account: {self.__number} Cash: {self.__cash}")


a = BankAccount(10)
a.deposit_cash(100)
print(a.get_number())