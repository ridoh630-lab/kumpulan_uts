from utils import total_harga, parse_list, hitung_diskon

data_input = input("Masukkan data harga: ")
data = parse_list(data_input)

total = total_harga(data)
diskon = hitung_diskon(total)
total_bayar = total - diskon

print("Total harga       :", total)
print("Diskon            :", diskon)
print("Total yang dibayar:", total_bayar)