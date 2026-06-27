class Price23Vat:
    VAT_RATE = 0.23

    def __init__(self, value):
        self._pretax = value
        self._net = value / (1 + self.VAT_RATE)
        self._tax = value - self._net

    # ----- getters -----
    def get_pretax(self):
        return self._pretax

    def get_net(self):
        return self._net

    def get_tax(self):
        return self._tax

    # ----- setters -----
    def set_pretax(self, value):
        self._pretax = value
        self._net = value / (1 + self.VAT_RATE)
        self._tax = value - self._net

    def set_net(self, value):
        self._net = value
        self._pretax = value * (1 + self.VAT_RATE)
        self._tax = self._pretax - self._net

    def set_tax(self, value):
        self._tax = value
        self._pretax = value / self.VAT_RATE
        self._net = self._pretax - self._tax