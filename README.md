
# Program cek kelulusan ujian matematika

nama = input("Nama : ").title()

# tentukan target nilai sesuai nama
if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    target = 0

if target == 0:
    print("Nama tidak terdaftar")
else:
    print("Target nilai", nama, ":", target)

    percobaan = 0
    lulus = False

    while percobaan < 3:
        percobaan = percobaan + 1
        nilai = int(input("Nilai " + str(percobaan) + " : "))

        if nilai >= target:
            lulus = True
            break   # kalau sudah lulus, berhenti

    if lulus:
        print(nama, "berhasil lulus setelah", percobaan, "kali percobaan!")
    else:
        print(nama, "tidak lulus setelah 3 kali percobaan!")