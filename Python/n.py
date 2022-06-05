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
elif user =='d' or 'D':
    print('Selamat Jawaban Anda BENAR!!!!')
elif user =='E':
    print('Maaf Jawaban anda salah')
else:
    print('Keywoard yg anda masukkan salah')