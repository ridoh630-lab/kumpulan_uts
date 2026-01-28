import fungsi

while True:
    print("\n=== MENU BANGUN DATAR ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar Genjang")
    print("6. Trapesium")
    print("7. Belah Ketupat")
    print("8. Layang-layang")
    print("9. Segi Lima")
    print("10. Segi Enam")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        s = float(input("Masukkan sisi: "))
        print("Luas:", fungsi.luas_persegi(s))
        print("Keliling:", fungsi.keliling_persegi(s))

    elif pilihan == "2":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Luas:", fungsi.luas_persegi_panjang(p, l))
        print("Keliling:", fungsi.keliling_persegi_panjang(p, l))

    elif pilihan == "3":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas:", fungsi.luas_segitiga(a, t))

    elif pilihan == "4":
        r = float(input("Masukkan jari-jari: "))
        print("Luas:", fungsi.luas_lingkaran(r))
        print("Keliling:", fungsi.keliling_lingkaran(r))

    elif pilihan == "5":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas:", fungsi.luas_jajar_genjang(a, t))

    elif pilihan == "6":
        a = float(input("Sisi sejajar A: "))
        b = float(input("Sisi sejajar B: "))
        t = float(input("Tinggi: "))
        print("Luas:", fungsi.luas_trapesium(a, b, t))

    elif pilihan == "7":
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        print("Luas:", fungsi.luas_belah_ketupat(d1, d2))

    elif pilihan == "8":
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        print("Luas:", fungsi.luas_layang_layang(d1, d2))

    elif pilihan == "9":
        s = float(input("Masukkan sisi: "))
        print("Keliling:", fungsi.keliling_segilima(s))

    elif pilihan == "10":
        s = float(input("Masukkan sisi: "))
        print("Keliling:", fungsi.keliling_segienam(s))

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")