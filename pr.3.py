print("=================================")
print("pr. 3")
def list_ku():
    daftar=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
    baris=int(input("Pilih Baris = "))
    print(daftar[baris])
    kolom=int(input("Pilih Kolom = "))
    print(daftar[baris][kolom])
    ubah=input("Ingin Ubah Angka ? ")

    if (ubah=="Y" or ubah=="y"):
        angka_baru=int(input("Masukkan angka baru =")) 
        daftar[baris][kolom]=angka_baru
    print(daftar[baris])

def utama_listku():
    print("coba list 2dimensi")
    list_ku()

utama_listku()