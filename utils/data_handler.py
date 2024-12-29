import csv

class DataHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        data = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Hata: Dosya bulunamadı - {self.filename}")
        return data

    def write_csv(self, data):
        try:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print(f"Veri başarıyla {self.filename} dosyasına kaydedildi.")
        except Exception as e:
            print(f"Veri kaydedilemedi: {e}")