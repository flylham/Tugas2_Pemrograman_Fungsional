"""Aplikasi 4: Keuangan Pribadi."""

from fp1lib import pipe, ambil, saring, urutkan, kelompokkan, jumlahkan, rata_rata, validasi, rupiah

transaksi = [
    {"keterangan": "Uang saku", "jenis": "Pemasukan", "kategori": "Bulanan", "nominal": 1500000},
    {"keterangan": "Makan", "jenis": "Pengeluaran", "kategori": "Makanan", "nominal": 25000},
    {"keterangan": "Transportasi", "jenis": "Pengeluaran", "kategori": "Transportasi", "nominal": 15000},
    {"keterangan": "Freelance", "jenis": "Pemasukan", "kategori": "Pekerjaan", "nominal": 300000},
]


def tampilkan():
    print("\\n--- RIWAYAT KEUANGAN ---")
    for item in ambil(transaksi, 100):
        print(f'{item["keterangan"]} | {item["jenis"]} | {item["kategori"]} | {rupiah(item["nominal"])}')


def tambah_transaksi():
    keterangan = input("Keterangan: ").strip()
    jenis = input("Jenis (Pemasukan/Pengeluaran): ").strip().title()
    validasi(jenis, lambda x: x in ("Pemasukan", "Pengeluaran"), "Jenis transaksi tidak valid")
    kategori = input("Kategori: ").strip().title()
    nominal = validasi(int(input("Nominal rupiah: ")), lambda x: x > 0, "Nominal harus lebih dari 0")
    transaksi.append({"keterangan": keterangan, "jenis": jenis, "kategori": kategori, "nominal": nominal})
    print("Transaksi berhasil ditambahkan.")


def ringkasan():
    pemasukan = saring(transaksi, lambda x: x["jenis"] == "Pemasukan")
    pengeluaran = saring(transaksi, lambda x: x["jenis"] == "Pengeluaran")
    total_masuk = jumlahkan(pemasukan, lambda x: x["nominal"])
    total_keluar = jumlahkan(pengeluaran, lambda x: x["nominal"])
    print("Total pemasukan :", rupiah(total_masuk))
    print("Total pengeluaran:", rupiah(total_keluar))
    print("Saldo            :", rupiah(total_masuk - total_keluar))
    print("Rata-rata transaksi:", rupiah(rata_rata(transaksi, lambda x: x["nominal"])))


def rekap_kategori():
    hasil = pipe(transaksi, lambda data: kelompokkan(data, lambda x: x["kategori"]))
    for kategori, daftar in hasil.items():
        total = jumlahkan(daftar, lambda x: x["nominal"])
        print(kategori, "-", len(daftar), "transaksi -", rupiah(total))


def urut_nominal():
    hasil = urutkan(transaksi, kunci=lambda x: x["nominal"], terbalik=True)
    for item in hasil:
        print(item["keterangan"], "-", rupiah(item["nominal"]))


def menu():
    while True:
        print("\\n=== KEUANGAN PRIBADI ===")
        print("1. Tampilkan transaksi | 2. Tambah transaksi | 3. Ringkasan")
        print("4. Rekap kategori | 5. Urut nominal | 0. Keluar")
        pilihan = input("Pilih: ").strip()
        try:
            if pilihan == "1":
                tampilkan()
            elif pilihan == "2":
                tambah_transaksi()
            elif pilihan == "3":
                ringkasan()
            elif pilihan == "4":
                rekap_kategori()
            elif pilihan == "5":
                urut_nominal()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak tersedia.")
        except ValueError as error:
            print("Kesalahan:", error)


if __name__ == "__main__":
    menu()
