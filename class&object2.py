#class dengan constructor
class Mahasiswa():
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan (self):
        print(f'perkenalkan saya {self.nama} dari {self.asal}')

ferizco = Mahasiswa('ferizco', 'palembang')

ferizco.perkenalan()