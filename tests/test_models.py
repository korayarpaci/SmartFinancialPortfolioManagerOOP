import unittest
from models.portfolio import Portfolio
from models.financial_instrument import FinancialInstrument

class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio("Test Portföy")
        self.investment1 = FinancialInstrument("Hisse Senedi", 100, 150)
        self.investment2 = FinancialInstrument("Tahvil", 200, 90)

    def test_add_investment(self):
        self.portfolio.add_investment(self.investment1)
        self.assertEqual(len(self.portfolio.investments), 1)
        self.assertEqual(self.portfolio.investments[0], self.investment1)

    def test_get_total_value(self):
        self.portfolio.add_investment(self.investment1)
        self.portfolio.add_investment(self.investment2)
        self.assertEqual(self.portfolio.get_total_value(), 10500)

    def test_get_investment_names(self):
        self.portfolio.add_investment(self.investment1)
        self.portfolio.add_investment(self.investment2)
        self.assertEqual(self.portfolio.get_investment_names(), ["Hisse Senedi", "Tahvil"])

if __name__ == "__main__":
    unittest.main()