import csv
mahsulotlar = [
    ["Olma", 8000, 12],
    ["Non", 4000, 20],
    ["Sut", 14000, 5]
]
with open("products.csv", "w", newline="",) as f:
    yozuvchi = csv.writer(f)
    yozuvchi.writerow(["nom", "narx", "soni"])
    yozuvchi.writerows(mahsulotlar)
print(" muvaffaqiyatli yaratildi!")