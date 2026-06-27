class Price23Vat:
    VAT_RATE = 0.23

    def __init__(self, pretax):
        self._pretax = pretax

    @property
    def pretax(self):
        return self._pretax

    @pretax.setter
    def pretax(self, value):
        self._pretax = value

    @property
    def tax(self):
        return self._pretax * self.VAT_RATE

    @tax.setter
    def tax(self, value):
        self._pretax = value / self.VAT_RATE

    @property
    def net(self):
        return self._pretax / (1 + self.VAT_RATE)

    @net.setter
    def net(self, value):
        self._pretax = value * (1 + self.VAT_RATE)