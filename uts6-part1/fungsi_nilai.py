def nilai_ke_label(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 65:
        return 'C'
    elif nilai >= 50:
        return 'D'
    else:
        return 'E'


def label_ke_bobot(label):
    if label == 'A':
        return 4
    elif label == 'B':
        return 3
    elif label == 'C':
        return 2
    elif label == 'D':
        return 1
    else:
        return 0


def hitung_total_sks(sks_list):
    return sum(sks_list)


def hitung_total_nilai(nilai_list, sks_list):
    total = 0
    for i in range(len(nilai_list)):
        label = nilai_ke_label(nilai_list[i])
        bobot = label_ke_bobot(label)
        total += bobot * sks_list[i]
    return total


def hitung_ips(total_nilai, total_sks):
    if total_sks == 0:
        return 0
    return total_nilai / total_sks