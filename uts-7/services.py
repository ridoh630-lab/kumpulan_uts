import os
import time

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def format_rupiah(angka):
    return f"Rp {angka:,}".replace(",", ".")

def jeda():
    input("Tekan ENTER untuk lanjut...")