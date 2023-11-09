print("=======PROGRAM LOOP DENGAN BREAK=======")
b = 0
for i in range(51): #51 sebbagai batas maksimum iterasi
    angka = int(input("Masukkan bilangan: "))
    b += angka

    if b > 50:
        break

print('berhenti pada bilangan: ',b)


print("=======PROGRAM LOOP DENGAN BREAK=======")
b = 0
i = 1
while True:
    angka = int(input("Masukan bilangan: "))
    b += angka
    if b > 50:
         break

print("berhenti pada bilangan: ", b)