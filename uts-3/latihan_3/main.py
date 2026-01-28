from utils import nilai_kelulusan, parse_list

data_input = input("masukan data siswa: ")
data = parse_list(data_input)

nilai = nilai_kelulusan(data)
print("nilai rata rata siswa", nilai)