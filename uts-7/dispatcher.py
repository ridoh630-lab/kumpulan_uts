from controller import proses_atm
from services import bersihkan_layar, format_rupiah, jeda

nama = USER_DATA["nama"]
saldo = USER_DATA["saldo"]

while True:
    bersihkan_layar()
    print("=== MENU ATM ===")
    print("Nama :", nama)
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Ganti Rekening")
    print("5. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        saldo, _ = proses_atm(saldo, "CEK")
        print("Saldo Anda:", format_rupiah(saldo))
        jeda()

    elif pilih == "2":
        nominal = int(input("Masukkan nominal: "))
        saldo, pesan = proses_atm(saldo, "TARIK", nominal)
        print(pesan)
        jeda()

    elif pilih == "3":
        nominal = int(input("Masukkan nominal: "))
        saldo, pesan = proses_atm(saldo, "SETOR", nominal)
        print(pesan)
        jeda()

    elif pilih == "4":
        USER_DATA["saldo"] = saldo
        break

    elif pilih == "5":
        USER_DATA["saldo"] = saldo
        exit()

    else:
        print("Menu tidak tersedia")
        jeda()