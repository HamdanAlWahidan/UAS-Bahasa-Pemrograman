data = []
data = {}

def inputdata():
        print("=======Tambah Data=======")
        nama    =input("Nama                :  ")
        nim     =input("Nim                 :  ")
        tugas   =int(input("Masukan Nilai Tugas :  "))
        uts     =int(input("Masukan Nilai UTS   :  "))
        uas     =int(input("Masukan Nilai UAS   :  "))
        akhir   = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim ,tugas, uts, uas, akhir
