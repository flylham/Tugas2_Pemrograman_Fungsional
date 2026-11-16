# Tugas 2 – Library Pemrograman Fungsional

Proyek ini menggunakan satu library bersama `fp1lib.py` untuk lima aplikasi terminal:
1. Kasir Kantin (`kasir.py`)
2. Presensi Kelas (`presensi.py`)
3. Perpustakaan Mini (`perpustakaan.py`)
4. Keuangan Pribadi (`keuangan.py`)
5. Nilai Mahasiswa (`nilai.py`)

## Struktur folder

```text
Tugas2_Pemrograman_Fungsional/
├── fp1lib.py
├── kasir.py
├── presensi.py
├── perpustakaan.py
├── keuangan.py
├── nilai.py
├── test_fp1lib.py
├── README.md
├── requirements.txt
└── LAPORAN.md
```

## Cara menjalankan

Pastikan Python 3 sudah terpasang. Buka terminal pada folder proyek, lalu jalankan salah satu:

```bash
python kasir.py
python presensi.py
python perpustakaan.py
python keuangan.py
python nilai.py
```

## Cara menjalankan pengujian

Pasang pytest:

```bash
python -m pip install -r requirements.txt
```

Lalu jalankan:

```bash
python -m pytest -v
```

## Daftar fungsi library

| Fungsi | Kegunaan |
|---|---|
| `pipe(data, *fungsi)` | Menjalankan fungsi secara berantai |
| `ambil(data, jumlah)` | Mengambil sejumlah elemen |
| `saring(data, kondisi)` | Memfilter elemen berdasarkan kondisi |
| `cari(data, kondisi)` | Mencari elemen pertama yang cocok |
| `urutkan(data, kunci, terbalik)` | Mengurutkan data |
| `kelompokkan(data, kunci)` | Mengelompokkan data berdasarkan kategori |
| `jumlahkan(data, kunci)` | Menjumlahkan nilai |
| `rata_rata(data, kunci)` | Menghitung nilai rata-rata |
| `validasi(nilai, kondisi, pesan)` | Memeriksa masukan |
| `rupiah(nilai)` | Memformat angka menjadi Rupiah |

## Matriks fungsi × aplikasi

Tanda centang menunjukkan fungsi benar-benar dipanggil pada file aplikasi terkait.

| Fungsi | Kasir | Presensi | Perpus | Keuangan | Nilai | Jumlah |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `pipe` | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| `ambil` | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| `saring` | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| `cari` | ✓ | – | ✓ | – | ✓ | 3 |
| `urutkan` | ✓ | – | ✓ | ✓ | ✓ | 4 |
| `kelompokkan` | – | ✓ | ✓ | ✓ | – | 3 |
| `jumlahkan` | ✓ | – | – | ✓ | ✓ | 3 |
| `rata_rata` | – | ✓ | – | ✓ | ✓ | 3 |
| `validasi` | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| `rupiah` | ✓ | – | ✓ | ✓ | – | 3 |

Seluruh fungsi digunakan oleh minimal tiga aplikasi, sesuai ketentuan pada instruksi tugas.

## Bukti pemanggilan fungsi

Contoh lokasi pemanggilan fungsi:
- `kasir.py`: `pipe()` pada `tampilkan_keranjang()`, `ambil()` pada `tampilkan_menu()`, `saring()` pada `tampilkan_keranjang()`, `cari()` pada `tambah_pesanan()` dan `cari_menu()`.
- `presensi.py`: `pipe()` dan `kelompokkan()` pada `rekap_per_kelas()`, `rata_rata()` pada perhitungan rata-rata kelas, `validasi()` pada `tambah_presensi()`.
- `perpustakaan.py`: `pipe()` dan `urutkan()` pada `daftar_denda()`, `cari()` pada pencarian buku, `kelompokkan()` pada rekap kategori.
- `keuangan.py`: `saring()`, `jumlahkan()`, dan `rata_rata()` pada `ringkasan()`, `kelompokkan()` pada `rekap_kategori()`.
- `nilai.py`: `pipe()` dan `urutkan()` pada `peringkat()`, `cari()` pada `cari_mahasiswa()`, `rata_rata()` pada `statistik()`.

## Catatan desain

Fungsi pada library dibuat sebagai fungsi umum agar dapat digunakan lintas aplikasi. Fungsi seperti `urutkan`, `saring`, dan `kelompokkan` menghasilkan koleksi baru sehingga tidak mengubah urutan atau isi daftar sumber. Data contoh disimpan di dalam masing-masing aplikasi dan dapat ditambah melalui menu terminal. Data belum disimpan secara permanen ke database atau file.
