<<<<<<< HEAD
import math

phi=3.14

print("pilihan")
print("1.hitung keliling lingkaran")
print("2.hitung luas lingkaran")

pilihan=int(input("masukan pilihan (1/2):"))
jari_jari=float(input("masukan nilai jari jari:"))

if pilihan==1:
    keliling=2*phi*jari_jari
    print("keliling lingkaran=",keliling)
elif pilihan==2:
    luas=phi*jari_jari*jari_jari
    print("luas lingkaran=",luas)
else:
=======
phi=3.14

print("pilihan")
print("1.hitung keliling lingkaran")
print("2.hitung luas lingkaran")

pilihan=int(input("masukan pilihan (1/2):"))
jari_jari=float(input("masukan nilai jari jari:"))

if pilihan==1:
    keliling=2*phi*jari_jari
    print("keliling lingkaran=",keliling)
elif pilihan==2:
    luas=phi*jari_jari*jari_jari
    print("luas lingkaran=",luas)
else:
>>>>>>> 2ec96d263eb3764ea0584a90c3a5b74da3eb8d9d
    print("pilihan tidak valid")