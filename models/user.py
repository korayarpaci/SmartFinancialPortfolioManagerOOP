class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user_info(self):
        return {
            "Ad": self.name,
            "E-posta": self.email
        }

# TEST
##user = User("<Koray>", "<Arpacı>")
##print("Kullanıcı Bilgileri:")
##print(user.get_user_info())