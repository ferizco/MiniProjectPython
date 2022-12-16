#define class with null variable
class Mahasiswa:
    nama =  None
    asal = None
#create function
    def perkenalan (self):
        print(f'Perkenalkan saya {self.nama} dari {self.asal}')
#create object
ferizco = Mahasiswa()
ferizco.nama = "Ferizco"
ferizco.asal = "palembang"

#run function
ferizco.perkenalan()