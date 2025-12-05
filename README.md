# Kelompok-Prikitiw
#PROJECT TO DO LIST/TASK MANAGER

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
