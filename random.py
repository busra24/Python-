import random

liste = []
ilk_sayi = random.randint(0,101)
ikinci_sayi = random.randint(0,101)

print("Birinci rastgele sayı: ",ilk_sayi)
print("İkinci rastgele sayı: ",ikinci_sayi)

if ilk_sayi == ikinci_sayi:
    print("Sayılar eşit olduğundan program sonlanıyor.")
    
else:
    if ilk_sayi < ikinci_sayi:
        for i in range(ilk_sayi,ikinci_sayi + 1):
            if i % 2 == 1:
                liste.append(i)
        print("Oluşan tek sayılar: ",liste)
        print("Toplam sayı adeti: ",len(liste))

    else:
        for i in range(ikinci_sayi,ilk_sayi +1):
            if i % 2 == 1:
                liste.append(i)
        print("Oluşan tek sayılar: ",liste)
        print("Toplam sayı adeti: ",len(liste))
                    