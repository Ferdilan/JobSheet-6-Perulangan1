n = 5
stop = False 
i = 1

while not stop:
    if i >= n:
        stop = True
    if i % 2 == 1:
        print("#", end="")
    else:
        print("*", end="")
    i += 1


#Urutan
# 1. Awalnya, `n = 5`, `stop = False`, dan `i = 1`.
# 2. Loop akan dieksekusi selama kondisi `not stop` benar, yang berarti loop akan berjalan hingga `stop` menjadi True.
# 3. Di setiap iterasi, program memeriksa apakah `i` lebih besar dari atau sama dengan `n`. Jika ya, maka program mengatur `stop` menjadi True, sehingga loop akan berhenti.
# 4. Selama loop berjalan, program juga memeriksa apakah `i` adalah bilangan ganjil (jika `i % 2 == 1`) atau genap. Jika `i` ganjil, maka program mencetak karakter '#', jika `i` genap, maka program mencetak karakter '*'.
# 5. Setelah mencetak karakter, `i` ditambahkan dengan 1.
# 6. Proses ini akan terus berlanjut sampai `i` mencapai atau melebihi 5.
# 7. Setelah `i` mencapai 5, loop akan berhenti karena kondisi `stop` menjadi True.
# 8. Output dari program adalah karakter '#' dan '*' secara bergantian hingga `i` mencapai atau melebihi 5.