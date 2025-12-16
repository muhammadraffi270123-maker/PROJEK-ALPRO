import json, os

FILE = "uang.json"

def baca():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def simpan(data):
    json.dump(data, open(FILE, "w"), indent=2)

def tambah():
    tgl = input("Tanggal (DD-MM-YYYY): ")
    jenis = input("Jenis (pemasukan(IN) / pengeluaran(OUT)): ").lower()
    jumlah = float(input("Jumlah: "))
    kat = input("Kategori: ")

    if jenis not in ("in",  "out"):
        print("TOLONG MASUKKAN IN ATAU OUT!\n")
        return

    data = baca()
    data.append({"tanggal": tgl, "jenis": jenis, "jumlah": jumlah, "kategori": kat})
    simpan(data)
    print("Tersimpan!\n") 

def lihat():
    data = baca()
    if not data:
        print("Belum ada data.\n"); return
    for d in data:
        print(f"{d['tanggal']} | {d['jenis']} | {d['kategori']} | Rp{d['jumlah']}")
    print()

def saldo():
    data = baca()
    masuk = sum(d["jumlah"] for d in data if d["jenis"] == "in")
    keluar = sum(d["jumlah"] for d in data if d["jenis"] == "out")
    print(f"Pemasukan : Rp{masuk}")
    print(f"Pengeluaran: Rp{keluar}")
    print(f"Saldo     : Rp{masuk - keluar}\n")

while True:
    print("=== PROGRAM MANAJEMEN UANG ===")
    print("1. Tambah Transaksi")
    print("2. Lihat Semua Transaksi")
    print("3. Lihat Saldo")
    print("4. Keluar")

    p = input("Pilih: ")
    if p == "1": tambah()
    elif p == "2": lihat()
    elif p == "3": saldo()
    elif p == "4": break
    else: print("Pilihan salah!\n")

print("TERIMA KASIH SUDAH MENCATAT :)")
