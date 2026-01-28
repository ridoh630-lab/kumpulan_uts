from fungsi import *

print("=== PROGRAM BANGUN RUANG ===")

# 1. Kubus
sisi = float(input("Masukkan sisi kubus: "))
print("Volume kubus:", volume_kubus(sisi))
print("Luas kubus:", luas_kubus(sisi))
print()

# 2. Balok
panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))
print("Volume balok:", volume_balok(panjang, lebar, tinggi))
print("Luas balok:", luas_balok(panjang, lebar, tinggi))
print()

# 3. Prisma Segitiga
alas = float(input("Masukkan alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))
print("Volume prisma segitiga:", volume_prisma_segitiga(alas, tinggi_segitiga, tinggi_prisma))
print()

# 4. Tabung
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))
print("Volume tabung:", volume_tabung(jari_jari, tinggi))
print()

# 5. Kerucut
jari_jari = float(input("Masukkan jari-jari kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))
print("Volume kerucut:", volume_kerucut(jari_jari, tinggi))
print()

# 6. Bola
jari_jari = float(input("Masukkan jari-jari bola: "))
print("Volume bola:", volume_bola(jari_jari))
print()

# 7. Limas Segiempat
sisi_alas = float(input("Masukkan sisi alas limas segiempat: "))
tinggi = float(input("Masukkan tinggi limas: "))
print("Volume limas segiempat:", volume_limas_segiempat(sisi_alas, tinggi))
print()

# 8. Limas Segitiga
alas = float(input("Masukkan alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))
print("Volume limas segitiga:", volume_limas_segitiga(alas, tinggi_segitiga, tinggi_limas))
print()

# 9. Prisma Segiempat
sisi_alas = float(input("Masukkan sisi alas prisma segiempat: "))
tinggi = float(input("Masukkan tinggi prisma: "))
print("Volume prisma segiempat:", volume_prisma_segiempat(sisi_alas, tinggi))
print()

# 10. Prisma Segilima
luas_alas = float(input("Masukkan luas alas segilima: "))
tinggi = float(input("Masukkan tinggi prisma: "))
print("Volume prisma segilima:", volume_prisma_segilima(luas_alas, tinggi))

print("\nProgram selesai.")