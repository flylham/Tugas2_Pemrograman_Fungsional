"""Aplikasi 5: Nilai Mahasiswa."""

from fp1lib import pipe, ambil, saring, cari, urutkan, jumlahkan, rata_rata, validasi

mahasiswa = [
    {"nim": "2024001", "nama": "Alya", "tugas": 85, "uts": 80, "uas": 90},
    {"nim": "2024002", "nama": "Bima", "tugas": 70, "uts": 75, "uas": 72},
    {"nim": "2024003", "nama": "Citra", "tugas": 90, "uts": 88, "uas": 95},
    {"nim": "2024004", "nama": "Doni", "tugas": 60, "uts": 65, "uas": 68},
]


def nilai_akhir(data):
    return data["tugas"] * 0.3 + data["uts"] * 0.3 + data["uas"] * 0.4


def grade(data):
    nilai = nilai_akhir(data)
    if nilai >= 85:
        return "A"
    if nilai >= 75:
        return "B"
    if nilai >= 65:
        return "C"
    if nilai >= 50:
        return "D"
    return "E"


def tampilkan(data=None):
    daftar = data if data is not None else mahasiswa
    print("\\n--- NILAI MAHASISWA ---")
    for mhs in ambil(daftar, 100):
        print(f'{mhs["nim"]} | {mhs["nama"]:<8} | Nilai: {nilai_akhir(mhs):.1f} | Grade: {grade(mhs)}')


def tambah_nilai():
    nim = input("NIM: ").strip()
    nama = input("Nama: ").strip()
    tugas = validasi(float(input("Nilai tugas: ")), lambda x: 0 <= x <= 100, "Nilai harus 0-100")
    uts = validasi(float(input("Nilai UTS: ")), lambda x: 0 <= x <= 100, "Nilai harus 0-100")
    uas = validasi(float(input("Nilai UAS: ")), lambda x: 0 <= x <= 100, "Nilai harus 0-100")
    validasi(nim, lambda x: x.isdigit() and len(x) >= 5, "NIM tidak valid")
    mahasiswa.append({"nim": nim, "nama": nama, "tugas": tugas, "uts": uts, "uas": uas})
    print("Nilai mahasiswa ditambahkan.")


def cari_mahasiswa():
    nim = input("Masukkan NIM: ").strip()
    hasil = cari(mahasiswa, lambda x: x["nim"] == nim)
    tampilkan([hasil] if hasil else [])
    if hasil is None:
        print("Mahasiswa tidak ditemukan.")


def peringkat():
    hasil = pipe(mahasiswa, lambda data: urutkan(data, kunci=nilai_akhir, terbalik=True))
    for nomor, mhs in enumerate(hasil, start=1):
        print(f'{nomor}. {mhs["nama"]} - {nilai_akhir(mhs):.1f} ({grade(mhs)})')


def statistik():
    lulus = saring(mahasiswa, lambda x: nilai_akhir(x) >= 60)
    print("Rata-rata kelas:", f"{rata_rata(mahasiswa, nilai_akhir):.2f}")
    print("Jumlah mahasiswa:", len(mahasiswa))
    print("Jumlah lulus:", jumlahkan(lulus, lambda x: 1))


def menu():
    while True:
        print("\\n=== NILAI MAHASISWA ===")
        print("1. Tampilkan nilai | 2. Tambah nilai | 3. Cari mahasiswa")
        print("4. Peringkat | 5. Statistik kelas | 0. Keluar")
        pilihan = input("Pilih: ").strip()
        try:
            if pilihan == "1":
                tampilkan()
            elif pilihan == "2":
                tambah_nilai()
            elif pilihan == "3":
                cari_mahasiswa()
            elif pilihan == "4":
                peringkat()
            elif pilihan == "5":
                statistik()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak tersedia.")
        except ValueError as error:
            print("Kesalahan:", error)


if __name__ == "__main__":
    menu()
