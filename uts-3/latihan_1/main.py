from utils import cari_nilai_terbesar, cari_nilai_terkecil, parse_list

data = input("Masukkan data: ")

data = parse_list(data)

nilai_terbesar = cari_nilai_terbesar(data)
nilai_terkecil = cari_nilai_terkecil(data)

print("Nilai terbesar: ", nilai_terbesar)
print("nilai terkecil :", nilai_terkecil)