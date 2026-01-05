from fungsi_nilai import (
    nilai_ke_label,
    label_ke_bobot,
    hitung_total_sks,
    hitung_total_nilai,
    hitung_ips
)

while True:
    print("\nMENU")
    print("1. Konversi nilai ke label")
    print("2. Konversi label ke bobot")
    print("3. Hitung total SKS yang diambil")
    print("4. Hitung total nilai")
    print("5. Hitung IPS")
    print("6. Exit")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nilai = int(input("Masukkan nilai: "))
        print("Label:", nilai_ke_label(nilai))

    elif pilihan == "2":
        label = input("Masukkan label (A-E): ").upper()
        print("Bobot:", label_ke_bobot(label))

    elif pilihan == "3":
        n = int(input("Jumlah mata kuliah: "))
        sks = []
        for i in range(n):
            sks.append(int(input(f"SKS ke-{i+1}: ")))
        print("Total SKS:", hitung_total_sks(sks))

    elif pilihan == "4":
        n = int(input("Jumlah mata kuliah: "))
        sks = []
        nilai = []

        print("Input SKS")
        for i in range(n):
            sks.append(int(input(f"SKS ke-{i+1}: ")))

        print("Input Nilai Mahasiswa")
        for i in range(n):
            nilai.append(int(input(f"Nilai ke-{i+1}: ")))

        total_nilai = hitung_total_nilai(nilai, sks)
        print("Total Nilai:", total_nilai)

    elif pilihan == "5":
        n = int(input("Jumlah mata kuliah: "))
        sks = []
        nilai = []

        print("Input SKS")
        for i in range(n):
            sks.append(int(input(f"SKS ke-{i+1}: ")))

        print("Input Nilai Mahasiswa")
        for i in range(n):
            nilai.append(int(input(f"Nilai ke-{i+1}: ")))

        total_sks = hitung_total_sks(sks)
        total_nilai = hitung_total_nilai(nilai, sks)
        ips = hitung_ips(total_nilai, total_sks)

        print("IPS:", round(ips, 2))

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid!")