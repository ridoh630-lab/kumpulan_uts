from utils import hitung_total, parse

data_input = input("Masukkan data: ")
angka = parse(data_input)
jumlah = hitung_total(angka)

print("Hasil penjumlahan:", jumlah)
