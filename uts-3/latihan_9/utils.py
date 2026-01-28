def parse_nilai(data):
    # Ubah input spasi menjadi list angka
    return list(map(float, data.split()))


def hitung_rata_rata(daftar_nilai):
    # Hitung rata-rata nilai
    if len(daftar_nilai) == 0:
        return 0
    return sum(daftar_nilai) / len(daftar_nilai)