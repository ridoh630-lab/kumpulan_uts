def parse_list(list_string):
    return list(map(int, list_string.split()))

def total_harga(data):
    return sum(data)

def hitung_diskon(total):
    if total > 50000:
        return total * 0.001  # diskon 0,1%
    return 0

def hitung_pajak(total_setelah_diskon):
    return total_setelah_diskon * 0.10  # pajak 10%

def format_rupiah(angka):
    return format(int(angka), ",").replace(",", ".")