# ========================== TO DO LIST / TASK MANAGER ==========================

tasks = []  # Collection Framework (List)

# ============================== FUNGSI PROGRAM =================================

def show_menu():
    print("\n=== PROGRAM TO DO LIST / TASK MANAGER ===")
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Edit Tugas")
    print("4. Hapus Tugas")
    print("5. Tandai Tugas Selesai")
    print("6. Simpan ke File")
    print("7. Keluar")

def tambah_tugas():
    judul = input("Masukkan nama tugas: ")
    task = {"judul": judul, "status": "Belum Selesai"}
    tasks.append(task)
    print("Tugas berhasil ditambahkan!")

def lihat_tugas():
    if len(tasks) == 0:
        print("Belum ada tugas yang ditambahkan.")
    else:
        print("\n--- Daftar Tugas ---")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['judul']} - {task['status']}")

def edit_tugas():
    lihat_tugas()
    try:
        index = int(input("Pilih nomor tugas yang ingin diedit: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Masukkan judul baru: ")
            tasks[index]["judul"] = new_title  # Operasi String
            print("Tugas berhasil diperbarui.")
        else:
            print("Nomor tugas tidak valid!")
    except ValueError:
        print("Input harus angka!")

def hapus_tugas():
    lihat_tugas()
    try:
        index = int(input("Pilih nomor tugas yang ingin dihapus: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Tugas berhasil dihapus!")
        else:
            print("Nomor tugas tidak valid!")
    except:
        print("Terjadi kesalahan saat menghapus tugas!")

def selesai_tugas():
    lihat_tugas()
    try:
        index = int(input("Pilih tugas yang sudah selesai: ")) - 1
        tasks[index]["status"] = "Selesai"
        print("Tugas berhasil ditandai selesai!")
    except:
        print("Nomor tidak valid!")

def simpan_ke_file():
    file_name = "todolist.txt"
    try:
        with open(file_name, "w") as file:
            for task in tasks:
                file.write(f"{task['judul']} - {task['status']}\n")
        print(f"Tugas disimpan ke file {file_name}")
    except:
        print("Gagal menyimpan data ke file!")

# =============================== PROGRAM UTAMA ================================

while True:  # Perulangan
    show_menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_tugas()
    elif pilihan == "2":
        lihat_tugas()
    elif pilihan == "3":
        edit_tugas()
    elif pilihan == "4":
        hapus_tugas()
    elif pilihan == "5":
        selesai_tugas()
    elif pilihan == "6":
        simpan_ke_file()
    elif pilihan == "7":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")

