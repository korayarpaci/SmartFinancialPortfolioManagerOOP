class RiskAnalysis:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def calculate_risk(self):
        total_value = self.portfolio.get_total_value()
        risk_factor = total_value * 0.05  # Örnek Risk !!
        return risk_factor

    def assess_portfolio_risk(self):
        risk = self.calculate_risk()
        if risk > 10000:
            return "Yüksek Risk"
        elif risk > 5000:
            return "Orta Risk"
        else:
            return "Düşük Risk"