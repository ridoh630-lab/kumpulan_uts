import math

# ===== BANGUN DATAR =====

# 1. Persegi
def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi


# 2. Persegi Panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)


# 3. Segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(a, b, c):
    return a + b + c


# 4. Lingkaran
def luas_lingkaran(r):
    return math.pi * r * r

def keliling_lingkaran(r):
    return 2 * math.pi * r


# 5. Jajar Genjang
def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

def keliling_jajar_genjang(a, b):
    return 2 * (a + b)


# 6. Trapesium
def luas_trapesium(a, b, tinggi):
    return 0.5 * (a + b) * tinggi

def keliling_trapesium(a, b, c, d):
    return a + b + c + d


# 7. Belah Ketupat
def luas_belah_ketupat(d1, d2):
    return 0.5 * d1 * d2

def keliling_belah_ketupat(sisi):
    return 4 * sisi


# 8. Layang-layang
def luas_layang_layang(d1, d2):
    return 0.5 * d1 * d2

def keliling_layang_layang(a, b):
    return 2 * (a + b)


# 9. Segi Lima
def keliling_segilima(sisi):
    return 5 * sisi


# 10. Segi Enam
def keliling_segienam(sisi):
    return 6 * sisi