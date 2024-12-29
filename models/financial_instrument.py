class FinancialInstrument:
    def __init__(self, symbol, quantity, price):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price

    def get_symbol(self):
        return self.symbol

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_price(self, price):
        self.price = price

    def calculate_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Sembol: {self.symbol}, Miktar: {self.quantity}, Fiyat: {self.price}"