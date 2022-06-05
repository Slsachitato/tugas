import time

# Kesempatan
kesempatan = 1
print("\nKamu memiliki", kesempatan,"kesempatan untuk mengerjakan soal ini.\nKerjakan dengan sebaik-baiknya!!!\n")

# Score
score = 0
print("------------------------------------------")
print("""|  Nama Mahasiswa  |  Mata Kuliah    
|  Anissa          |  Literasi Digital
|  Amira           |  Struktur Data
|  Bunga           |  Matematika Diskrit
|  Roman           |  Arsikom""")
print('------------------------------------------\n')

print("""R adalah relasi yang menghubungkan nama siswa dan mata pelajaran yang disukainya sesuai dengan tabel di atas, yakni R = {(Anissa, Struktur Data),(Anissa, Matematika Diskrit), (Amira, Struktur Data), (Amira, Literasi Digital), (Bunga, Literasi Digital), (Roman, Arsikom)}\n""")

# Pertanyaan dan jawaban
pertanyaan_1 = print("1. Pernyataan diatas yang tidak tepat adalah...\n\n(A). Anissa~R~Matematika Diskrit\n(B). Vilsen R Arsikom\n(C). (Roman, Arsikom) ∈ R\n(D). (Amira, Literasi Digital) ∉ R\n(E). (Bunga, Struktur Data) ∉ R\n")
jawaban_1 = "D"

for i in range (kesempatan):
    jawaban = input("Masukkan jawaban anda (A,B,C,D,E) : ")
    if jawaban.upper() == jawaban_1:
        print("Jawaban anda benar\n")
        score += 10
        break
    else:
        print("Jawaban anda salah\n")
        print("Jawabannya adalah", jawaban_1, "\n\n")

time.sleep(1)
pertanyaan_2 = print("2. Banyaknya relasi yang mungkin dari himpunan A ke himpunan B jika A memiliki 4 anggota dan B memiliki 3 anggota adalah...\n\nA. 16\nB. 64\nC. 1.024\nD. 4.096\nE. 16.384\n")
jawaban_2 = "D"

for i in range (kesempatan):
    jawaban = input("Masukkan jawaban anda (A,B,C,D,E) : ")
    if jawaban.upper() == jawaban_2:
        print("Jawaban anda benar\n")
        score += 10
        break
    else:
        print("Jawaban anda salah\n")
        print("Jawabannya adalah", jawaban_2, "\n\n")

time.sleep(1)
pertanyaan_3 = print("3. Dari relasi di bawah ini, manakah relasi yang refleksif pada himpunan bilangan bulat positif N ?\n\n(A). R : x lebih kecil dari y\n(B). S:x+y=7\n(C). T:2x+y= 10\n(D). U : x − y = 0\n(E). V : x faktor prima dari y\n")
jawaban_3 = "D"

for i in range (kesempatan):
    jawaban = input("Masukkan jawaban anda (A,B,C,D,E) : ")
    if jawaban.upper() == jawaban_3:
        print("Jawaban anda benar\n")
        score += 10
        break
    else:
        print("Jawaban anda salah\n")
        print("Jawabannya adalah", jawaban_3, "\n\n")

time.sleep(1)
pertanyaan_4 = print("4. Dari defenisi di bawaHh ini, manakah yang merupakan defenisi dan ingkaran ?\n\n(A). Implikasi p -› q bernilai benar jika anteseden salah atau konsekuen benar\n(B). Pernyataan yang bernilai benar hanya jika komponen-komponennya bernilai sama\n(C). Pernyataan yang bernilai benar, jika pernyataan semula salah, dan sebaliknya\n(D). Suatu pernyataann bernilai benar apabila paling sedikit satu komponennya bernilai benar\n")
jawaban_4 = "C"

