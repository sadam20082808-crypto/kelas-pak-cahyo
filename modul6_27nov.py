

penumpang = ["William", "Kate", "Anderson", "Jame", "Mady"]
print(penumpang)


penumpang.append("Jones")
print(penumpang)


penumpang[penumpang.index("Anderson")] = "Grace"
print(penumpang)


print("Thompson" in penumpang)


penumpang.sort()
print(penumpang)


for nama in penumpang:
    print(nama)


penumpang.clear()
print(penumpang)
