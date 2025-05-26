from datetime import datetime

# Struktur Data
MAX = 100
data_parkiran = [None] * MAX
jumlah_kendaraan = 0

class Kendaraan:
    def __init__(self, plat_nomor, jenis_kendaraan, jam_masuk, jam_keluar=None):
        self.plat_nomor = plat_nomor
        self.jenis_kendaraan = jenis_kendaraan
        self.jam_masuk = jam_masuk
        self.jam_keluar = jam_keluar
        self.biaya = 0

def plat_unik(plat_nomor):
    for i in range(jumlah_kendaraan):
        if data_parkiran[i].plat_nomor == plat_nomor and data_parkiran[i].jam_keluar is None:
            return False
    return True

def tambah_kendaraan(plat_nomor, jenis_kendaraan, jam_masuk):
    global jumlah_kendaraan
    if jumlah_kendaraan >= MAX:
        return "Kapasitas parkir penuh!"
    if not plat_unik(plat_nomor):
        return "Plat nomor sudah terdaftar!"
    data_parkiran[jumlah_kendaraan] = Kendaraan(plat_nomor, jenis_kendaraan, jam_masuk)
    jumlah_kendaraan += 1
    return "Data valid dan telah disimpan."

def tampilkan_kendaraan():
    if jumlah_kendaraan == 0:
        return "Tidak ada kendaraan yang terdaftar."
    daftar = ""
    for i in range(jumlah_kendaraan):
        k = data_parkiran[i]
        daftar += f"{i+1}. Plat: {k.plat_nomor}, Jenis: {k.jenis_kendaraan}, Masuk: {k.jam_masuk}, "
        if k.jam_keluar:
            daftar += f"Keluar: {k.jam_keluar}, Biaya: Rp{k.biaya}\n"
        else:
            daftar += "Status: Masih Parkir\n"
    return daftar

def cari_kendaraan(plat_nomor):
    for i in range(jumlah_kendaraan):
        k = data_parkiran[i]
        if k.plat_nomor == plat_nomor and k.jam_keluar is None:
            return k
    return None

def hitung_durasi(jam_masuk, jam_keluar):
    fmt = "%H:%M:%S"
    masuk = datetime.strptime(jam_masuk, fmt)
    keluar = datetime.strptime(jam_keluar, fmt)
    durasi = keluar - masuk
    return durasi.seconds // 60

def hitung_biaya(jam_masuk, jam_keluar, tarif_biaya):
    durasi = hitung_durasi(jam_masuk, jam_keluar)
    total_jam = max(1, durasi // 60)
    if total_jam <= 15:
        return tarif_biaya
    else:
        denda = (total_jam - 15) * 1000
        return tarif_biaya + denda

def set_keluar(plat_nomor, jam_keluar):
    k = cari_kendaraan(plat_nomor)
    if k:
        k.jam_keluar = jam_keluar
        tarif = 3000 if k.jenis_kendaraan.lower() == "motor" else 5000
        k.biaya = hitung_biaya(k.jam_masuk, jam_keluar, tarif)
        return (
            f"Kendaraan keluar:\n"
            f"Plat: {k.plat_nomor}, Jenis: {k.jenis_kendaraan}\n"
            f"Masuk: {k.jam_masuk}, Keluar: {k.jam_keluar}\n"
            f"Biaya: Rp{k.biaya}"
        )
    else:
        return "Kendaraan tidak ditemukan atau sudah keluar."

def insertion_sort_durasi():
    for i in range(1, jumlah_kendaraan):
        temp = data_parkiran[i]
        j = i - 1
        durasi_temp = hitung_durasi(temp.jam_masuk, temp.jam_keluar or "23:59:59")
        while j >= 0:
            durasi_j = hitung_durasi(data_parkiran[j].jam_masuk, data_parkiran[j].jam_keluar or "23:59:59")
            if durasi_j > durasi_temp:
                data_parkiran[j + 1] = data_parkiran[j]
                j -= 1
            else:
                lanjut = False
        data_parkiran[j + 1] = temp

def cari_kendaraan_sequential(plat_nomor):
    for i in range(jumlah_kendaraan):
        k = data_parkiran[i]
        if k.plat_nomor.lower() == plat_nomor.lower() and k.jam_keluar is None:
            return f"Ditemukan:\nPlat: {k.plat_nomor}, Jenis: {k.jenis_kendaraan}, Masuk: {k.jam_masuk}"
    return "Kendaraan tidak ditemukan."

# Tampilkan menu hanya sekali
print("===== SMART PARKIR =====")
print("1. Tambah Kendaraan Masuk")
print("2. Proses Kendaraan Keluar")
print("3. Tampilkan Daftar Kendaraan")
print("4. Cari Plat Nomor (Masih Parkir)")
print("5. Urutkan Durasi Parkir (Ascending)")
print("6. Keluar")

# Program utama
selesai = False
while not selesai:
    pilihan = input("\nPilih menu (1-6): ")

    if pilihan == "1":
        plat = input("Masukkan plat nomor: ")
        jenis = input("Jenis kendaraan (motor/mobil): ")
        jam_masuk = input("Jam masuk (Jam:Menit:Detik): ")
        hasil = tambah_kendaraan(plat, jenis, jam_masuk)
        print(hasil)

    elif pilihan == "2":
        plat = input("Masukkan plat nomor kendaraan: ")
        jam_keluar = input("Masukkan jam keluar (Jam:Menit:Detik): ")
        print(set_keluar(plat, jam_keluar))

    elif pilihan == "3":
        print("\n---- Daftar Kendaraan ----")
        print(tampilkan_kendaraan())

    elif pilihan == "4":
        plat = input("Masukkan plat nomor yang ingin dicari: ")
        print(cari_kendaraan_sequential(plat))

    elif pilihan == "5":
        insertion_sort_durasi()
        print("\n---- Data Diurutkan Berdasarkan Durasi Parkir (Ascending) ----")
        print(tampilkan_kendaraan())

    elif pilihan == "6":
        print("Terima kasih. Program selesai.")
        selesai = True

    else:
        print("Pilihan tidak valid.")











