class Portfolio:
    def __init__(self, user):
        """
        Kullanıcıya ait portföyü oluşturur.

        Args:
        - user (User): Kullanıcı nesnesi.
        """
        self.user = user
        self.instruments = []  # Finansal enstrümanları saklamak için liste

    def add_instrument(self, symbol, quantity, price):
        """
        Portföye yeni bir finansal enstrüman ekler.

        Args:
        - symbol (str): Enstrümanın sembolü (ör. AAPL, BTC).
        - quantity (float): Enstrümanın miktarı.
        - price (float): Enstrümanın birim başına fiyatı.
        """
        instrument = {
            "Sembol": symbol,
            "Miktar": quantity,
            "Fiyat": price
        }
        self.instruments.append(instrument)

    def view_portfolio(self):
        """
        Portföydeki tüm finansal enstrümanları listeler.
        """
        if not self.instruments:
            print("Portföy boş. Lütfen enstrüman ekleyin.")
        else:
            print(f"{self.user.name} için Portföy:")
            for i, instrument in enumerate(self.instruments, 1):
                print(f"{i}. Sembol: {instrument['Sembol']}, Miktar: {instrument['Miktar']}, Fiyat: {instrument['Fiyat']}")