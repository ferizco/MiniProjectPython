import random

angka = random.randint(1, 100)

print('='*23)
print('Silahkan Tebak Angkanya')
print('='*23)

batas_percobaan = 7

for percobaan in range(batas_percobaan):
    jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukkan angka: '))

    if jawaban == angka:
        print('Selamat tebakanmu benar')
        break
    else:
        print(
            'Tebakanmu terlalu',
            'kecil' if jawaban < angka else 'besar'
        )
else:
    print(f'\nSayang sekali kamu sudah salah menebak sebanyak {batas_percobaan}x')