
# Membuat dictionary nilai ujian hari pertama
nilai = {
    "Mady": 8,
    "Roger": 5,
    "Paul": 5,
    "Lucy": 7
}
print(nilai)

# Membuat dictionary nilai ujian hari kedua
nilai_susulan = {
    "Ken": 8,
    "Andrea": 7,
    "Smith": 6
}
print(nilai_susulan)

# Menggabungkan dictionary
nilai.update(nilai_susulan)
print(nilai)

# Mengubah nilai Roger, Paul, dan Smith menjadi 8
nilai["Roger"] = 8
nilai["Paul"] = 8
nilai["Smith"] = 8
print(nilai)

#nama dan nilai yang lebih dari atau sama dengan 8
for nama, hasil in nilai.items():
    if hasil >= 8:
        print(nama, "=", hasil)
