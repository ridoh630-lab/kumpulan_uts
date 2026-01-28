from constants import DATA_USER
from services import bersihkan_layar

while True:
    bersihkan_layar()
    print("=== LOGIN ATM ===")
    no_rek = input("Masukkan No Rekening: ")

    if no_rek in DATA_USER:
        USER_DATA = DATA_USER[no_rek]
        exec(open("dispatcher.py").read())
    else:
        print("Rekening tidak ditemukan")
        input("Tekan ENTER...")