import sys

print('\n')
print("""|  Nama Mahasiswa  |  Mata Kuliah    
|  Anissa          |  Literasi Digital
|  Amira           |  Struktur Data
|  Bunga           |  Matematika Diskrit
|  Roman           |  Arsikom\n""")


print('R adalah relasi yang menghubungkan nama siswa dan mata pelajaran \n yg dsukainya sesuai dengan tabel diatas, yakni \n')
print('R = {(Anissa, Struktur Data),(Anissa, Matematika Diskrit), (Amira, Struktur Data),\n(Amira, Literasi Digital), (Bunga, Literasi Digital), (Roman, Arsikom)}\n')
print("""1. Pernyataan berikut yang tidak tepat adalah..
A. Anissa~R~Matematika Diskrit
B. Vilsen R Arsikom
C. (Roman, Arsikom) ∈ R
D. (Amira, Literasi Digital) ∉ R
E. (Bunga, Struktur Data) ∉ R\n""")

user = input('Masukkan jawaban anda (Huruf Besar): ')
if user == 'A': 
    print('Maaf Jawaban Anda Salah')
elif user =='B':
    print('Maaf Jawaban Anda Salah')
elif user =='C':
    print('Maaf Jawaban anda salah')
elif user =='D':
    print('Selamat Jawaban Anda BENAR!!!!')
elif user =='E':
    print('Maaf Jawaban anda salah')
else:
    print('Keywoard yg anda masukkan salah')
print('\n')

print("""2. Banyaknya relasi yang mungkin dari himpunan A ke himpunan B jika  Amemiliki 4 anggota dan B memiliki 3 anggota adalah...
A. 16 
B. 64
C. 1.024 
E. 16.384
D. 4.096\n""")

user2 = input('Masukkan jawaban anda (Huruf Besar): ')
if user2 == 'A':
    print('Maaf Jawaban Anda Salah')
if user2 == 'B':
    print('Maaf Jawaban Anda Salah')
elif user2 == 'C':
    print('Maaf Jawaban Anda Salah')
elif user2 == 'D':
    print('Selamat Jawaban Anda BENAR!!!')
elif user2 == 'E':
    print('Maaf Jawaban Anda Salah')
else:
    print('Keywoard yg anda masukkan salah!!!')
print('\n')


print("""3. Dari relasi di bawah ini, manakah relasi yang refleksif pada himpunan bilangan bulat positif N ?
A. R : x lebih kecil dari y
B. S:x+y=7
C. T:2x+y= 10
D. U : x − y = 0
E. V : x faktor prima dari y\n""")

user3 = input('Masukkan jawaban anda (Huruf Besar): ')
if user3 == 'A':
    print('Maaf Jawaban Anda Salah')
elif user3 == 'B':
    print('Maaf Jawaban Anda Salah')
elif user3 == 'c':
    print('Maaf Jawaban Anda Salah')
elif user3 == 'D':
    print('Selamat Jawaban Anda BENAR!!!')
elif user3 == 'E':
    print('Maaf Jawaban Anda Salah')
else:
    print('Keywoard yg anda masukkan')
print('\n')

print("""4. Dari defenisi di bawah ini,manakah yang merupakan defenisi dan lingkaran.
a. Implikasi p -› q bemnilai benarikaantesedensalahataukonsekuenbenar.
b. Pernyataan yang bernilai benar hanya jika komponen-komponennya bernilai sama.
C. peryataan yanq bernilai benar, jika pernyataan semula salah,dan sebaliknya.
d. Suatu pernyataann bernilai benar apabila paling sedikit satu komponennya bernilai benar.\n""")

user4 = input('Masukkan jawaban anda (Huruf Besar): ')
if user4 == 'A':
    print('Maaf Jawaban Anda Salah')
elif user4 == 'B':
    print('Maaf Jawaban Anda Salah')
elif user4 == 'C':
    print('Selamat Jawaban Anda BENAR!!!')
elif user4 == 'D':
    print('Maaf Jawaban Anda Salah')
else:
    print('Keywoard yg anda masukkan')
print('\n')

print("""5. Bila size dari suatu graf adalah n, maka jumlah derajat grafnya adalah:
A. 2n-1
C. 2n
B. 2 (n-1)
D. 2n+1\n""")

user5 = input('Masukkan jawaban anda (Huruf Besar): ')
if user5 == 'A':
     print('Maaf Jawaban Anda Salah')
elif user5 == 'B':
    print('Selamat Jawaban Anda BENAR!!!')
elif user5 == 'C':
    print('Maaf Jawaban Anda Salah')
elif uuser5 == 'D':
    print('Maaf Jawaban Anda Salah')
elif user5 == 'E':
    print('Maaf Jawaban Anda Salah')
else:
    print('Keywoard yg anda masukkan salah')
print('\n')

print("""6. Tentukan apakah argumen berikut di bawah ini valid atau tidak!
Jika saya pergi ke bioskop, saya tidak akan menyelesaikan PR saya.
Jika saya tidak menyelesaikan PR saya, saya tidak akan berhasil pada ujian besok.
∴ Jika saya pergi ke bioskop, saya tidak akan berhasil pada ujian besok
Jawab
p →q
q →r
∴ p →r\n""")

user6 = input('Masukkan jawaban anda : ')
jawaban1 = 'valid'
if user6 == jawaban1:
    print('Selamat Jawaban Anda Benar!!!!')
else:
    print("Maaf jawaban anda salah...")
print('\n')

print('7. Pernyataan gabungan dari dua per- nyataan dengan kata penghubung atau, disebut?')
user7 = input('Masukkan jawaban anda : ')
jawaban2 = 'disjungsi'
if user7 == jawaban2:
    print('Selamat Jawaban Anda Benar!!!!')
else:
    print("Maaf jawaban anda salah...")
print('\n')

print('8. Kaidah dasar menghitung Kombinatorial adalah...?')
jawaban3 = 'kombinasi penjumlahan' and 'Kombinasi perkalian'
user8 = input('Masukkan jawaban anda : ')
if user8 == 'kombinasi penjumlahan':
    print('Selamat Jawaban Anda Benar!!!!')
else:
    ("Maaf jawaban anda salah...")
print('\n')

print('9. Apa yg dimaksud Binary Tree ?')
user9 = input('Masukkan jawaban anda : ')
if user9 == 'suatu tree yang mempunyai cabang/anak selalu 2':
    print('Selamat Jawaban Anda Benar!!!!')
else:
    ("Maaf jawaban anda salah...")
print('\n')

print('10. Pencarian ruang solusi dengan menggunakan stack disebut juga ?')
user10 = input('Masukkan jawaban anda : ')
if user10 == 'Depth First Search':
    print('Selamat Jawaban Anda Benar!!!!')
else:
    ("Maaf jawaban anda salah...")
print('\n')