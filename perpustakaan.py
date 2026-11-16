"""Aplikasi 3: Perpustakaan Mini."""

from fp1lib import pipe, ambil, saring, cari, urutkan, kelompokkan, validasi, rupiah

katalog = [
    {"kode": "B01", "judul": "Laskar Pelangi", "kategori": "Novel", "stok": 3, "denda": 1000},
    {"kode": "B02", "judul": "Bumi Manusia", "kategori": "Novel", "stok": 2, "denda": 1000},
    {"kode": "B03", "judul": "Dasar Python", "kategori": "Teknologi", "stok": 4, "denda": 1500},
    {"kode": "B04", "judul": "Basis Data", "kategori": "Teknologi", "stok": 1, "denda": 1500},
]

peminjaman = [
    {"peminjam": "Rafi", "kode": "B01", "terlambat": 2},
    {"peminjam": "Nina", "kode": "B03", "terlambat": 0},
]


def denda_pinjam(item):
    buku = cari(katalog, lambda x: x["kode"] == item["kode"])
    return item["terlambat"] * (buku["denda"] if buku else 0)


def tampilkan_katalog():
    print("\\n--- KATALOG BUKU ---")
    for buku in ambil(katalog, 100):
        print(f'{buku["kode"]} | {buku["judul"]} | {buku["kategori"]} | Stok: {buku["stok"]}')


def pinjam_buku():
    kode = input("Kode buku: ").strip().upper()
    buku = cari(katalog, lambda x: x["kode"] == kode)
    validasi(buku, lambda x: x is not None, "Buku tidak ditemukan")
    validasi(buku["stok"], lambda x: x > 0, "Stok buku habis")
    nama = input("Nama peminjam: ").strip()
    terlambat = 0
    peminjaman.append({"peminjam": nama, "kode": kode, "terlambat": terlambat})
    katalog[:] = [{**x, "stok": x["stok"] - 1} if x["kode"] == kode else x for x in katalog]
    print("Peminjaman berhasil dicatat.")


def cari_buku():
    kata = input("Judul/kata kunci: ").strip().lower()
    hasil = saring(katalog, lambda x: kata in x["judul"].lower())
    print(hasil if hasil else "Buku tidak ditemukan.")


def kelompok_kategori():
    hasil = kelompokkan(katalog, lambda x: x["kategori"])
    for kategori, daftar in hasil.items():
        print(f"\\n{kategori}:")
        for buku in daftar:
            print("-", buku["judul"], "| stok", buku["stok"])


def daftar_denda():
    hasil = pipe(peminjaman, lambda data: urutkan(data, kunci=denda_pinjam, terbalik=True))
    for item in hasil:
        print(item["peminjam"], "-", rupiah(denda_pinjam(item)))


def menu():
    while True:
        print("\\n=== PERPUSTAKAAN MINI ===")
        print("1. Katalog | 2. Pinjam buku | 3. Cari buku")
        print("4. Kelompokkan kategori | 5. Daftar denda | 0. Keluar")
        pilihan = input("Pilih: ").strip()
        try:
            if pilihan == "1":
                tampilkan_katalog()
            elif pilihan == "2":
                pinjam_buku()
            elif pilihan == "3":
                cari_buku()
            elif pilihan == "4":
                kelompok_kategori()
            elif pilihan == "5":
                daftar_denda()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak tersedia.")
        except ValueError as error:
            print("Kesalahan:", error)


if __name__ == "__main__":
    menu()
