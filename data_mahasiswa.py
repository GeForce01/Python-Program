import sqlite3
from os import system
#from prettytable import PrettyTable

def lihat_data():
    cursor.execute(""" SELECT COUNT(*) from Mahasiswa1 """)
    result = cursor.fetchall()
    print("")
    if result[0][0] == 0:
        print("Data masih kosong")
    else:
        for x in cursor.execute("SELECT NPM, nama, prodi from Mahasiswa1"):
            print("NPM :", x[0])
            print("Nama :", x[1])
            print("Prodi :", x[2],"\n")
   
def tambah_data():
    NPM_baru = int(input("NPM : "))
    nama_baru = input("Nama : ")
    prodi_baru = input("Prodi: ")

    cursor.execute("""INSERT INTO Mahasiswa1(NPM,nama,prodi)VALUES(?,?,?)""", (NPM_baru,nama_baru,prodi_baru))
    db.commit()

def hapus_data():
    npm_hapus = int(input("NPM yang ingin dihapus : "))

    cursor.execute("DELETE FROM Mahasiswa1 where NPM = ?", (npm_hapus,))
    db.commit()

with sqlite3.connect("UTY.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Mahasiswa1(NPM integer PRIMARY KEY, nama text, prodi text);""")
db.commit()

menu = 0
while menu != 4:
    system("cls")
    print("DATA MAHASISWA UTY")
    print("1. Lihat data")
    print("2. Tambah data")
    print("3. Hapus data")
    print("4. Keluar")
    menu = int(input("Pilih menu : "))

    if menu == 1:
        lihat_data()
        input("Tekan Enter Untuk Melanjutkan...")
    elif menu == 2:
        tambah_data()
        input("Tekan Enter Untuk Melanjutkan...")
    elif menu == 3:
        hapus_data()
        input("Tekan Enter Untuk Melanjutkan...")
    elif menu == 4:
        db.close()
        print("Keluar...")