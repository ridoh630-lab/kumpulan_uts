import math

# 1. Kubus
def volume_kubus(sisi):
    return sisi ** 3

def luas_kubus(sisi):
    return 6 * sisi * sisi


# 2. Balok
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def luas_balok(panjang, lebar, tinggi):
    return 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)


# 3. Prisma Segitiga
def volume_prisma_segitiga(alas, tinggi_segitiga, tinggi_prisma):
    return 0.5 * alas * tinggi_segitiga * tinggi_prisma


# 4. Tabung
def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari * jari_jari * tinggi


# 5. Kerucut
def volume_kerucut(jari_jari, tinggi):
    return (1/3) * math.pi * jari_jari * jari_jari * tinggi


# 6. Bola
def volume_bola(jari_jari):
    return (4/3) * math.pi * jari_jari ** 3


# 7. Limas Segiempat
def volume_limas_segiempat(sisi_alas, tinggi):
    return (1/3) * sisi_alas * sisi_alas * tinggi


# 8. Limas Segitiga
def volume_limas_segitiga(alas, tinggi_segitiga, tinggi_limas):
    return (1/3) * 0.5 * alas * tinggi_segitiga * tinggi_limas


# 9. Prisma Segiempat
def volume_prisma_segiempat(sisi_alas, tinggi):
    return sisi_alas * sisi_alas * tinggi


# 10. Prisma Segilima
def volume_prisma_segilima(luas_alas, tinggi):
    return luas_alas * tinggi