"""Library bersama untuk lima aplikasi tugas Pemrograman Fungsional."""

from functools import reduce


def pipe(data, *fungsi):
    """Menjalankan beberapa fungsi secara berurutan pada data."""
    return reduce(lambda hasil, fn: fn(hasil), fungsi, data)


def ambil(data, jumlah=5):
    """Mengambil maksimal sejumlah elemen dari awal data."""
    return list(data)[:jumlah]


def saring(data, kondisi):
    """Menghasilkan daftar elemen yang memenuhi kondisi."""
    return list(filter(kondisi, data))


def cari(data, kondisi):
    """Mengembalikan elemen pertama yang memenuhi kondisi, atau None."""
    return next((item for item in data if kondisi(item)), None)


def urutkan(data, kunci=None, terbalik=False):
    """Mengurutkan data tanpa mengubah urutan pada data asli."""
    return sorted(data, key=kunci, reverse=terbalik)


def kelompokkan(data, kunci):
    """Mengelompokkan elemen berdasarkan hasil fungsi kunci."""
    hasil = {}
    for item in data:
        kategori = kunci(item)
        hasil.setdefault(kategori, []).append(item)
    return hasil


def jumlahkan(data, kunci=lambda item: item):
    """Menjumlahkan data, atau hasil pemetaan setiap elemen."""
    return sum(kunci(item) for item in data)


def rata_rata(data, kunci=lambda item: item):
    """Menghitung rata-rata; mengembalikan 0 jika data kosong."""
    data = list(data)
    if not data:
        return 0
    return jumlahkan(data, kunci) / len(data)


def validasi(nilai, kondisi, pesan="Data tidak valid"):
    """Mengembalikan nilai jika valid, selain itu melempar ValueError."""
    if not kondisi(nilai):
        raise ValueError(pesan)
    return nilai


def rupiah(nilai):
    """Mengubah angka menjadi format mata uang Rupiah."""
    angka = f"{nilai:,.0f}".replace(",", ".")
    return f"Rp{angka}"
