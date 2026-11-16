"""Aplikasi 1: Kasir Kantin."""

from fp1lib import pipe, ambil, saring, cari, urutkan, jumlahkan, validasi, rupiah

menu_makanan = [
    {"kode": "M01", "nama": "Nasi Goreng", "harga": 15000},
    {"kode": "M02", "nama": "Mie Ayam", "harga": 12000},
    {"kode": "M03", "nama": "Ayam Geprek", "harga": 18000},
    {"kode": "D01", "nama": "Es Teh", "harga": 5000},
    {"kode": "D02", "nama": "Air Mineral", "harga": 4000},
]

keranjang = [
    {"kode": "M01", "nama": "Nasi Goreng", "harga": 15000, "jumlah": 2},
    {"kode": "D01", "nama": "Es Teh", "harga": 5000, "jumlah": 1},
]


def total_item(item):
    return item["harga"] * item["jumlah"]


def tampilkan_menu():
    print("\\n--- MENU KANTIN ---")
    for item in ambil(menu_makanan, 100):
        print(f'{item["kode"]} | {item["nama"]:<15} | {rupiah(item["harga"])}')


def tampilkan_keranjang():
    print("\\n--- KERANJANG ---")
    hasil = pipe(keranjang, lambda data: saring(data, lambda x: x["jumlah"] > 0))
    for item in ambil(hasil, 100):
        print(f'{item["nama"]} x{item["jumlah"]} = {rupiah(total_item(item))}')
    print("Total belanja:", rupiah(jumlahkan(hasil, total_item)))


def tambah_pesanan():
    kode = input("Kode menu: ").strip().upper()
    menu = cari(menu_makanan, lambda x: x["kode"] == kode)
    validasi(menu, lambda x: x is not None, "Kode menu tidak ditemukan")
    jumlah = validasi(int(input("Jumlah: ")), lambda x: x > 0, "Jumlah harus lebih dari 0")

    ada = cari(keranjang, lambda x: x["kode"] == kode)
    if ada:
        # Membuat daftar baru agar perubahan data dilakukan secara terkontrol.
        keranjang[:] = [
            {**x, "jumlah": x["jumlah"] + jumlah} if x["kode"] == kode else x
            for x in keranjang
        ]
    else:
        keranjang.append({**menu, "jumlah": jumlah})
    print("Pesanan ditambahkan.")


def cari_menu():
    kata = input("Nama menu yang dicari: ").strip().lower()
    hasil = cari(menu_makanan, lambda x: kata in x["nama"].lower())
    print(hasil if hasil else "Menu tidak ditemukan.")


def urutkan_keranjang():
    hasil = urutkan(keranjang, kunci=total_item, terbalik=True)
    for item in hasil:
        print(item["nama"], "-", rupiah(total_item(item)))


def menu():
    while True:
        print("\\n=== KASIR KANTIN ===")
        print("1. Lihat menu | 2. Lihat keranjang | 3. Tambah pesanan")
        print("4. Cari menu | 5. Urutkan belanja terbesar | 0. Keluar")
        pilihan = input("Pilih: ").strip()
        try:
            if pilihan == "1":
                tampilkan_menu()
            elif pilihan == "2":
                tampilkan_keranjang()
            elif pilihan == "3":
                tambah_pesanan()
            elif pilihan == "4":
                cari_menu()
            elif pilihan == "5":
                urutkan_keranjang()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak tersedia.")
        except (ValueError, TypeError) as error:
            print("Kesalahan:", error)


if __name__ == "__main__":
    menu()
