# Program Cek Kelulusan Ujian Matematika

nama = input("Masukkan nama mahasiswa: ")

# menentukan target nilai sesuai nama
if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    target = 0
    print("Nama tidak terdaftar")

if target != 0:
    print("Target nilai", nama, ":", target)

    percobaan = 0
    lulus = False

    while percobaan < 3 and lulus == False:
        percobaan = percobaan + 1
        nilai = int(input("Nilai " + str(percobaan) + " : "))

        if nilai >= target:
            lulus = True
        else:
            if percobaan < 3:
                print("Nilai belum mencapai target, ikut remedial!")

    print()
    if lulus:
        print(nama, "berhasil lulus setelah", percobaan, "kali percobaan!")
    else:
        print(nama, "tidak lulus setelah 3 kali percobaan!")