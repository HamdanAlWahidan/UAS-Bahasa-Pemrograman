# UAS-Bahasa-Pemrograman

**Struktur Package & Module**


**Penjelasan:**

**Modul**

file daftar_nilai in folder model

*TAMBAH DATA*

* ``data = []
  data = {}`` -> untuk menampung beberapa list data yang nanti akan terinput.
  
* ``def tambah():`` 
-> command yang ber fungsi memanggil script di folder dan file yang berbeda.

```       print("=======Tambah Data=======")
        nama    =input("Nama                :  ")
        nim     =input("Nim                 :  ")
        tugas   =int(input("Masukan Nilai Tugas :  "))
        uts     =int(input("Masukan Nilai UTS   :  "))
        uas     =int(input("Masukan Nilai UAS   :  "))
        akhir   = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim ,tugas, uts, uas, akhir 
 ``` 
        
-> script di atas berfungsi untuk menginputkan data ketika program ini di jalankan.

*UBAH DATA*


* ``def ubah()``
-> command ini harus ada di setiap pemrograman karna berfungsi sebagai pemanggil program tersebut jika command ini tidak ada makan program tersebut tidak akan terpanggil.


* ```
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
            print("Data Nilai Tidak Ada".format(nama))```
         

* -> scipt diatas berfungsi untuk mengubah data yang telah di input kan ke dalam program.

* ``-> data[nama] = `` 
-> command ini berfungsi untuk memanggil beberapa command di atas seperti ``nim,tugas,uts,uas,dan akhir``

*HAPUS DATA*

* ``def hapus():``
-> seperti biasa command ini harus ada.

* ```        print("=======Hapus Data Mahasiswa=======")
            nama=input("Nama :  ")
            if nama in data.keys():
                del data[nama]
            else:
                print("Data Nilai Tidak Ada".format(nama)) 
``` 
                
-> script diatas berfungsi untuk menghapus beberapa data yang telah terinputkan.

* ``nama = input("Nama : ")`` -> command ini berfungsi untuk mencari data yang telah diinputkan, setalah itu command ini -> ``if nama in data.key()`` berfungsi mencari data inputan yang di cari apakah data inputan itu ada dalam program atau tidak yang terdapat pada command ini -> ``in data.key()``


*CARI DATA*

* ```   print("=======Cari Data Mahasiswa=======")
          nama=input("Masukan Nama :  ")
          if nama in data.keys():
              print("Daftar Nilai Mahasiswa")
              print("================================================================================================")
              print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
              print("================================================================================================")
              print("|    {0} |   {1} | ".format(nama, data[nama]))
              print("===============================================================================================")
          else:
              print("Datanya {0} Tidak Ada ".format(nama))``` 
            
-> script ini berfungsi mencari dan melihat apakah data yang diinputkan sudah ada

* Penjelasannya seperti ``*hapus data*``


**file input_nilai in folder view**

* ``` data = []
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
```
-> sama seperti ``tambah data``


file view_nilai in folder view

* 
```def cari():
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

def lihat():
    if data.items():
        print("Daftar Nilai Mahasiswa")
        print("================================================================================================")
        print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
        print("================================================================================================")
        i=0
        for x in data.items():
            i+=1
            print(" | {6:2}  |  {0:12s} | {1:9s} | {2:11}  | {3:11} | {4:11}  |  {5:11} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("============================================================================================")
    else:
        print("Daftar Nilai Mahasiswa")
        print("================================================================================================")
        print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
        print("================================================================================================")
        print("|                                      TIDAK ADA DATA                                         |")
        print("===============================================================================================")```

file view_nilai in folder view

* ``` def cari():
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

def lihat():
    if data.items():
        print("Daftar Nilai Mahasiswa")
        print("================================================================================================")
        print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
        print("================================================================================================")
        i=0
        for x in data.items():
            i+=1
            print(" | {6:2}  |  {0:12s} | {1:9s} | {2:11}  | {3:11} | {4:11}  |  {5:11} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("============================================================================================")
    else:
        print("Daftar Nilai Mahasiswa")
        print("================================================================================================")
        print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
        print("================================================================================================")
        print("|                                      TIDAK ADA DATA                                         |")
        print("===============================================================================================")```
        
        
