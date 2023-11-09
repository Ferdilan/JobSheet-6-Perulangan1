print("Menghitung jumlah bilangan genap dari N bilangan")
print("------------------------------------------------")
def jumlah_rata_bilangan_genap():
    #input dari user
    n = int(input("Masukkan bilangan bulat N: "))

    # inisialisasi variabel
    total_genap = 0
    jumlah_genap = 0

    #hitung jumlah dan banyaknya bilangan genap
    for i in range(1, n + 1):
        if i % 2 == 0:
            total_genap += i
            jumlah_genap += 1

    #tampilkan hasil
    print(f"Banyaknya bilangan genap dari 1 sampai {n} adalah {jumlah_genap}.")
    print(f"Jumlah bilangan genap dari 1 sampai {n} adalah {total_genap}.")

    # Menghitung dan menampilkan rata-rata bilangan genap
    if jumlah_genap > 0:
        rata_genap = total_genap / jumlah_genap
        print(f"Rata-rata bilangan genap dari 1 sampai {n} = {rata_genap}.")
    else:
        print("Tidak ada bilangan genap di dalam range yang dimasukkan.")

# Memanggil fungsi
jumlah_rata_bilangan_genap()

# #penjelasan program

# 1. `jumlah_rata_bilangan_genap()` adalah fungsi utama yang mengandung seluruh logika program.
# 2. `N = int(input("Masukkan bilangan bulat N (N > 0): "))` meminta pengguna untuk memasukkan bilangan bulat N.
# 3. Variabel `total_genap` dan `jumlah_genap` diinisialisasi untuk menyimpan jumlah dan banyaknya bilangan genap.
# 4. Loop `for i in range(1, N + 1):` digunakan untuk iterasi dari 1 sampai N (inklusif).
# 5. Pada setiap iterasi, program memeriksa apakah `i` adalah bilangan genap dengan kondisi `if i % 2 == 0:`.
# 6. Jika i genap, maka nilai i ditambahkan ke `total_genap` dan `jumlah_genap` ditambah 1.
# 7. Setelah selesai iterasi, program menampilkan banyaknya dan jumlah bilangan genap.
# 8. Program kemudian menghitung rata-rata bilangan genap dan menampilkannya, jika ada bilangan genap.
# 9. Jika tidak ada bilangan genap, program memberikan pesan bahwa tidak ada bilangan genap di dalam range yang dimasukkan.

# Panggilan fungsi `jumlah_rata_bilangan_genap()` di akhir memulai eksekusi program, meminta input pengguna, dan menampilkan hasil perhitungan.
