def TersCevir(kelime):
    uzunluk = len(kelime)
    ters = ""
    for i in range(uzunluk-1,-1,-1):
        ters += kelime[i]

    if ters == kelime:
        print("Tersten yazılışı aynıdır.")
        print("Girdiğiniz kelime: ",kelime)
        print("Tersten yazılışı: ",ters)

    else:
        print("Tersten yazılışı farklıdır.")
        print("Girdiğiniz kelime: ",kelime)
        print("Tersten yazılışı: ",ters)

kelime = input("Kelimeyi giriniz: ")
TersCevir(kelime)
