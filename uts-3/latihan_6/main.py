from utils import (
    parse_list,
    total_harga,
    hitung_diskon,
    hitung_pajak,
    format_rupiah
)

data_input = input("Masukkan harga barang (pisahkan spasi): ")
data = parse_list(data_input)

total = total_harga(data)
diskon = hitung_diskon(total)
total_setelah_diskon = total - diskon
pajak = hitung_pajak(total_setelah_diskon)
total_bayar = total_setelah_diskon + pajak

print("Total harga           : Rp", format_rupiah(total))
print("Diskon                : Rp", format_rupiah(diskon))
print("Total setelah diskon  : Rp", format_rupiah(total_setelah_diskon))
print("Pajak 10%             : Rp", format_rupiah(pajak))
print("Total yang dibayar    : Rp", format_rupiah(total_bayar))