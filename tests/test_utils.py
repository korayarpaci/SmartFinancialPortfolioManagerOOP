import unittest
from utils.data_handler import DataHandler
from utils.risk_analysis import RiskAnalysis
from models.portfolio import Portfolio
from models.financial_instrument import FinancialInstrument

class TestDataHandler(unittest.TestCase):

    def setUp(self):
        self.data_handler = DataHandler("test_data.csv")
        self.data = [["Hisse Senedi", 100, 150], ["Tahvil", 200, 90]]

    def test_read_csv(self):
        # CSV dosyasını okumayı test eder
        self.data_handler.write_csv(self.data)
        read_data = self.data_handler.read_csv()
        self.assertEqual(read_data, self.data)

    def test_write_csv(self):
        # CSV dosyasına yazma işlemini test eder
        self.data_handler.write_csv(self.data)
        with open("test_data.csv", mode='r') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 2)

class TestRiskAnalysis(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio("Test Portföy")
        self.investment1 = FinancialInstrument("Hisse Senedi", 100, 150)
        self.investment2 = FinancialInstrument("Tahvil", 200, 90)
        self.portfolio.add_investment(self.investment1)
        self.portfolio.add_investment(self.investment2)
        self.risk_analysis = RiskAnalysis(self.portfolio)

    def test_calculate_risk(self):
        risk = self.risk_analysis.calculate_risk()
        self.assertEqual(risk, 525)

    def test_assess_portfolio_risk(self):
        risk_level = self.risk_analysis.assess_portfolio_risk()
        self.assertEqual(risk_level, "Orta Risk")

if __name__ == "__main__":
    unittest.main()