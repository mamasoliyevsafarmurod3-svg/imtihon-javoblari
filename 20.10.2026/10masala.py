from matplotlib import pyplot
kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]

pyplot.plot(kunlar,daromad,marker = "o")
pyplot.title("Haftalik daromad")
pyplot.xlabel("Kunlar")
pyplot.ylabel("daromad")
pyplot.legend()
pyplot.grid("-")
pyplot.savefig("daromad.png")
pyplot.show()

