"""Pengujian unit untuk seluruh fungsi fp1lib.py."""

import pytest
from fp1lib import (
    pipe, ambil, saring, cari, urutkan, kelompokkan,
    jumlahkan, rata_rata, validasi, rupiah
)


def test_pipe():
    assert pipe(3, lambda x: x + 2, lambda x: x * 4) == 20


def test_ambil():
    assert ambil([1, 2, 3, 4], 2) == [1, 2]


def test_saring():
    assert saring([1, 2, 3, 4], lambda x: x % 2 == 0) == [2, 4]


def test_cari():
    assert cari([1, 3, 5], lambda x: x > 3) == 5
    assert cari([1, 3], lambda x: x > 8) is None


def test_urutkan_tidak_mengubah_data_asli():
    data = [3, 1, 2]
    hasil = urutkan(data)
    assert hasil == [1, 2, 3]
    assert data == [3, 1, 2]


def test_kelompokkan():
    data = [{"kelas": "A"}, {"kelas": "B"}, {"kelas": "A"}]
    hasil = kelompokkan(data, lambda x: x["kelas"])
    assert len(hasil["A"]) == 2
    assert len(hasil["B"]) == 1


def test_jumlahkan():
    assert jumlahkan([1, 2, 3]) == 6
    assert jumlahkan([{"n": 2}, {"n": 4}], lambda x: x["n"]) == 6


def test_rata_rata():
    assert rata_rata([2, 4, 6]) == 4
    assert rata_rata([]) == 0


def test_validasi():
    assert validasi(5, lambda x: x > 0) == 5
    with pytest.raises(ValueError):
        validasi(-1, lambda x: x > 0, "Harus positif")


def test_rupiah():
    assert rupiah(15000) == "Rp15.000"
    assert rupiah(1250000) == "Rp1.250.000"
