print("=======PROGRAM LOOP DENGAN CONTINUE=======")
b = 0
count = 0

for i in range(5): 
    angka = int(input("Masukkan bilangan: "))

    if angka >= 50:
        continue
    b += angka
    count += 1

total = float(b)
print("Jumlah angka kurang dari 50: ", total)
avg = float(b) / count if count != 0 else 0
print('Rata-rata angka kurang dari 50 : ',avg)
