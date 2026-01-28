# Fungsi untuk mengubah angka menjadi format Rupiah
def ubah_ke_rupiah(angka):
    return "Rp {:,.0f}".format(angka).replace(",", ".")

# Input angka dari pengguna
angka = int(input("Masukkan angka: "))

# Menampilkan hasil dalam format Rupiah
print("Hasil:", ubah_ke_rupiah(angka))