for i in range (kesempatan):
    jawaban = input("Masukkan jawaban anda (A,B,C,D,E) : ")
    if jawaban.upper() == jawaban_4:
        print("Jawaban anda benar\n")
        score += 10
        break
    else:
        print("Jawaban anda salah\n")
        print("Jawabannya adalah", jawaban_4, "\n\n")

time.sleep(1)
pertanyaan_5 = print("5. Bila size dari suatu graf adalah n, maka jumlah derajat grafnya adalah\n(A). 2n-1\n(C). 2n\n(B). 2 (n-1)\n(D). 2n+1\n")
jawaban_5 = "B"

for i in range (kesempatan):
    jawaban = input("Masukkan jawaban anda (A,B,C,D,E) : ")
    if jawaban.upper() == jawaban_5:
        print("Jawaban anda benar\n")
        score += 10
        break
    else:
        print("Jawaban anda salah\n")
        print("Jawabannya adalah", jawaban_5, "\n\n")

time.sleep(1)
pertanyaan_6 = print("""6. Tentukan apakah argumen berikut di bawah ini valid atau tidak!
Jika saya pergi ke bioskop, saya tidak akan menyelesaikan PR saya.
Jika saya tidak menyelesaikan PR saya, saya tidak akan berhasil pada ujian besok.
∴ Jika saya pergi ke bioskop, saya tidak akan berhasil pada ujian besok\n""")
jawaban_6 = "valid"

for i in range (kesempatan):
    jawaban = input("Masukkan jawaban anda (valid/tidak) : ")
    if jawaban.lower() == jawaban_6:
        print("Jawaban anda benar\n")
        score += 10
        break
    else:
        print("Jawaban anda salah\n")
        print("Jawabannya adalah", jawaban_6, "\n\n")

time.sleep(1)
pertanyaan_7 = print("7. Pernyataan gabungan dari dua per- nyataan dengan kata penghubung atau, disebut?\n")
jawaban_7 = "disjungsi"

for i in range (kesempatan):
    jawaban = input("Masukkan jawaban anda : ")
    if jawaban.lower() == jawaban_7:
        print("Jawaban anda benar\n")
        score += 10
        break
    else:
        print("Jawaban anda salah\n")
        print("Jawabannya adalah", jawaban_7, "\n\n")

time.sleep(1)
pertanyaan_8 = print("8. Algoritma Welch-Powell digunakan untuk mencari\n")
jawaban_8 = "bilangan kromatik"

for i in range (kesempatan):
    jawaban = input("Masukkan jawaban anda : ")
    if jawaban.lower() == jawaban_8:
        print("Jawaban anda benar\n")
        score += 10
        break
    else:
        print("Jawaban anda salah\n")
        print("Jawabannya adalah", jawaban_8, "\n\n")

time.sleep(1)
pertanyaan_9 = print("9. Apa yg dimaksud Binary Tree?\n")
jawaban_9 = "suatu tree yang mempunyai cabang/anak selalu 2"

for i in range (kesempatan):
    jawaban = input("Masukkan jawaban anda : ")
    if jawaban.lower() == jawaban_9:
        print("Jawaban anda benar\n")
        score += 10
        break
    else:
        print("Jawaban anda salah\n")
        print("Jawabannya adalah", jawaban_9, "\n\n")

time.sleep(1)
pertanyaan_10 = print("10. Pencarian ruang solusi dengan menggunakan stack disebut juga?\n")
jawaban_10 = "depth first search"

for i in range (kesempatan):
    jawaban = input("Masukkan jawaban anda : ")
    if jawaban.lower() == jawaban_10:
        print("Jawaban anda benar\n")
        score += 10
        break
    else:
        print("Jawaban anda salah\n")
        print("Jawabannya adalah", jawaban_10, "\n\n")

# Total Score
time.sleep(1)
if score >= 75:
    print("Score kamu adalah", score)
else:
    print("Score kamu adalah", score, "tingkatkan lagi belajarmu")

print("\n")
close = input("Tekan ENTER untuk keluar")