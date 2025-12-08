# 🎯 To Do List / Task Manager (CLI Python)

Aplikasi sederhana berbasis Command Line Interface (CLI) yang dibuat menggunakan Python murni untuk mengelola daftar tugas harian. Aplikasi ini memiliki kemampuan untuk menyimpan dan memuat data tugas ke file teks, sehingga tugas tetap tersimpan setelah program ditutup.

## ✨ Fitur Utama

1.  *Tambah Tugas:* Memungkinkan pengguna memasukkan judul tugas baru.
2.  *Lihat Semua Tugas:* Menampilkan daftar tugas yang ada beserta statusnya (Belum Selesai / Selesai).
3.  *Edit Tugas:* Mengubah judul tugas berdasarkan nomor indeks.
4.  *Hapus Tugas:* Menghapus tugas dari daftar.
5.  *Tandai Selesai:* Mengubah status tugas menjadi 'Selesai'.
6.  *Penyimpanan Data Otomatis:*
    * *Memuat Data:* Tugas dimuat otomatis dari todolist.txt saat program dimulai.
    * *Menyimpan Data:* Tugas disimpan ke todolist.txt setiap kali pengguna memilih menu *Simpan ke File* atau saat *Keluar* dari program.
7.  *Validasi Input & Error Handling:* Program dilengkapi dengan penanganan kesalahan (try-except) untuk memastikan input pengguna adalah angka yang valid dan berada dalam rentang nomor tugas yang tersedia.

## 🛠 Konsep Programming yang Digunakan

| Konsep Python | Implementasi |
| :--- | :--- |
| *Collection Framework* | Menggunakan list untuk menampung semua tugas, di mana setiap tugas adalah sebuah dictionary. |
| *Struktur Data* | Menggunakan dictionary ({"judul": ..., "status": ...}) untuk menyimpan detail setiap tugas. |
| *Modularitas* | Program dibagi menjadi beberapa fungsi (tambah_tugas, lihat_tugas, dll.) agar kode lebih terorganisir. |
| *Perulangan* | Menggunakan while True untuk menjalankan menu program utama secara berulang. |
| *File I/O* | Menggunakan fungsi open() dan with open() dalam mode baca ("r") dan tulis ("w") untuk persistensi data pada file todolist.txt. |
| *Error Handling* | Menggunakan try-except untuk menangani kesalahan umum seperti ValueError (input non-angka) dan FileNotFoundError. |
| *Helper Function* | Menggunakan fungsi pembantu (_get_valid_task_index) untuk mengurangi duplikasi kode dan memusatkan logika validasi input. |

## 🚀 Cara Menjalankan Program

1.  Pastikan Anda telah menginstal *Python 3* di sistem Anda.
2.  Simpan kode program ke dalam sebuah file, misalnya todo_app.py.
3.  Buka terminal atau Command Prompt.
4.  Jalankan perintah:
    bash
    python todo_app.py
    
5.  Program akan menampilkan menu utama, dan Anda bisa mulai mengelola tugas Anda.
