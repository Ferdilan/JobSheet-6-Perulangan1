n = 5
hasil = 1

for i in range(1, n+1):
    hasil *= i

print(str(n) + "! = " + str(hasil))



# Program ini adalah sebuah program Python yang menghitung faktorial dari suatu angka `n`. Faktorial dari suatu angka `n`, dilambangkan dengan `n!`, adalah hasil perkalian semua bilangan bulat positif dari 1 hingga `n`.

# Berikut adalah penjelasan programnya baris per baris:

# 1. `n = 5`: Baris ini mendefinisikan variabel `n` dengan nilai 5. Ini adalah angka yang akan digunakan untuk menghitung faktorial.

# 2. `hasil = 1`: Baris ini mendefinisikan variabel `hasil` dengan nilai awal 1. Ini adalah variabel yang akan digunakan untuk mengakumulasi hasil perkalian.

# 3. `for i in range(1, n+1):`: Ini adalah loop `for` yang akan berjalan dari 1 hingga `n+1` (5+1 = 6). Dalam loop ini, `i` akan mengambil nilai dari 1 hingga 5.

# 4. `hasil *= i`: Pada setiap iterasi loop, nilai `i` akan dikalikan dengan `hasil`, dan hasilnya akan disimpan kembali ke variabel `hasil`. Ini bertujuan untuk mengakumulasi hasil perkalian.

# 5. `print(str(n) + "! = " + str(hasil))`: Setelah loop selesai berjalan, program akan mencetak hasil faktorial dari `n` dengan menggunakan pernyataan `print`. Ini akan mencetak teks dalam format "n! = hasil", di mana `n` adalah angka yang telah ditentukan sebelumnya, dan `hasil` adalah hasil faktorial yang telah dihitung.

# Hasil dari program ini akan mencetak "5! = 120", karena 5! (5 faktorial) adalah 1 * 2 * 3 * 4 * 5 = 120.