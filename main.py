from models.user import User
from models.portfolio import Portfolio


def main():
    print("Akıllı Finansal Portföy Yöneticisine Hoş Geldiniz!")

    name = input("Adınızı girin: ")
    email = input("E-posta adresinizi girin: ")
    user = User(name, email)

    portfolio = Portfolio(user)
    print(f"{user.name} için portföy oluşturuldu. Şimdi yatırımlarınızı yönetmeye başlayalım!")

    while True:
        print("\n1. Finansal Enstrüman Ekle")
        print("2. Portföyü Görüntüle")
        print("3. Risk Analizi Yap")
        print("4. Çıkış")

        choice = input("Bir seçenek seçin: ")

        if choice == "1":
            symbol = input("Finansal enstrümanın sembolünü girin: ")
            quantity = float(input("Miktarı girin: "))
            price = float(input("Birim başına fiyatı girin: "))
            portfolio.add_instrument(symbol, quantity, price)
            print(f"{symbol}, portföyünüze eklendi.")

        elif choice == "2":
            print("Portföyünüz:")
            portfolio.view_portfolio()

        elif choice == "3":
            print("Risk analizi yapım aşamasında.")

        elif choice == "4":
            print("Hosçakalın !!")
            break

        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
