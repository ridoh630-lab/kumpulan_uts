from utils import parse_nilai, hitung_rata_rata

# Input jumlah orang
jumlah_orang = int(input("Masukkan jumlah orang: "))

hasil_rata_rata = []

# Input nilai tiap orang
for i in range(1, jumlah_orang + 1):
    data_nilai = input(f"Masukkan nilai orang ke-{i} (pisahkan spasi): ")
    daftar_nilai = parse_nilai(data_nilai)
    rata_rata = hitung_rata_rata(daftar_nilai)
    hasil_rata_rata.append(rata_rata)

# Output
print("\n=== HASIL ===")
print("Jumlah orang:", jumlah_orang)
for i, rata in enumerate(hasil_rata_rata, start=1):
    print(f"Rata-rata nilai orang ke-{i}: {rata}")