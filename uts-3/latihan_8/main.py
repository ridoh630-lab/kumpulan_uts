from utils import ambil_input

# Input jumlah orang
jumlah_orang = int(input("Masukkan jumlah orang: "))

hasil = []

# Input jumlah barang tiap orang (bebas, bisa pakai spasi)
for i in range(1, jumlah_orang + 1):
    data = input(f"Jumlah barang orang ke-{i}: ")
    hasil.append(ambil_input(data))

# Output
print("\n=== HASIL ===")
print("Jumlah orang:", jumlah_orang)
for i, nilai in enumerate(hasil, start=1):
    print(f"Jumlah barang orang ke-{i}:", nilai)