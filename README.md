# Rental Mobil App

Sistem manajemen rental mobil berbasis terminal (CLI) yaitu antarmuka berbasis teks, yang dibuat dengan Python.  
Dirancang untuk membantu petugas atau admin rental dalam mengelola data mobil, pelanggan, dan transaksi penyewaan.

---

## Fitur Utama

-  Tambah, lihat, edit, dan hapus data mobil
-  Sewa mobil dengan input pelanggan baru atau lama
-  Hitung total biaya sewa & validasi pembayaran
-  Kelola data pelanggan dan peminjaman
-  Antarmuka berbasis teks (console)

---

## Struktur Data

Program menggunakan 3 struktur data utama berupa list:

| Nama List           | Deskripsi                                         | Format                                  |
|---------------------|--------------------------------------------------|-----------------------------------------|
| `listData`          | Daftar mobil dalam sistem                        | `[merk, nama, tahun, plat, harga, status]` |
| `listDataCustomer`  | Data pelanggan                                    | `[nama, alamat, nomor KTP, status]`     |
| `listDataPeminjaman`| Riwayat transaksi peminjaman                     | `[nama, KTP, merk, nama, tahun, plat, harga, durasi, total]` |

---

Reyhan Kurniawan (JCDS 2702)
