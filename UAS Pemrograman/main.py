from model import daftar_nilai
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
