#menginisialisasi dua bilangan pertama dalam deret Fibonacci
a, b = 0, 1

#Menampilkan bilangan pertama dalam deret
print(a, end=" ")

#Menentukan jumlah angka dalam deret Fibonacci yang ingin ditampilkan
jumlah_angka = 8  # Ganti dengan jumlah angka yang diinginkan

#menghitung dan menampilkan deret Fibonacci
for _ in range(jumlah_angka - 1):
    a, b = b, a + b
    print(a, end=" ")


#Penjelasan
# Program tersebut adalah implementasi sederhana dari deret Fibonacci menggunakan bahasa pemrograman Python. Mari kita bahas langkah-langkahnya:

# 1. Inisialisasi dua variabel `a` dan `b` dengan nilai 0 dan 1. Ini merupakan dua angka pertama dalam deret Fibonacci.

# 2. Menampilkan nilai variabel `a` menggunakan perintah `print(a, end=" ")`. Ini mencetak nilai `a` tanpa membuat baris baru dan menambahkan spasi setelah nilai.

# 3. Menggunakan loop `for` untuk menghasilkan deret Fibonacci selanjutnya. Loop ini berjalan sebanyak `jumlah_angka - 1` kali, karena kita sudah menampilkan satu angka pertama sebelumnya.

# 4. Di dalam loop, nilai `a` diperbarui menjadi nilai `b`, dan nilai `b` diperbarui menjadi penjumlahan nilai `a` dan `b`. Ini mengikuti aturan deret Fibonacci, di mana setiap angka dalam deret adalah hasil penjumlahan dua angka sebelumnya.

# 5. Menampilkan nilai `a` di setiap iterasi loop menggunakan perintah `print(a, end=" ")`.
