print("=======PROGRAM MENGHITUNG NILAI FAKTORIAL DENGAN FOR=======")
n = int(input("Masukkan bilangan bulat positif: "))

faktorial = 1

for i in range(1, n + 1):
    faktorial *= i

print(f"Faktorial dari {n} adalah {faktorial}")


print("=======PROGRAM MENGHITUNG NILAI FAKTORIAL DENGAN WHILE=======")
n = int(input("Masukkan bilangan bulat positif: "))

faktorial = 1

i = 1
while i <= n:
    faktorial *= i
    i+=1

print(f"Faktorial dari {n} adalah {faktorial}")
