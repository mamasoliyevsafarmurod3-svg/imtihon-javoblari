def tahlil_qil(sonlar):
    juftyigindi = 0
    toqyigindi = 0
    
    for son in sonlar:
        if son % 2 == 0:
            juftyigindi += son
        else:
            toqyigindi += son
            
    eng_katta = max(sonlar)
    
    print(f"Juft sonlar yig'indisi: {juftyigindi}")
    print(f"Toq sonlar yig'indisi: {toqyigindi}")
    print(f"Eng katta son: {eng_katta}")

sonlar = [12, 7, 5, 18, 9, 4]
tahlil_qil(sonlar)