* file main 

* ```from model import daftar_nilai
from view import input_nilai
from view import view_nilai

print("======== LOGIN KAMPUS PELITA BANGSA =========")
data={}
while True:
    print("")
    c =input("(D)osen, (M)ahasiswa, (K)eluar : ")
    if c.lower() == 'k':
        print("Keluar")
        break

    elif c.lower() == 'd':
        d=input("(L)ogin, (K)embali : ")
        if d.lower() == 'l':
            user = input("Username : ")
            import getpass
            sandi = getpass.getpass()
            if sandi == 'admin' and user == 'admin':
                while True:
                    print ("Anda Telah Login")
                    f=input("MENU: (T)ambah Data, (U)bah Data, (H)apus Data, (C)ari Data, (K)eluar : ")

                    if f.lower() == 't':
                        daftar_nilai.tambah()

                    elif f.lower() == 'u':
                        daftar_nilai.ubah()

                    elif f.lower() == 'h':
                        daftar_nilai.hapus()

                    elif f.lower() == 'c':
                        daftar_nilai.cari()

                    elif f.lower() == 'k':
                        break

                else:
                    print ("Username atau Password Anda Salah")

            elif d.lower() == 'k':
                continue

    elif c.lower() == 'm':
        e=input("(L)ogin, (K)embali : ")
        if e.lower() == 'l':
            user = input("Username : ")
            import getpass
            sandi = getpass.getpass()
            if sandi == '123' and user == 'mahasiswa':
                while True:
                    print ("Anda Telah Login")
                    g=input("MENU: (T)ambah Data, (C)ari Data (L)ihat, (K)eluar : ")
                    if g.lower() == 't':
                        input_nilai.inputdata()
                        view_nilai.inputdata()

                    elif g.lower() == 'c':
                        view_nilai.cari()

                    elif g.lower() ==  'l':
                        view_nilai.lihat()

                    elif g.lower() == 'k':
                        break

                else:
                    print ("Username atau Password Anda Salah")

        elif e.lower() == 'k':
            continue
```

-> di file main saya menambahkan beberapa command user ID dimana sebelum menginput data mahasiswa ktia harus mengisi user ID tersebut, seperti command ini 

``` user = input("Username : ")
    import getpass
    sandi = getpass.getpass()
    if sandi == 'admin' and user == 'admin': 
```
    
 -> command itu yang digunakan untuk login melalui menu dosen.
 
 ``` user = input("Username : ")
    import getpass
    sandi = getpass.getpass()
    if sandi == '123' and user == 'mahasiswa': 
```
-> jika command yang diatas itu untuk login user ID melalui menu Mahasiswa.


* FOTO HASILNYA
![Latihan 4.1](https://github.com/HamdanAlWahidan/UAS-Bahasa-Pemrograman/blob/main/SS%20UAS%20Pemrograman/1.png) <br>
![Latihan 4.2](https://github.com/HamdanAlWahidan/UAS-Bahasa-Pemrograman/blob/main/SS%20UAS%20Pemrograman/2.png) <br>
![Latihan 4.3](https://github.com/HamdanAlWahidan/UAS-Bahasa-Pemrograman/blob/main/SS%20UAS%20Pemrograman/3.png) <br>
![Latihan 4.4](https://github.com/HamdanAlWahidan/UAS-Bahasa-Pemrograman/blob/main/SS%20UAS%20Pemrograman/4.png) <br>
![Latihan 4.5](https://github.com/HamdanAlWahidan/UAS-Bahasa-Pemrograman/blob/main/SS%20UAS%20Pemrograman/5.png) <br>
![Latihan 4.6](https://github.com/HamdanAlWahidan/UAS-Bahasa-Pemrograman/blob/main/SS%20UAS%20Pemrograman/6.png) <br>
![Latihan 4.6](https://github.com/HamdanAlWahidan/UAS-Bahasa-Pemrograman/blob/main/SS%20UAS%20Pemrograman/7.png) <br>
