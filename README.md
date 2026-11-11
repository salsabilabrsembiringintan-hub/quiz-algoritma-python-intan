# Quiz Algoritma Python - Cek Kelulusan Ujian Matematika

print("=== PROGRAM CEK KELULUSAN ===")
nama = input("Nama mahasiswa : ")

# tentukan target nilai tiap mahasiswa
if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    target = 0

if target == 0:
    print("Maaf, nama tidak ada di data")
else:
    print("Target nilai", nama, "adalah", target)
    print()

    ke = 1
    lulus = False

    # ulangi maksimal 3 kali
    while ke <= 3:
        nilai = int(input("Nilai " + str(ke) + " : "))

        if nilai >= target:
            lulus = True
            break
        else:
            if ke < 3:
                print("Belum mencapai target, harus remedial")
            ke = ke + 1

    print()
    if lulus == True:
        print(nama, "berhasil lulus setelah", ke, "kali percobaan!")
    else:
        print(nama, "tidak lulus setelah 3 kali percobaan!")