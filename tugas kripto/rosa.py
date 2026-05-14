import hashlib

# Dictionary untuk menyimpan data (sebagai simulasi database)
# Format: {'username': 'hashed_password'}
database_user = {}

def hash_sha256(password):
    """Fungsi untuk mengubah string password menjadi hash SHA-256."""
    # Encode password ke bentuk byte, lalu di-hash, dan diubah ke format hexadecimal
    return hashlib.sha256(password.encode()).hexdigest()

def registrasi():
    print("\n=== MENU REGISTRASI ===")
    username = input("Masukkan Username baru: ")
    
    # Cek apakah username sudah ada
    if username in database_user:
        print("Gagal: Username sudah terdaftar!")
        return

    password = input("Masukkan Password baru: ")
    
    # 1. Mengubah password menjadi hash SHA-256
    hashed_password = hash_sha256(password)
    
    # 2. Menyimpan username dan hash password ke "database"
    database_user[username] = hashed_password
    
    print("\n[+] Registrasi Berhasil!")
    # 3. Menampilkan hasil Hash Password
    print(f"[+] Hasil Hash Password Anda: {hashed_password}")

def login():
    print("\n=== MENU LOGIN ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    # 1. Melakukan login dan memverifikasi username
    if username in database_user:
        # 2. Memverifikasi password login dengan mencocokkan hash-nya
        input_hash = hash_sha256(password)
        
        if input_hash == database_user[username]:
            # 3. Menampilkan status login
            print(f"\n[Status] Login Berhasil! Selamat datang, {username}.")
        else:
            print("\n[Status] Login Gagal! Password yang Anda masukkan salah.")
    else:
        print("\n[Status] Login Gagal! Username tidak ditemukan.")

# --- Program Utama (Main Loop) ---
while True:
    print("\n" + "="*25)
    print(" APLIKASI SISTEM LOGIN ")
    print("="*25)
    print("1. Registrasi User")
    print("2. Login User")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == '1':
        registrasi()
    elif pilihan == '2':
        login()
    elif pilihan == '3':
        print("Keluar dari program. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")