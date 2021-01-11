data = []
data = {}

def tambah():
        print("=======Tambah Data=======")
        nama    =input("Nama                :  ")
        nim     =input("Nim                 :  ")
        tugas   =int(input("Masukan Nilai Tugas :  "))
        uts     =int(input("Masukan Nilai UTS   :  "))
        uas     =int(input("Masukan Nilai UAS   :  "))
        akhir   = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim ,tugas, uts, uas, akhir

def ubah():
        print('=======Ubah Data Mahasiswa=======')
        nama = input('Nama                :  ')
        if nama in data.keys():
            nim     =input('Nim                 :  ')
            tugas   =int(input("Masukan Nilai Tugas :  "))
            uts     =int(input("Masukan Nilai UTS   :  "))
            uas     =int(input("Masukan Nilai UAS   :  "))
            akhir   =(0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim, tugas, uts, uas, akhir
        else:
            print("Data Nilai Tidak Ada".format(nama))

def hapus():
        print("=======Hapus Data Mahasiswa=======")
        nama=input("Nama :  ")
        if nama in data.keys():
            del data[nama]
        else:
            print("Data Nilai Tidak Ada".format(nama))

def cari():
        print("=======Cari Data Mahasiswa=======")
        nama=input("Masukan Nama :  ")
        if nama in data.keys():
            print("Daftar Nilai Mahasiswa")
            print("================================================================================================")
            print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
            print("================================================================================================")
            print("|    {0} |   {1} | ".format(nama, data[nama]))
            print("===============================================================================================")
        else:
            print("Datanya {0} Tidak Ada ".format(nama))
