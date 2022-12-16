class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f'perkenalkan nama saya {self.nama} dari {self.asal}')

class Pelajar(Orang):
    def __init__(self, nama,asal, sekolah):
        super().__init__(nama, asal)
        self.sekolah = sekolah

class Pekerja(Orang):
    def __init__(self,nama,asal, tempat_kerja):
        super().__init__( nama, asal)
        self.tempat_kerja = tempat_kerja

andi = Orang('Andi','palembang')
andi.perkenalan()

deni = Pelajar('Deni','jakarta','sma n 1 jakarta')
deni.perkenalan()
print(f'saya sekolah di {deni.sekolah}')

budi = Pekerja('Budi','malang', 'PT pupuk indonesia')
budi.perkenalan()
print(f'saya bekerja di {budi.tempat_kerja}')