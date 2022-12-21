# buat fungsi yang mengembalikan nilai list
def fibonacci (n):
    if n < 1:
        return[n]

    listSebelumN = fibonacci(n -1)
    angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
    angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

    return listSebelumN + [angka1 + angka2]

panjang = int(input('masukkan panjang deret: '))
print('----Deret Fibonacci----')
print(fibonacci(panjang-1))