# Sistem Pengelolaan Stok Barang Toko

# 1. Input data
nama_barang = input("Masukkan nama barang: ")
stok = int(input("Masukkan jumlah stok awal: "))

# 5. Perulangan agar transaksi bisa berkali-kali
while True:
    # 2. Pilih transaksi
    print("\n=== MENU TRANSAKSI ===")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Selesai")
    pilihan = input("Pilih transaksi (1/2/3): ")

    # 3. Proses transaksi (percabangan)
    if pilihan == "1":
        jumlah = int(input("Jumlah barang masuk: "))
        stok += jumlah
        print("Stok berhasil ditambah.")

    elif pilihan == "2":
        jumlah = int(input("Jumlah barang keluar: "))
        # 4. Cek stok
        if jumlah > stok:
            print("Stok Tidak Mencukupi")
        else:
            stok -= jumlah
            print("Stok berhasil dikurangi.")

    elif pilihan == "3":
        break

    else:
        print("Pilihan tidak valid!")

    # 6. Tampilkan hasil
    print(f"Stok {nama_barang} saat ini: {stok}")

print(f"\nStok terakhir {nama_barang}: {stok}")
print("Terima kasih!")