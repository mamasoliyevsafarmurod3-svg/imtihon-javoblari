def tashqi_funksiya(koeffitsiyent):
    
    def ichki_funksiya(son):
        return son * koeffitsiyent
    return ichki_funksiya
koeffitsiyent = 4
qiymat = 7
kopaytiruvchi_funksiya = tashqi_funksiya(koeffitsiyent)
natija = kopaytiruvchi_funksiya(qiymat)
print(f"Natija: {natija}")