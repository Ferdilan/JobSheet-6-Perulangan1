def jumlah_rata_bilangan_ganjil():
    #input user
    n = int(input("Masukkan bilangan bulat N: "))

    #inisialisasi variabel
    total_ganjil_kuadrat = 0
    jumlah_ganjil = 0

    #hitung jumlah dan banyaknya bilangan ganjil
    for i in range(1, n + 1):
        if i % 2 != 0:
            total_ganjil_kuadrat += i ** 2
            jumlah_ganjil += 1

    #menampilkan hasil
    print(f"Banyaknya bilangan ganjil dari 1 sampai {n} adalah {jumlah_ganjil}")
    print(f"Jumlah kuadrat bilangan ganjil dari 1 sampai {n} adalah {total_ganjil_kuadrat}")

    # menghitung dan menampilkan rata-rata kuadrat bilangan ganjil
    if jumlah_ganjil > 0:
        rata_ganjil_kuadrat = total_ganjil_kuadrat / jumlah_ganjil
        print(f"Rata-rata kuadrat bilangan ganjil dari 1 sampai {n} = {rata_ganjil_kuadrat:.2f}")
    else:
        print("Tidak ada bilangan ganjil di dalam range yang dimasukkan.")

# Memanggil fungsi
jumlah_rata_bilangan_ganjil()

# #Penjelasan
# Program ini menghitung jumlah, total kuadrat, dan rata-rata kuadrat dari bilangan ganjil dalam rentang 1 sampai N. Mari kita jelaskan langkah-langkahnya:

# 1. Pengguna diminta untuk memasukkan sebuah bilangan bulat positif N.
# 2. Variabel `total_ganjil_kuadrat` dan `jumlah_ganjil` diinisialisasi sebagai 0. `total_ganjil_kuadrat` akan digunakan untuk menyimpan jumlah kuadrat dari bilangan ganjil, sedangkan `jumlah_ganjil` akan menyimpan banyaknya bilangan ganjil.
# 3. Program menggunakan loop `for` untuk mengiterasi melalui bilangan dari 1 sampai N.
# 4. Pada setiap iterasi, program memeriksa apakah bilangan tersebut ganjil dengan menggunakan kondisi `if i % 2 != 0`. Jika ganjil, maka program akan menambahkan kuadrat dari bilangan tersebut ke dalam `total_ganjil_kuadrat` dan menambahkan 1 ke dalam `jumlah_ganjil`.
# 5. Setelah selesai iterasi, program menampilkan banyaknya bilangan ganjil dan jumlah kuadrat bilangan ganjil dalam rentang 1 sampai N.
# 6. Program kemudian menghitung rata-rata kuadrat bilangan ganjil dengan membagi `total_ganjil_kuadrat` oleh `jumlah_ganjil`. Hasilnya ditampilkan dengan dua desimal.
# 7. Jika tidak ada bilangan ganjil dalam rentang yang dimasukkan, program memberikan pesan bahwa tidak ada bilangan ganjil.

# Sebagai contoh, jika pengguna memasukkan N=5, program akan menghitung jumlah, total kuadrat, dan rata-rata kuadrat dari bilangan ganjil 1, 3, dan 5 dalam rentang tersebut.