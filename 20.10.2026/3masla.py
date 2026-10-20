mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}
nomi = input("Mahsulot nomi ")
narxi = int(input("yangi narxi:"))
for mahsulot in mahsulotlar:
    if nomi == mahsulot:
        mahsulotlar[nomi] = narxi
        print("narx yangilandi: ")
        print(mahsulotlar)
        break
else:
    print("bunday mahsulot topilmadi:")