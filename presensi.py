"""Aplikasi 2: Presensi Kelas."""

from fp1lib import pipe, ambil, saring, kelompokkan, rata_rata, validasi

data_presensi = [
    {"nim": "2024001", "nama": "Alya", "kelas": "A", "hadir": 14, "total": 16},
    {"nim": "2024002", "nama": "Bima", "kelas": "A", "hadir": 12, "total": 16},
    {"nim": "2024003", "nama": "Citra", "kelas": "B", "hadir": 15, "total": 16},
    {"nim": "2024004", "nama": "Doni", "kelas": "B", "hadir": 10, "total": 16},
]


def persentase(data):
    return data["hadir"] / data["total"] * 100 if data["total"] else 0


def tampilkan(data=None):
    daftar = data if data is not None else data_presensi
    print("\\n--- REKAP PRESENSI ---")
    for mhs in ambil(daftar, 100):
        print(f'{mhs["nim"]} | {mhs["nama"]:<8} | Kelas {mhs["kelas"]} | {persentase(mhs):.1f}%')


def tambah_presensi():
    nim = input("NIM: ").strip()
    nama = input("Nama: ").strip()
    kelas = input("Kelas: ").strip().upper()
    total = validasi(int(input("Jumlah pertemuan: ")), lambda x: x > 0, "Jumlah pertemuan harus positif")
    hadir = validasi(int(input("Jumlah hadir: ")), lambda x: 0 <= x <= total, "Jumlah hadir tidak sesuai")
    validasi(nim, lambda x: x.isdigit() and len(x) >= 5, "NIM harus berupa angka")
    data_presensi.append({"nim": nim, "nama": nama, "kelas": kelas, "hadir": hadir, "total": total})
    print("Data presensi ditambahkan.")


def rekap_per_kelas():
    hasil = pipe(data_presensi, lambda data: kelompokkan(data, lambda x: x["kelas"]))
    for kelas, daftar in hasil.items():
        rata = rata_rata(daftar, persentase)
        print(f"Kelas {kelas}: {len(daftar)} mahasiswa, rata-rata kehadiran {rata:.1f}%")


def daftar_perlu_perhatian():
    hasil = saring(data_presensi, lambda x: persentase(x) < 75)
    print("Mahasiswa dengan kehadiran di bawah 75%:")
    tampilkan(hasil)


def menu():
    while True:
        print("\\n=== PRESENSI KELAS ===")
        print("1. Tampilkan rekap | 2. Tambah data | 3. Rekap per kelas")
        print("4. Kehadiran di bawah 75% | 0. Keluar")
        pilihan = input("Pilih: ").strip()
        try:
            if pilihan == "1":
                tampilkan()
            elif pilihan == "2":
                tambah_presensi()
            elif pilihan == "3":
                rekap_per_kelas()
            elif pilihan == "4":
                daftar_perlu_perhatian()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak tersedia.")
        except ValueError as error:
            print("Kesalahan:", error)


if __name__ == "__main__":
    menu()
