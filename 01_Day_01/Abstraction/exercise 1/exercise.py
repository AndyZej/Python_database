import random
from enum import Enum


class Command(Enum):
    BUY = "buy"
    SELL = "sell"
    WAIT = "wait"


class CommandPrompt:
    def __init__(self, buy: list[str], sell: list[str], wait: list[str]):
        self.buy = buy
        self.sell = sell
        self.wait = wait

    def ask(self) -> Command:
        while True:
            choice = input('Decision [b/s/w/buy/sell/wait]: ')
            if choice in self.buy:
                return Command.BUY

            if choice in self.sell:
                return Command.SELL

            if choice in self.wait:
                return Command.WAIT

            print(f"Invalid choice: {choice}")

class Wallet:
    def __init__(self, zloty: float, usd: float):
        self.zloty = zloty
        self.usd = usd

    def convert_pln_to_usd(self, usdpln_rate):
        self.usd += self.zloty / usdpln_rate
        self.zloty = 0

    def convert_usd_to_pln(self, usdpln_rate):
        self.zloty += self.usd * usdpln_rate
        self.usd = 0


random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))

cp = CommandPrompt(['b', 'buy'], ['s', 'sell'], ['w', 'wait', ''])

def main(usdpln_rates):
    wallet_pln = 100.0
    wallet_usd = 0.0
    wallet = Wallet(zloty=wallet_pln, usd=wallet_usd)

    for usdpln_rate in usdpln_rates:
        print(f'Balance: {round(wallet.zloty, 2)} PLN, ${round(wallet.usd, 2)}, rate {usdpln_rate}')
        choice = cp.ask()

        if choice == Command.BUY:
            wallet.convert_pln_to_usd(usdpln_rate)

        elif choice == Command.SELL:
            wallet.convert_usd_to_pln(usdpln_rate)

    wallet.convert_usd_to_pln(usdpln_rate)
    print(f'Your result: {wallet.zloty} PLN!')


if __name__ == '__main__':
    main(random_usdpln_rates)