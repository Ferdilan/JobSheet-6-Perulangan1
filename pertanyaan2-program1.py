r = 1
i = 1
a = 2
n = 4

while i <= n:
    r *= a
    i += 1

print(r)

# Program ini menghitung hasil pangkat dari bilangan 2 (a) dengan eksponen bilangan 4 (n) menggunakan loop while. Berikut adalah langkah-langkah eksekusi dan output dari program:

# 1. Awalnya, nilai r = 1, i = 1, a = 2, dan n = 4.
# 2. Loop akan dieksekusi selama i kurang dari atau sama dengan n. Karena i awalnya adalah 1 dan n adalah 4, maka loop akan dijalankan 4 kali.
# 3. Setiap kali loop dieksekusi, nilai r akan dikalikan dengan a. Jadi, langkah-langkah perhitungan adalah sebagai berikut:
#    - Iterasi 1: r = 1 * 2 = 2, i = 2
#    - Iterasi 2: r = 2 * 2 = 4, i = 3
#    - Iterasi 3: r = 4 * 2 = 8, i = 4
#    - Iterasi 4: r = 8 * 2 = 16, i = 5
# 4. Setelah 4 iterasi, i menjadi 5, dan kondisi loop (i <= n) tidak lagi terpenuhi, sehingga loop berhenti.
# 5. Program mencetak nilai terakhir da ri r, yaitu 16.

# Jadi, output dari program ini adalah:

# ```
# 16
# ```
