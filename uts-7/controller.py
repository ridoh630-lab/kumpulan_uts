def proses_atm(saldo, aksi, nominal=0):
    if aksi == "CEK":
        return saldo, "OK"

    if aksi == "TARIK":
        if nominal <= saldo:
            return saldo - nominal, "TARIK BERHASIL"
        return saldo, "SALDO TIDAK CUKUP"

    if aksi == "SETOR":
        return saldo + nominal, "SETOR BERHASIL"

    if aksi == "KELUAR":
        return saldo, "KELUAR"

    return saldo, "AKSI TIDAK VALID"