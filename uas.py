import sqlite3
from os import system
from prettytable import PrettyTable

def lihat_data():
    print()
    cursor.execute(""" SELECT COUNT(*) from Mahasiswa1 """)
    result = cursor.fetchall()
    if result[0][0] == 0:
        print("Data masih kosong")
    else:
        x = PrettyTable()
        x.field_names = ["NPM", "Nama", "Prodi"]
        for row in cursor.execute("SELECT NPM, nama, prodi from Mahasiswa1"):
            x.add_row([row[0], row[1], row[2]])
        print(x)

def tambah_data():
    NPM_baru = input("NPM : ")
    nama_baru = input("Nama : ")
    prodi_baru = input("Prodi: ")

    if NPM_baru and nama_baru and prodi_baru:
        if NPM_baru.isdigit():
            cursor.execute("""INSERT INTO Mahasiswa1(NPM,nama,prodi) VALUES(?,?,?)""", (NPM_baru,nama_baru,prodi_baru))
            db.commit()
        else:
            print("Masukkan NPM dengan benar")
    else:
        print("Mohon isi seluruh data")

def hapus_data():
    npm_hapus = int(input("NPM yang ingin dihapus : "))
    cursor.execute("SELECT rowid FROM Mahasiswa1 WHERE NPM = ?", (npm_hapus,))
    data = cursor.fetchone()
    print()
    if data is None:
        print("Gagal menghapus. NPM", npm_hapus, "tidak ditemukan")
    else:
        print("Berhasil menghapus")
        cursor.execute("DELETE FROM Mahasiswa1 where NPM = ?", (npm_hapus,))
        db.commit()

def cari_data():
    print("Cari data berdasarkan :")
    print("1. NPM")
    print("2. Nama")
    cari =  int(input("Masukkan pilihan anda : "))
    if (cari == 1):
        npm_cari = int(input("NPM : "))
        cursor.execute("SELECT rowid FROM Mahasiswa1 WHERE NPM = ?", (npm_cari,))
        data = cursor.fetchone()
        if data is None:
            print("Gagal mencari data")
        else:
            x = PrettyTable()
            x.field_names = ["NPM", "Nama", "Prodi"]
            for row in cursor.execute("SELECT NPM, nama, prodi from Mahasiswa1"):
                if row[0] == npm_cari:
                    x.add_row([row[0], row[1], row[2]])
                    break
            print(x)
            tanya = input("Apakah ingin mengubah data (Y/T) : ")
            if (tanya.upper() == "Y"):
                tanyalg = input("Data apa yang ingin diubah (npm,nama,prodi): ")
                if (tanyalg == "nama" or tanyalg == "Nama" or tanyalg == "NAMA"):
                    NPM_baru1 = npm_cari
                    nama_baru1 = input("Nama : ")
                    cursor.execute("UPDATE Mahasiswa1 SET nama=? WHERE NPM=?", (nama_baru1, NPM_baru1))
                    db.commit()
                elif (tanyalg == "prodi" or tanyalg == "Prodi" or tanyalg == "PRODI"):
                    NPM_baru1 = npm_cari
                    prodi_baru1 = input("Prodi : ")
                    cursor.execute("UPDATE Mahasiswa1 SET prodi=? WHERE NPM=?", (prodi_baru1, NPM_baru1))
                    db.commit()
                elif (tanyalg == "npm" or tanyalg == "Npm" or tanyalg == "NPM"):
                    NPM_baru1 = npm_cari
                    npm_baru1 = input("NPM : ")
                    cursor.execute("UPDATE Mahasiswa1 SET npm=? WHERE NPM=?", (npm_baru1, NPM_baru1))
                    db.commit()
                else:
                    print("Tipe data tidak tersedia")
            elif (tanya.upper() == "T"):
                print("Tidak ada perubahan data")
            else:
                print("Keyword error")
    elif (cari == 2):
        nama_cari = input("Nama : ")
        cursor.execute("SELECT rowid FROM Mahasiswa1 WHERE Nama = ?", (nama_cari,))
        data = cursor.fetchone()
        if data is None:
            print("Gagal mencari data")
        else:
            x = PrettyTable()
            x.field_names = ["NPM", "Nama", "Prodi"]
            for row in cursor.execute("SELECT NPM, nama, prodi from Mahasiswa1"):
                if row[1] == nama_cari:
                    x.add_row([row[0], row[1], row[2]])
                    break
            print(x)
            tanya = input("Apakah ingin mengubah data (Y/T) : ")
            if (tanya.upper() == "Y"):
                tanyalg = input("Data apa yang ingin diubah (npm,nama,prodi): ")
                if (tanyalg == "nama" or tanyalg == "Nama" or tanyalg == "NAMA"):
                    Name_baru1 = nama_cari
                    nama_baru1 = input("Nama : ")
                    cursor.execute("UPDATE Mahasiswa1 SET nama=? WHERE Nama=?", (nama_baru1, Name_baru1))
                    db.commit()
                elif (tanyalg == "prodi" or tanyalg == "Prodi" or tanyalg == "PRODI"):
                    Name_baru1 = nama_cari
                    prodi_baru1 = input("Prodi : ")
                    cursor.execute("UPDATE Mahasiswa1 SET prodi=? WHERE Nama=?", (prodi_baru1, Name_baru1))
                    db.commit()
                elif (tanyalg == "npm" or tanyalg == "Npm" or tanyalg == "NPM"):
                    Name_baru1 = nama_cari
                    npm_baru1 = input("NPM : ")
                    cursor.execute("UPDATE Mahasiswa1 SET npm=? WHERE Nama=?", (npm_baru1, Name_baru1))
                    db.commit()
                else:
                    print("Tipe data tidak tersedia")
            elif (tanya.upper() == "T"):
                print("Tidak ada perubahan data")
            else:
                print("Keyword error")
    else:
        print("Keyword error")


def show_menu():
    menu = 0
    while menu != 5:
        system("cls")
        print("DATA MAHASISWA UTY")
        print("1. Lihat data")
        print("2. Tambah data")
        print("3. Hapus data")
        print("4. Cari data")
        print("5. Keluar")
        menu = input("Pilih menu : ")

        if menu.isdigit():
            menu = int(menu)
            if menu == 1:
                lihat_data()
            elif menu == 2:
                tambah_data()
            elif menu == 3:
                hapus_data()
            elif menu == 4:
                cari_data()
            elif menu == 5:
                db.close()
                print("Keluar...")
                break
            else:
                print("Menu tidak tersedia")
                pass
        else:
            pass
        input("Tekan Enter Untuk Melanjutkan...")

def login():
    system("cls")
    user = input("Username : ")
    passw = input("Password : ")

    username = "admin"
    password = "admin"

    if (user == username and passw == password):
        print("Silahkan login, tap ENTER untuk melanjutkan")
        input()
        show_menu()
    else:
        print("Username atau password salah")
        input("")
        login()

with sqlite3.connect("UTY1.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Mahasiswa1(NPM integer PRIMARY KEY, nama text, prodi text);""")
db.commit()

login()